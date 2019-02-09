# coding=UTF-8
from django.db import models, transaction
from django.utils.translation import ugettext_lazy as _
from cities.models import *
from comments.models import Thread
from django.contrib.auth import get_user_model
import datetime

# Create your models here.
'''
Um time: pode ser um clube ou uma seleção
'''
class Team(models.Model):
    full_name = models.CharField("nome completo", max_length=100)
    short_name = models.CharField("nome resumido", max_length=40)
    is_national_team = models.BooleanField(u"seleção?", default=False)
    logo = models.CharField("Escudo", max_length=200, null=True, blank=True)
    
    def __unicode__(self):
        return self.short_name
    
    class Meta:
        verbose_name_plural = u"clubes ou seleções"
        verbose_name = u"clube ou seleção"
        ordering = ['short_name']


'''
Uma temporada. Normalmente eh um ano, mas pode ser dois. ex: 2013/2014
'''
class Season(models.Model):
    start_year = models.IntegerField(u"Ano de início")
    end_year = models.IntegerField(u"Ano de término")

    def __unicode__(self):
        if self.start_year == self.end_year:
            return unicode(self.start_year)
        else:
            return unicode(self.start_year) + "/" + unicode(self.end_year)
    
    class Meta:
        verbose_name_plural = "Temporadas"
        verbose_name = "Temporada"
        

'''
Um técnico
'''
class Coach(models.Model):
    name = models.CharField("nome", max_length=50)
    nick = models.CharField("apelido", max_length=50)    
    country_of_birth = models.ForeignKey(Country, verbose_name=_(u"país de nascimento"), null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = u"Técnicos"
        verbose_name = u"Técnico"
    
        
'''
Uma equipe. Representa um time em uma determinada temporada.
'''
class ConcreteTeam(models.Model):
    team = models.ForeignKey(Team, verbose_name=u"clube ou seleção")
    season = models.ForeignKey(Season, verbose_name="temporada")
    coach = models.ForeignKey(Coach, verbose_name=u"técnico", null=True, blank=True)

    def __unicode__(self):
        return self.team.short_name + " - " + unicode(self.season) 

    
    def save(self, *args, **kwargs):
        if self.id:
            pass
        super(ConcreteTeam, self).save(args,kwargs)
    class Meta:
        verbose_name_plural = "Equipes"
        verbose_name = "Equipe"    

'''
Um campeonato
'''
class Championship(models.Model):
    name = models.CharField("nome", max_length=40)
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Campeonatos"
        verbose_name = "Campeonato"    

'''
Um campeonato concreto (que ocorre em uma determinada temporada)
'''
class ConcreteChampionship(models.Model):
    championship = models.ForeignKey(Championship, verbose_name="campeonato")
    season = models.ForeignKey(Season, verbose_name="temporada")
    start_date = models.DateField(u'data de início')
    end_date = models.DateField(u'data de término', null=True, blank=True)
    participants = models.ManyToManyField(ConcreteTeam, verbose_name="participantes", null=True, blank=True)
    champion = models.ForeignKey(ConcreteTeam, verbose_name=u"campeão", related_name="champion", null=True, blank=True)
    match_count = models.PositiveSmallIntegerField(u"número de jogos", null=True, blank=True)
    
    def __unicode__(self):
        return unicode(self.championship.name) + "-" + unicode(self.season) 

    class Meta:
        verbose_name_plural = u"Edições de campeonato"
        verbose_name = u"Edição de um campeonato"
    
    
'''
Fase de um campeonato: ex: fase de classificação, oitavas-de-final, final, etc..
'''
class ChampionshipPhase(models.Model):
    name = models.CharField("nome", max_length=50)
    championship = models.ForeignKey(ConcreteChampionship, verbose_name="campeonato")
    rounds = models.PositiveSmallIntegerField(u"número de rodadas da fase", default=1)
    groups = models.BooleanField(u"dividida em grupos?", default=False)
    phase_order = models.PositiveSmallIntegerField("ordem", default=1)

    def __unicode__(self):
        return self.name + " do(a) " + unicode(self.championship) 

    class Meta:
        verbose_name_plural = "Fases do campeonato"
        verbose_name = "Fase do campeonato"    


'''
Grupos de uma fase
'''
class PhaseGroup(models.Model):
    name = models.CharField("nome", max_length=25)    
    phase = models.ForeignKey(ChampionshipPhase, verbose_name="fase")
    participants = models.ManyToManyField(ConcreteTeam, verbose_name="participantes", null=True, blank=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "grupos"
        verbose_name = "grupo"    
    
'''
Tabela de classificação
Pode ser montada automaticamente a partir dos jogos cadastrados
'''    
class ChampionshipTable(models.Model):
    team = models.ForeignKey(ConcreteTeam, verbose_name=u"clube/seleção")
    phase = models.ForeignKey(ChampionshipPhase, verbose_name="fase")
    round = models.PositiveSmallIntegerField("rodada", default=1)
    matches_played = models.PositiveSmallIntegerField("partidas jogadas", default=0)
    matches_won = models.PositiveSmallIntegerField("partidas vencidas", default=0)
    matches_drawn = models.PositiveSmallIntegerField("partidas empatadas", default=0)
    matches_lost = models.PositiveSmallIntegerField("partidas perdidas", default=0)
    goals_scored = models.PositiveSmallIntegerField("gols marcados", default=0) 
    goals_against = models.PositiveSmallIntegerField("gols levados", default=0)
    points = models.PositiveSmallIntegerField("pontos", default=0) 
     
'''
Dados de um jogador
'''    
class Player(models.Model):
    name = models.CharField("nome", max_length=100)
    nick = models.CharField("apelido", max_length=50)
    current_team = models.ForeignKey(Team, verbose_name="clube atual", null=True, blank=True)
    birth_city = models.ForeignKey(City, verbose_name=_("Cidade"), null=True, blank=True)
    country_of_birth = models.ForeignKey(Country, verbose_name=_(u"país de nascimento"), related_name="country_of_birth",  null=True, blank=True)
    second_nationality = models.ForeignKey(Country, verbose_name=_("naturalizado"), related_name="second_nationality",  null=True, blank=True)
    

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Jogadores"
        verbose_name = "Jogador"    


'''
Histórico de um jogador: cada registro desta tabela corresponde a uma passagem do jogador pelo time
'''
class PlayerHistoryEntry(models.Model):
    player = models.ForeignKey(Player, verbose_name="jogador")
    team = models.ForeignKey(Team, verbose_name="clube")
    from_date = models.DateField('de')
    to_date = models.DateField(u'até')


'''
Associação de um jogador com um time concreto
'''
class TeamPlayer(models.Model):
    concrete_team = models.ForeignKey(ConcreteTeam, verbose_name = "equipe")
    player = models.ForeignKey(Player, verbose_name="jogador")
    t_shirt = models.PositiveSmallIntegerField("camisa do jogador", null=True, blank=True)
    substitute = models.BooleanField("reserva", default=False)
    position = models.CharField("posição do jogador", max_length=3, null=True, blank=True)
    #poderia colocar mais dados do jogador aqui, como gols marcados, assistências, cartoes levados. etc...
    
    def __unicode__(self):
        return unicode(self.player)    

    class Meta:
        verbose_name_plural = "Jogadores da equipe"
        verbose_name = "Jogador da equipe"    

'''
Estadio
'''
class Stadium(models.Model):
    full_name = models.CharField("nome completo", max_length=100, null=True, blank=True)
    short_name = models.CharField("nome resumido", max_length=50)
    city = models.ForeignKey(City, verbose_name=_("Cidade"), null=True, blank=True)
    lat = models.DecimalField(max_digits=12, decimal_places=8, verbose_name=_("latitude"), blank=True, null=True)
    lng = models.DecimalField(max_digits=12, decimal_places=8, verbose_name=_("longitude"), blank=True, null=True)

    def __unicode__(self):
        return unicode(self.short_name)
    
    class Meta:
        verbose_name_plural = u"Estádios"
        verbose_name = u"Estádio"

'''
Um árbitro
'''
class Referee(models.Model):
    name = models.CharField("nome", max_length=50)
    country_of_birth = models.ForeignKey(Country, verbose_name=_(u"país de nascimento"), null=True, blank=True)
    date_of_birth = models.DateField('data de nascimento', null=True, blank=True)        
    birth_data = models.CharField("dados não estruturados de nascimento", max_length=30, null=True, blank=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"Árbitros"
        verbose_name = u"Árbitro"


'''
Uma partida
'''    
class Match(models.Model):
    match_date = models.DateField('data da partida', null=True, blank=True)    
    stadium = models.ForeignKey(Stadium, verbose_name=u"estádio", null=True, blank=True)
    referee = models.ForeignKey(Referee, verbose_name=u"árbitro", null=True, blank=True)
    referee_ass1 = models.ForeignKey(Referee, verbose_name=u"árbitro auxiliar 1", null=True, blank=True, related_name="ref_aux1")
    referee_ass2 = models.ForeignKey(Referee, verbose_name=u"árbitro auxiliar 2", null=True, blank=True, related_name="ref_aux2")
    championship = models.ForeignKey(ConcreteChampionship, verbose_name="campeonato")
    championshipPhase = models.ForeignKey(ChampionshipPhase, verbose_name="fase do campeonato", null=True, blank=True)
    phaseGroup = models.ForeignKey(PhaseGroup, verbose_name="grupo", null=True,blank=True)
    round_number = models.PositiveSmallIntegerField("rodada", null=True,blank=True)            
    home_team = models.ForeignKey(ConcreteTeam, verbose_name="mandante", related_name="home_team")
    away_team = models.ForeignKey(ConcreteTeam, verbose_name="visitante")
    home_team_coach = models.ForeignKey(Coach, verbose_name=u"técnico da equipe mandante", related_name="home_team_coach", null=True, blank=True)
    away_team_coach = models.ForeignKey(Coach, verbose_name=u"técnico da equipe visitante", related_name="away_team_coach", null=True, blank=True)
    home_team_goals = models.PositiveSmallIntegerField("Gols da equipe mandante", 
                                                                     default=0, 
                                                                     null = True, 
                                                                     blank=True) 
    away_team_goals = models.PositiveSmallIntegerField("Gols da equipe visitante", 
                                                                     default=0, 
                                                                     null = True, 
                                                                     blank=True)
    home_team_penalty_goals = models.PositiveSmallIntegerField("Gols da equipe mandante na disputa por penalties", 
                                                                     default=0, 
                                                                     null = True, 
                                                                     blank=True) 
    away_team_penalty_goals = models.PositiveSmallIntegerField("Gols da equipe visitante na disputa por penalties", 
                                                                     default=0, 
                                                                     null = True, 
                                                                     blank=True) 
     
    is_complete = models.BooleanField(default=False, verbose_name="ficha completa?")

    public_thread = models.ForeignKey('comments.Thread', related_name="public_thread", verbose_name=_("Thread publica e unica"), blank=True, null=True)
    user_thread = models.ManyToManyField('comments.Thread', related_name="user_thread", verbose_name=_("Thread que cada usuario pode criar"), through='UserThread')

    def fill_players_from_team(self, concrete_team, from_home_team):
        '''
        Preenche os MatchPlayers com os TeamPlayers associados ao ConcreteTeam
        '''
        players_from_home_team = TeamPlayer.objects.filter(concrete_team=concrete_team)            
        
        for team_player in players_from_home_team:
            match_player = MatchPlayer(team=concrete_team, match=self, from_home_team=from_home_team)
            match_player.player = team_player.player
            match_player.substitute = team_player.substitute
            match_player.save()
        

    def fill_players_from_home_team(self):
        '''
        Preenche os jogadores do time mandante
        '''
        self.fill_players_from_team(self.home_team, True)

    def fill_players_from_away_team(self):
        '''
        Preenche os jogadores do time visitante
        '''
        self.fill_players_from_team(self.away_team, False)

    def __unicode__(self):
        result = self.home_team.team.short_name
        
        if self.home_team_goals:
            result += " " + unicode(self.home_team_goals)
            
        result += " X " 
        
        if self.away_team_goals:
            result += unicode(self.away_team_goals) + " " 

        result += self.away_team.team.short_name
        
        #campeonato/temporada            
        if self.championship:
            result += " - " + self.championship.championship.name
        
        if self.championship.season:
            result += " " + unicode(self.championship.season)
            
        #data
        if self.match_date:
            result += " - " + unicode(self.match_date)
                    
        return result

    def save(self, *args, **kwargs):
        if self.public_thread_id is None:
            pub_thread = Thread()
            pub_thread.started_date = datetime.datetime.now()
            pub_thread.save()
            self.public_thread = pub_thread
        super(Match, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Partidas"
        verbose_name = "Partida"    


class UserThread(models.Model):
    match = models.ForeignKey(Match)
    thread = models.ForeignKey(Thread)
    user = models.ForeignKey(get_user_model())


'''
Associação entre jogador e partida
'''
class MatchPlayer(models.Model):
    match = models.ForeignKey(Match, verbose_name="partida")
    player = models.ForeignKey(Player, verbose_name="jogador")
    from_home_team = models.BooleanField(default=True)
    team = models.ForeignKey(ConcreteTeam, verbose_name="equipe")
    t_shirt = models.PositiveSmallIntegerField("camisa do jogador", null=True, blank=True)
    substitute = models.BooleanField("reserva", default=False)    
    first_yellow_card = models.NullBooleanField(u"levou cartão amarelo", null=True, blank=True)
    first_yellow_card_minute = models.PositiveSmallIntegerField(u"minuto do cartão amarelo", null=True, blank=True)
    first_yellow_card_time = models.CharField("tempo do jogo", max_length=3, null=True, blank=True) #1,2,1PR,2PR    
    second_yellow_card = models.NullBooleanField(u"levou segundo cartão amarelo", null=True, blank=True)
    red_card = models.NullBooleanField(u"levou cartão vermelho", null=True, blank=True)
    second_card_or_red_card_minute = models.PositiveSmallIntegerField(u"minuto do segundo cartão ou vermelho direto", null=True, blank=True)
    second_card_or_red_card_time = models.CharField("tempo do jogo", max_length=3, null=True, blank=True) #1,2,1PR,2PR
    
    position = models.CharField("posição do jogador", max_length=3, null=True, blank=True)
        
    def __unicode__(self):
        if self.player:
            return self.player.nick
        else:
            return None
    
    class Meta:
        verbose_name_plural = "Jogadores da partida"
        verbose_name = "jogador da partida"    
            
'''
Gol!
'''
class Goal(models.Model):
    match = models.ForeignKey(Match, verbose_name="partida")    
    scored_by = models.ForeignKey(Player, verbose_name="quem marcou") 
    in_favor_of = models.ForeignKey(ConcreteTeam, verbose_name="a favor de")
    in_favor_of_home_team = models.BooleanField(verbose_name="Da equipe mandante?", default=True)
    auto_gol = models.BooleanField("gol contra", default=False)
    minute = models.PositiveSmallIntegerField("minuto", null=True, blank=True)
    match_time = models.CharField("tempo do jogo", max_length=3, null=True, blank=True) #1,2,1PR,2PR
    

    def __unicode__(self):
        return "Gol de " + self.scored_by.name

    class Meta:
        verbose_name_plural = "Gols"
        verbose_name = "Gol"    

'''
Substituições de um jogo
'''
class MatchSubstitution(models.Model):
    match = models.ForeignKey(Match, verbose_name="jogo")
    from_home_team = models.BooleanField(verbose_name=u"Da equipe mandante?", default=True)
    player_in = models.ForeignKey(Player, verbose_name="quem entrou", related_name="player_in")
    player_out = models.ForeignKey(Player, verbose_name=u"quem saíu", related_name="player_out")
    minute = models.PositiveSmallIntegerField("minuto", null=True, blank=True)
    match_time = models.CharField("tempo do jogo", max_length=3, null=True, blank=True) #1,2,1PR,2PR
    
    class Meta:
        verbose_name_plural = u"Substituições"
        verbose_name = u"Substituição"
        
    def __unicode__(self):
        return u"Saíu " + unicode(self.player_out) + " e entrou " + unicode(self.player_in)

class MatchImporter(models.Model):
    """
    Controle de importações
    """
    filename = models.CharField(u'nome do arquivo', max_length=80, null=True, blank=True)
    start_time = models.DateTimeField(u'hora de início da importação', null=True, blank=True)
    matchs_to_import = models.IntegerField(u'partidas a importar', null=True, blank=True)
    imported_matches = models.IntegerField(u'partidas importadas', null=True, blank=True, default=0)
    imported = models.BooleanField(u'importado ?', default=False)

    def set_imported(self):
        self.imported = True
        self.save()

    def set_not_imported(self):
        self.imported = False
        self.start_time = None
        self.save()
            
    def __unicode__(self):
        if (self.start_time):
            return unicode(self.filename) + u' - Iniciado em ' + unicode(self.start_time) 
        else: 
            return unicode(self.filename) + u' - ' +  unicode(u'Ñ iniciado') 
    
                 
