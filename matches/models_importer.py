# coding=UTF-8
'''
Created on Apr 27, 2014

@author: mvgagliotti
'''
import codecs
import datetime
import os
import shutil
from zipfile import ZipFile

from django.db import transaction, connection

from fut_friends import settings
from fut_friends.common import JsonHelper, int_or_none
from matches.models import Championship, ConcreteChampionship, Season, Team, \
    ConcreteTeam, MatchPlayer, Match, TeamPlayer, Player, Goal, MatchSubstitution, \
    ChampionshipPhase, PhaseGroup, Referee, Coach, Stadium
from matches.models_dtos import MatchDTO, PlayerDTO, ChampDTO


def test_import():
    
#     import_match(os.path.expanduser("~") + '/' + "Campeonato_Brasileiro_2013_16_10_2013_Santos_Internacional.json")
#     import_match(os.path.expanduser("~") + '/' + "Campeonato_Brasileiro_2013_14_08_2013_Vitória_Ponte_Preta.json")
#     import_match(os.path.expanduser("~") + '/' + "Copa_do_Mundo_1958_17_06_1958_Irlanda_do_Norte_Tchecoslováquia.json")
    
#     import_champ(champ_name="Copa do Mundo", champ_season=1994, skip=0)
#     import_champ(champ_name="Copa do Mundo", champ_season=2010)
    import_champ(champ_name="Campeonato Brasileiro", champ_season=2013, is_from_national_team=False)    

def import_champ(champ_name, champ_season, is_from_national_team=True, skip=0, importer_entry=None):
    
    '''
    1. Vamos buscar o Championship: se não existir com o nome o criamos. 
       Em seguida, verificamos ConcreteChampionship/Season e os criamos caso seja necessário
    '''
    
    champ_file_name = champ_name.replace(" ","_") + "_" + unicode(champ_season)    
    filename = os.path.join(settings.IMPORTER_PATH, champ_file_name  + ".json")
    champ_file = codecs.open(filename, 'r', 'utf-8-sig')
    json_str = champ_file.read()
    champ_dto = JsonHelper.to_object(json_str)
        
    champ_result = Championship.objects.filter(name__exact=champ_name)
    
    if champ_result:
        championship = champ_result[0]
    else: 
        championship = Championship(name=champ_name)
        championship.save()
    

    concrete_champ_resultset = ConcreteChampionship.objects. \
        filter(season__start_year=int(champ_season), championship=championship)
    
    if concrete_champ_resultset:
        concrete_championship = concrete_champ_resultset[0]
        season = concrete_championship.season
    else:
        season_resultset = Season.objects.filter(start_year=int(champ_season))
        if season_resultset:
            season = season_resultset[0]
        else:
            season = Season(start_year=int(champ_season), end_year=int(champ_season))
            season.save()
    
        concrete_championship = ConcreteChampionship(championship=championship, season=season)
        '''
        jogando datas atuais para start_date e end_date: depois de importar partidas, muda isto
        '''
        concrete_championship.start_date = datetime.datetime.now()
        concrete_championship.end_date = datetime.datetime.now()
        concrete_championship.match_count = champ_dto.match_count
        
        concrete_championship.save()
    
    '''
    Partidas
    '''
    json_files = get_files_from_championship(champ_name.replace(" ","_"), champ_season)
    '''
    Salvando qtde de partidas no importer_entry
    '''
    if importer_entry:
        importer_entry.matchs_to_import = len(json_files)
        importer_entry.save()
    
    imported=0
    for _file in json_files:
        if imported < skip:
            imported = imported+1
            continue
#         print "Importando arquivo %s".decode('utf-8') % (_file)
        match = import_match(_file, concrete_championship, is_from_national_team)
        imported=imported+1
#         print unicode(match).decode('utf-8') + ' importada com sucesso; %d partidas importadas de um total de %d' % (imported, champ_dto.match_count)
        
        '''
        Atualizando MatchImporter
        '''        
        if importer_entry:
            importer_entry.imported_matches = importer_entry.imported_matches + 1
            importer_entry.save()

    '''
    Salvando campeão e data de início e fim
    '''
    champion = concrete_championship.participants.filter(team__short_name__exact=champ_dto.champion)[0]
    first_game = concrete_championship.match_set.all().order_by('match_date')[:1][0]
    start_date = first_game.match_date
    last_game = concrete_championship.match_set.all().order_by('-match_date')[:1][0] 
    end_date = last_game.match_date
    
    concrete_championship.start_date = start_date
    concrete_championship.end_date = end_date
    concrete_championship.champion = champion
    
    concrete_championship.save()


def get_files_from_championship(champ_name, season):
    _starts_with = champ_name.decode('utf-8') + "_" + unicode(season).decode('utf-8')
    _files = [ _file.decode('utf-8') for _file in os.listdir(settings.IMPORTER_PATH) ]
    _jsons = [_file for _file in _files if _file.startswith(_starts_with)               
              and _file.endswith(u'.json')
              and (not _file == (_starts_with+u'.json').decode('utf-8'))]
    return sorted(_jsons)


@transaction.atomic
def import_match(filepath, concrete_championship, is_national_team=False):
    '''
    Importa uma partida, dado o caminho para o arquivo json-dto
    '''
    
    season = concrete_championship.season
    
    '''
    Lê o arquivo o e obtém o DTO
    '''    
    match_file = codecs.open(os.path.join(settings.IMPORTER_PATH,filepath), 'r', 'utf-8-sig')  # tem que usar o codes.open!
    json_str = match_file.read()
    match_dto = JsonHelper.to_object(json_str)
            
        
    '''
    Times da partida
    '''    
    home_concrete_team = get_concrete_team(match_dto.home_team, season, is_national_team)
    away_concrete_team = get_concrete_team(match_dto.away_team, season, is_national_team)
        
        
    concrete_championship.participants.add(home_concrete_team, away_concrete_team)
    
    '''
    Obtendo a data da partida
    '''
    date_data = match_dto.match_date.split('/')    
    match_date = datetime.datetime(day=int(date_data[0]), month=int(date_data[1]), year=int(date_data[2]))
    
    '''
    Estádio
    '''
    stadium = None
    if match_dto.stadium:
        stadium_result_set = Stadium.objects.filter(short_name__istartswith=match_dto.stadium)
        if stadium_result_set:
            stadium = stadium_result_set[0]
        else:
            stadium = Stadium(short_name=match_dto.stadium)
            stadium.save()
    
    '''
    Técnicos
    '''
    def get_coach(coach_name):
        coach_resultset = Coach.objects.filter(name=coach_name)
        if coach_resultset:
            return coach_resultset[0]
        else:
            coach = Coach(name=coach_name, nick="na")
            coach.save()
            return coach 
    
    '''
    Time mandante: criando o técnico da equipe e setando em ht_coach pra associar
    à partida mais à frente
    '''
    if home_concrete_team.coach:
        if home_concrete_team.coach.name == match_dto.home_team_coach: #se tem o mesmo nome, pega o do time
            ht_coach = home_concrete_team.coach
        else:
            ht_coach = get_coach(match_dto.home_team_coach) 
    else:
        ht_coach = Coach(name=match_dto.home_team_coach, nick="na")
        ht_coach.save()
        home_concrete_team.coach = ht_coach
        home_concrete_team.save()

    '''
    Time visitante: criando o técnico da equipe e setando em at_coach pra associar
    à partida mais à frente
    '''
    if away_concrete_team.coach:
        if away_concrete_team.coach.name == match_dto.away_team_coach: #se tem o mesmo nome, pega o do time
            at_coach = away_concrete_team.coach
        else:
            at_coach = get_coach(match_dto.away_team_coach) 
    else:
        at_coach = Coach(name=match_dto.away_team_coach, nick="na")
        at_coach.save()
        away_concrete_team.coach = at_coach
        away_concrete_team.save()

    '''
    Buscando ou criando partida
    '''
    
    match_just_created = False
        
    match_resultset = Match.objects.filter(
           championship__id__exact=concrete_championship.id,
           match_date__day=match_date.day,
           match_date__month=match_date.month,
           match_date__year=match_date.year,
           home_team__id__exact=home_concrete_team.id,
           away_team__id__exact=away_concrete_team.id)
    
    if match_resultset:
        match = match_resultset[0]
        match.home_team_coach = ht_coach
        match.away_team_coach = at_coach
    else:         
        match = Match(championship=concrete_championship,
                      home_team=home_concrete_team,
                      away_team=away_concrete_team,
                      match_date=match_date,
                      home_team_coach=ht_coach,
                      away_team_coach=at_coach)        
        match_just_created = True
    
    match.stadium = stadium
    match.round_number = int_or_none(match_dto.round)    
    match.save()
    
    '''
    Partida recém criada
    '''
    
    '''
    Placar da partida
    '''
    match.home_team_goals = match_dto.home_team_goals
    if match_dto.home_team_penalty_goals > 0:
        match.home_team_penalty_goals = match_dto.home_team_penalty_goals
    match.away_team_goals = match_dto.away_team_goals
    if match_dto.away_team_penalty_goals > 0:
        match.away_team_penalty_goals = match_dto.away_team_penalty_goals
    
    '''
    Árbitro e auxiliares
    '''
    if match_dto.referee:
        referee_resultset = Referee.objects.filter(name=match_dto.referee.name)
        
        if referee_resultset:
            referee = referee_resultset[0]
        else:
            referee = Referee(name=match_dto.referee.name, birth_data=match_dto.referee.birth_data[:30]) #TODO: Bug aqui
            referee.save()
        
        match.referee = referee
             
    if match_dto.referee_aux1:
        referee_aux1_resultset = Referee.objects.filter(name=match_dto.referee_aux1.name)
        if referee_aux1_resultset:
            referee_aux1 = referee_aux1_resultset[0]
        else:
            referee_aux1 = Referee(name=match_dto.referee_aux1.name, birth_data=match_dto.referee_aux1.birth_data[:30])
            referee_aux1.save()
        match.referee_ass1 = referee_aux1 
        
    if match_dto.referee_aux2:
        referee_aux2_resultset = Referee.objects.filter(name=match_dto.referee_aux2.name)
        if referee_aux2_resultset:
            referee_aux2 = referee_aux2_resultset[0]
        else:
            referee_aux2 = Referee(name=match_dto.referee_aux2.name, birth_data=match_dto.referee_aux2.birth_data[:30])
            referee_aux2.save()
        match.referee_ass2 = referee_aux2 
    
    
    match.save()
    
    '''
    Fase do campeonato
    '''
    phase = None
    if match_dto.champ_phase != "":
        ch_phase_resultset = concrete_championship.championshipphase_set.filter(name=match_dto.champ_phase)
        if ch_phase_resultset:
            phase = ch_phase_resultset[0]
        else:
            '''
            Falta associar: num. de rodadas, se eh divida em grupos e a ordem da fase
            '''
            phase = ChampionshipPhase(name=match_dto.champ_phase, championship=concrete_championship)
            phase.save()
    
        match.championshipPhase = phase
    
    '''
    Grupo: 
    '''
    if match_dto.champ_group != "":
        
        if not phase:
            phase = ChampionshipPhase(name="Fase Única", championship=concrete_championship)
            phase.save()
        
        gr_resultset =  phase.phasegroup_set.filter(name=match_dto.champ_group)
        
        if gr_resultset:
            group = gr_resultset[0] 
        else:
            '''
            Associando participantes do grupo: home e away
            '''
            group = PhaseGroup(name=match_dto.champ_group, phase=phase)
            group.save()
            
            group.participants.add(home_concrete_team)
            group.participants.add(away_concrete_team)
            
            group.save()
    
        match.phaseGroup = group
    
    match.save()
    
    
    '''
    2.1 Jogadores do time mandante
    '''
    '''
    Titulares
    '''
    
    for player_dto in match_dto.home_team_players:
        match_player = get_match_player(player_dto, home_concrete_team, match)
        '''
        gols marcados e cartões levados
        '''
        set_player_goals_and_cards(player_dto, match, match_player, True)
            
    '''
    Reservas que entraram
    '''
    for sub_dto in match_dto.home_team_subs:
        player_dto = sub_dto.p_in
        
        player_in = get_match_player(player_dto, home_concrete_team, match)
        player_in.substitute = True
        player_in.save()        
        
        player_out = get_match_player(sub_dto.p_out, home_concrete_team, match) 
        
        match_sub_resultset = MatchSubstitution.objects.filter(match=match, 
                                                               player_in=player_in.player, 
                                                               player_out=player_out.player)
        if match_sub_resultset:
            pass
        else:
            splitted = sub_dto.time.split('_')
            sub_minute = int_or_none(splitted[0])
            if len(splitted) > 1:
                sub_match_time = splitted[1]
            else:
                sub_match_time = ""
            
            match_sub = MatchSubstitution(match=match,
                                          player_in=player_in.player,
                                          player_out=player_out.player,
                                          from_home_team=True,
                                          minute=sub_minute,
                                          match_time=sub_match_time)
            match_sub.save()
            
                
    '''
    3.1 Jogadores do time visitante
    '''
    for player_dto in match_dto.away_team_players:
        match_player = get_match_player(player_dto, away_concrete_team, match, False)
        '''
        gols marcados e cartões levados
        '''
        set_player_goals_and_cards(player_dto, match, match_player, False)
            
    '''
    Reservas que entraram
    '''
    for sub_dto in match_dto.away_team_subs:
        player_dto = sub_dto.p_in
        
        match_player = get_match_player(player_dto, away_concrete_team, match, False)
        match_player.substitute = True
        match_player.save()

        player_out = get_match_player(sub_dto.p_out, away_concrete_team, match, False) 
        
        match_sub_resultset = MatchSubstitution.objects.filter(match=match, 
                                                               player_in=match_player.player, 
                                                               player_out=player_out.player)
        if match_sub_resultset:
            pass
        else:
            splitted = sub_dto.time.split('_')
            sub_minute = int_or_none(splitted[0])
            if len(splitted) > 1:
                sub_match_time = splitted[1]
            else:
                sub_match_time = ""
            
            match_sub = MatchSubstitution(match=match,
                                          player_in=match_player.player,
                                          player_out=player_out.player,
                                          from_home_team=False,
                                          minute=sub_minute,
                                          match_time=sub_match_time)
            match_sub.save()
    
    return match
    

def set_player_goals_and_cards(player_dto, match, match_player, scored_by_home_team):
    '''
    Dado um playerDTO, define os gols e cartões do MatchPlayer
    '''

    '''
    Gols 
    '''        
    for goal_dto in player_dto.goals:
        splitted = goal_dto.time.split('_')
        
        g_minute = int_or_none(splitted[0])
                    
        if len(splitted) > 1:
            g_match_time = splitted[1]
        else:
            g_match_time = ""
        
        auto_gol = goal_dto.auto
        
        '''
        Definindo a equipe, baseado em dois booleans: scored_by_home_team e auto_gol 
        '''        
        if scored_by_home_team:
            if not auto_gol:
                concrete_team = match.home_team
                in_favor_of_home_team = True;
            else:
                concrete_team = match.away_team
                in_favor_of_home_team = False;
                
        else:
            if not auto_gol:
                concrete_team = match.away_team
                in_favor_of_home_team = False;                
            else:
                concrete_team = match.home_team
                in_favor_of_home_team = True                
                 
        goal_resultset = Goal.objects.filter(
                 match=match,
                 in_favor_of=concrete_team,
                 in_favor_of_home_team=in_favor_of_home_team,
                 scored_by=match_player.player,
                 minute=g_minute,
                 match_time=g_match_time,
                 auto_gol=auto_gol)
        
        if goal_resultset:
            goal = goal_resultset[0]
        else:
            goal = Goal(match=match,
                        scored_by=match_player.player,
                        minute=g_minute,
                        match_time=g_match_time,
                        auto_gol=auto_gol,
                        in_favor_of=concrete_team,
                        in_favor_of_home_team=in_favor_of_home_team)
            goal.save()
                        
    '''
    Cartões
    '''
    if player_dto.first_yellow_card:
        match_player.first_yellow_card = True
        if player_dto.first_yellow_card.time.find('_') > -1:
            splitted = player_dto.first_yellow_card.time.split('_')
            match_player.first_yellow_card_minute = int_or_none(splitted[0])
            if len(splitted) > 1:
                match_player.first_yellow_card_time = splitted[1]
    
    if player_dto.second_yellow_card:
        match_player.second_yellow_card = True
        match_player.red_card = True
        
        if player_dto.second_yellow_card.time.find('_') > -1:
            splitted = player_dto.second_yellow_card.time.split('_')
            match_player.second_card_or_red_card_minute = int_or_none(splitted[0])
            if len(splitted) > 1:
                match_player.second_card_or_red_card_time = splitted[1]
        
    else:
        if player_dto.red_card:
            match_player.red_card = True
            
            if player_dto.red_card.time.find('_') > -1:
                splitted = player_dto.red_card.time.split('_')
                match_player.second_card_or_red_card_minute = int_or_none(splitted[0])
                if len(splitted) > 1:
                    match_player.second_card_or_red_card_time = splitted[1]
    
    match_player.save()
    

def get_match_player(player_dto, concrete_team, match, from_home_team=True):    
    '''
    Obtém o MatchPlayer a partir do nome do jogador: 
    Já cria também Player e TeamPlayer caso seja necessário    
    '''    
    player_result_set = concrete_team.teamplayer_set.filter(player__name__iexact=player_dto.name) 
    
    if player_result_set:
        team_player = player_result_set[0] 
    else:
        player_rs = Player.objects.filter(name__iexact=player_dto.name)
        
        if player_rs:
            player = player_rs[0]
        else:        
            player = Player(name=player_dto.name, nick=player_dto.name)
            player.save()
        
        team_player = TeamPlayer(player=player, concrete_team=concrete_team, substitute=player_dto.substitute, position=player_dto.position)
        team_player.save()
    
    match_player_resultset = \
        MatchPlayer.objects.filter(
               match=match,
               player=team_player.player,
               from_home_team=from_home_team)
    
    if match_player_resultset:     
        match_player = match_player_resultset[0]
    else:           
        match_player = MatchPlayer(
                                   player=team_player.player, 
                                   match=match, team=concrete_team, 
                                   substitute=player_dto.substitute, 
                                   position=player_dto.position, 
                                   from_home_team=from_home_team)
        match_player.save()
        
    return match_player
    

def get_concrete_team(name, season, is_national_team):
    '''
    Obtém o ConcreteTeam baseado no nome do time, temporada e se é seleção ou não
    '''    
    concrete_team_resultset = ConcreteTeam. \
        objects.filter(team__short_name__istartswith=name, 
                       team__is_national_team=is_national_team,
                       season=season)
        
    if concrete_team_resultset:
        concrete_team = concrete_team_resultset[0]
    else:         
        team_resultset = Team.objects.filter(short_name=name)
        if team_resultset:
            team = team_resultset[0]
        else:
            team = Team(short_name=name, is_national_team=is_national_team)
            team.save()

        concrete_team = ConcreteTeam(team=team, season=season)
        concrete_team.save()
    
    return concrete_team
    
def save_zip_file(path, champ_name, champ_season):    
    '''
    Salva um arquivo zip do campeonato.
    '''    
    zip_name = path  + '/' + champ_name.replace(" ","_") + "_" + unicode(champ_season) + '.zip'    
    zip_file = ZipFile(zip_name,'w')
    
    '''
    JSON do campeonato
    '''
    
    champ_file_name = os.path.join(settings.IMPORTER_PATH, champ_name.replace(" ","_") + "_" + unicode(champ_season) + ".json")
    zip_file.write(os.path.join(path, champ_file_name))
    
    '''
    JSONs das partidas
    '''
    json_matches = get_files_from_championship(champ_name.replace(" ","_"), champ_season)
    for _file in json_matches:
        zip_file.write(os.path.join(settings.IMPORTER_PATH, _file))
    
    zip_file.close()
    
    '''
    Remove os JSON's
    '''
    remove_json_files(champ_name.replace(" ","_"), champ_season)

def read_zip_file(zip_file_name, destination_path):
    '''
    Lê um arquivo ZIP e extrai o conteúdo para destination_path
    '''
    with ZipFile(zip_file_name) as zip_file:
        for member in zip_file.namelist():
            filename = os.path.basename(member)
            # skip directories
            if not filename:
                continue
    
            # copy file (taken from zipfile's extract)
            source = zip_file.open(member)
            target = file(os.path.join(destination_path, filename), "wb")
            with source, target:
                shutil.copyfileobj(source, target)    

def remove_json_files(champ_name, champ_season):
    '''
    Remove os json de partidas e do campeonato
    '''
    
    json_matches = get_files_from_championship(champ_name, champ_season)
    for _file in json_matches:
        os.remove(os.path.join(settings.IMPORTER_PATH,_file))
    
    champ_file_name = os.path.join(settings.IMPORTER_PATH, champ_name + "_" + unicode(champ_season) + ".json")
    os.remove(champ_file_name)
        
    
if __name__ == "__main__":
#     read_zip_file(os.path.expanduser("~") + '/' + 'Campeonato_Brasileiro_2013.zip', os.path.expanduser("~") + '/tempJSON')
#     save_zip_file(os.path.join(os.path.expanduser("~"), 'test_importing'),"Campeonato_Brasileiro", 2013)
    test_import()
#     read_zip_file(os.path.join(os.path.expanduser("~"), 'test_importing','Campeonato_Brasileiro_2013.zip'), 
#                   os.path.join(os.path.expanduser("~"), 'test_importing'))    
