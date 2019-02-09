# coding=UTF-8
'''
Created on Apr 10, 2014

@author: mvgagliotti
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from matches.models_dtos import MatchDTO, SubDTO, PlayerDTO,\
    GoalDTO, YellowCardDTO, RedCardDTO, ChampDTO, PersonDTO
from symbol import except_clause
from matches.js_futpedia_crawler_utils import get_home_team_goal_data,\
    get_home_team_sub, get_away_team_sub, get_away_team_goal_data,\
    get_away_team_yellow_card, get_home_team_yellow_card, get_home_team_red_card,\
    get_away_team_red_card
import json
import os
import inspect
from fut_friends.common import JsonHelper
import re
from matches.models_importer import save_zip_file
from fut_friends import settings

def dotIt():
    
#    scan_champ('Taça Libertadores', '2013', 'http://futpedia.globo.com/campeonato/taca-libertadores/2013', 10)

#     champ_2006 = \
#         scan_champ_first_phase("Copa do Mundo", 2006, "http://futpedia.globo.com/campeonato/copa-do-mundo/2006#/fase=copa2006-primeira-fase")
#     scan_champ_final_phase(champ_2006, "http://futpedia.globo.com/campeonato/copa-do-mundo/2006#/fase=copa2006-oitavas")
# 
#      
#     champ_2010 = \
#         scan_champ_first_phase("Copa do Mundo", 2010, "http://futpedia.globo.com/campeonato/copa-do-mundo/2010#/fase=primeira-fase")
#     scan_champ_final_phase(champ_2010, "http://futpedia.globo.com/campeonato/copa-do-mundo/2010#/fase=oitavas-de-final")
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2013, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2013-2013", 38)

    '''
    *************************************Copas do mundos****************************************************
    '''

    
    #champ_1930 = scan_champ_first_phase("Copa do Mundo", 1930, "http://futpedia.globo.com/campeonato/copa-do-mundo/1930#/fase=primeira-fase")
    #scan_champ_final_phase(champ_1930, "http://futpedia.globo.com/campeonato/copa-do-mundo/1930#/fase=final")
    
#     scan_champ("Copa do Mundo", 1934, "http://futpedia.globo.com/campeonato/copa-do-mundo/1934", 2, 1)
#     scan_champ("Copa do Mundo", 1938, "http://futpedia.globo.com/campeonato/copa-do-mundo/1938", 2, 1)
#     scan_champ("Copa do Mundo", 1950, "http://futpedia.globo.com/campeonato/copa-do-mundo/1950", 2, 1)
#     scan_champ("Copa do Mundo", 1954, "http://futpedia.globo.com/campeonato/copa-do-mundo/1954", 2, 1)
#     scan_champ("Copa do Mundo", 1958, "http://futpedia.globo.com/campeonato/copa-do-mundo/1958", 3, 1)
#     scan_champ("Copa do Mundo", 1962, "http://futpedia.globo.com/campeonato/copa-do-mundo/1962", 3, 1)

#    scan_champ("Copa do Mundo", 1994, "http://futpedia.globo.com/campeonato/copa-do-mundo/1994", 4)
    

    scan_champ_pontos_corridos("Campeonato Brasileiro", 2013, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2013-2013", 38)


def get_page_failsafely(driver, url, attempts=3):
    '''
    Dispara a request novamente em 30 segungos, n vezes até desistir
    '''
    
    driver.set_page_load_timeout(30)

    while True:
        try:
            driver.get(url)
        except Exception as e:
            attempts = attempts -1
            if attempts == 0:
                raise e
            else:
                continue
        break    
        

def get_by_xpath(element, xpath):
    '''
    Obtém o text elemento recuperado a partir de um find_element_by_xpath em element.
    Caso não encontre, retorna ""    
    '''
    try:
        return element.find_element_by_xpath(xpath).text
    except:
        return ""

def scan_champ_pontos_corridos(champ_name, season, url, rounds, start_round=1, skip_saving=False, champ=None):
    '''
    Campeonato de pontos corridos
    '''
    driver = webdriver.Firefox()
    driver.get(url)

    match_driver = webdriver.Firefox() #driver para página do jogo

    '''
    Campeão
    '''
    champion = driver.find_element_by_xpath("//div[@class='nome-campeao top7']/a[1]").text
    
    match_count = 0;
    for round_index in range(rounds+1)[start_round:]:
        lis = driver.find_elements_by_xpath("//li[@class='lista-classificacao-jogo'][@data-rodada='%d']" % (round_index))
        for li in lis:
            link = li.find_element_by_xpath(".//link[@itemprop='url']").get_attribute('href')
            print "Rodada %d: Link sendo escaneado: %s" % (round_index, link)
            match_count = match_count + 1
            scanned_match = scan_champ_match(match_driver, link)
            if scanned_match == None:
                continue
            
            scanned_match.champ = champ_name
            scanned_match.champ_season = season
            '''
            Salvando arquivo
            '''
            scanned_match.save_to_file()

    if champ == None:
        champ = ChampDTO()    
    champ.name = champ_name
    champ.season = season
    champ.match_count = match_count
    champ.champion = champion
    
    if not skip_saving:

        champ.save_to_file()
    
    
        '''
        Salvando ZIP com arquivos
        '''
        save_zip_file(settings.IMPORTER_PATH, champ_name, season)
    
    '''
    Fechando
    '''
    driver.close()
    match_driver.close()                
    
    return champ    

def scan_champ_first_phase(champ_name, season, url):
    '''
    Jogos da primeira fase: 
    retorna o campeonato, que deve ser passado pro método scan_champ_final_phase
    '''
    driver = webdriver.Firefox()
    driver.get(url)

    match_driver = webdriver.Firefox() #driver para página do jogo 

    '''
    Obtendo links p/ jogos
    '''
    lis = driver.find_elements_by_xpath("//li[@class='lista-classificacao-jogo']")
    links = [li.find_element_by_xpath(".//link").get_attribute("href") for li in lis] 
            
    '''
    Algumas páginas estão com formato diferente: jogos vêm (também) em tabela-jogos
    '''
    tables_with_matches = driver.find_elements_by_xpath('//*[@id="tabela-jogos"]')
    for table in tables_with_matches:
        links = [anchor.get_attribute("href") for anchor in table.find_elements_by_xpath('.//a')] + links
        
    '''
    Campeão
    '''
    champion = driver.find_element_by_xpath("//div[@class='nome-campeao top7']/a[1]").text
    
    match_count=0          
    for link in links:
                
        print "link sendo scaneado: %s" % (link)        
        scanned_match = scan_champ_match(match_driver, link)
        if scanned_match == None:
            continue
        
        scanned_match.champ = champ_name
        scanned_match.champ_season = season
        '''
        Salvando arquivo
        '''
        scanned_match.save_to_file()
        match_count=match_count+1
        print "%d Jogos scaneados " % (match_count)
    
    '''
    Fechando
    '''
    driver.close()
    match_driver.close()                
        
    champ = ChampDTO(name=champ_name, season=season, match_count=match_count, champion=champion)
    return champ
    

def scan_champ_final_phase(champ, url, skip_saving=False):
    '''
    Jogos no formato "mata-mata"
    '''
    driver = webdriver.Firefox()
    driver.get(url)
    
    match_driver = webdriver.Firefox() #driver para página do jogo 
                
    anchors1 = driver.find_elements_by_xpath("//div[@class='jogo_ida dados']/a[1]")
    anchors2 = driver.find_elements_by_xpath("//div[@class='jogo_volta dados']/a[1]")
    anchors = anchors1 + anchors2
    
    links = map(lambda anchor: anchor.get_attribute('href'), anchors)
    
    match_count=champ.match_count        
    for link in links:
        print "link sendo scaneado: %s" % (link)        
        scanned_match = scan_champ_match(match_driver, link)
        if scanned_match == None:
            continue
        
        scanned_match.champ = champ.name
        scanned_match.champ_season = champ.season
        '''
        Salvando arquivo
        '''
        scanned_match.save_to_file()
        match_count=match_count+1
        print "%d Jogos scaneados " % (match_count)
    
    '''
    Salvando dados do campeonato
    '''
    champ.match_count = match_count
    if not skip_saving:
        champ.save_to_file()
        
        '''
        Salvando ZIP com arquivos
        '''
        save_zip_file(settings.IMPORTER_PATH, champ.name, champ.season)
        
    
    '''
    Fechando
    '''
    driver.close()
    match_driver.close()                
    
    if skip_saving:
        return champ
             

def scan_champ(champ_name, season, url, page_count, ini_page=1):
    '''
    Página com jogos no formato em listagem paginada
    '''
    driver = webdriver.Firefox()
    driver.get(url)
    
    match_driver = webdriver.Firefox() #driver para página do jogo 

    '''
    Campeão
    '''
    champion = driver.find_element_by_xpath("//div[@class='nome-campeao top7']/a[1]").text
    
    '''
    Obtém os links de jogos da página do campeonato e acessa os jogos
    '''
    match_count=0
    for i in range(page_count):
        
        page = i+1; 
        if page < ini_page:
            continue;
        
        print "****************PÁGINA %d*******************" % page
                        
        '''
        div com jogos: lista-jogos
        '''
        div_matches = driver.find_elements_by_class_name('lista-jogos')[0]                
        anchors = div_matches.find_elements_by_xpath(".//a[not(@class)]") #links , exceto previous e next       
        links = map(lambda anchor: anchor.get_attribute('href'), anchors)
        
        for link in links:
            
            '''
            Scaneando a página do jogo
            '''
            print "Scaneando página %d link: %s" % (page, link)            
            scanned_match = scan_champ_match(match_driver, link)
            if scanned_match == None:
                continue
            
            
            scanned_match.champ = champ_name
            scanned_match.champ_season = season                    
            
            print scanned_match
                        
            '''
            Salvando arquivo
            '''
            scanned_match.save_to_file()
            
            match_count = match_count+1
            print "%d Jogos scaneados " % (match_count)
                                
        '''
        obtendo link para próxima página
        '''
        np = driver.find_elements_by_class_name('next_page')[0]
        np.click()
    
    '''
    Salvando dados do campeonato
    '''
    champ = ChampDTO(name=champ_name, season=season, match_count=match_count, champion=champion)
    champ.save_to_file()
    
    '''
    Salvando ZIP com arquivos
    '''
    save_zip_file(settings.IMPORTER_PATH, champ_name, season)
    
    '''
    Fechando
    '''
    driver.close()
    match_driver.close()                

def scan_champ_match(match_driver, link):
    '''
    Acessa a página do jogo e obtém os dados
    '''
    get_page_failsafely(match_driver, link)    

    match = MatchDTO()
    
    '''
    Árbitro
    '''
    ref_head_divs = match_driver.find_elements_by_xpath("//div[@rel='publico-renda-arbitragem']")
    if len(ref_head_divs) > 0:
        ref_head_div = ref_head_divs[0] 
        ref_head_div.click();
        
        ref_div = match_driver.find_elements_by_xpath("//div[@class='arbitragem']")
        if len(ref_div) > 0:
            '''
            Árbitro principal
            '''
            ref_div = ref_div[0]
            ref_name = get_by_xpath(ref_div,".//span[@class='nome-juiz']")
            birth_data = get_by_xpath(ref_div, ".//span[@class='data-nascimento']")
            if ref_name != "":
                match.referee = PersonDTO(name=ref_name, birth_data=birth_data)
            
            '''
            Auxiliares
            ''' 
            aux_lis = ref_div.find_elements_by_xpath(".//ul[@class='auxiliares']/li")
            if len(aux_lis) > 0:
                referee_aux1 = aux_lis[0].text
                if referee_aux1.find('-') > -1:
                    match.referee_aux1 = PersonDTO(name=referee_aux1.split('-')[0], birth_data=referee_aux1.split('-')[1])
                else:
                    match.referee_aux1 = PersonDTO(name=referee_aux1)
                
                if len(aux_lis) > 1:
                    referee_aux2 = aux_lis[1].text
                    if referee_aux2.find('-') > -1:
                        match.referee_aux2 = PersonDTO(name=referee_aux2.split('-')[0], birth_data=referee_aux2.split('-')[1])
                    else:
                        match.referee_aux2 = PersonDTO(name=referee_aux2)
                                        
                     
    '''
    Obtendo dados do grupo e fase e rodada e processar esta porra
    Copa do Mundo 2010, Primeira fase (Grupo A) - 3ª rodada
    '''
    try:
        group_phase_round_data = match_driver.find_element_by_xpath("//a[@class='link-campeonato']").text
    except:
        print "Página %s não contém dados de jogo" % link
        return None
        
    
    def get_phase_group_and_round(group_phase_round_data):
        phase_str = ""
        if group_phase_round_data.find(',') > -1:
            phase_str = group_phase_round_data.split(',')[1]
            
            '''
            Em alguns caso, estranhamente a informação de grupo/fase/rodada eh exatamente igual a do campeonato
            '''
            if group_phase_round_data.split(',')[1].strip() == group_phase_round_data.split(',')[0].strip():
                return ("","","") 
            
        
        _phase = ""
        _round = ""
        _group = ""
        
        '''
        Grupo        
        '''                
        pattern = re.compile('\((.*)\)')
        '''
        PAU: 
        url: http://futpedia.globo.com/campeonato/copa-do-mundo/1966/07/13/franca-1-x-1-mexico
        erro: UnboundLocalError: local variable 'phase_str' referenced before assignment
        '''
        re_match = pattern.search(phase_str)
        if re_match:
            _group = re_match.group(1)
            _phase = phase_str[:phase_str.find('(')] 
        
        '''
        Checando se tem "-": neste caso deve ter rodada
        '''
        if phase_str.find('-') > -1:
            splitted = phase_str.split('-')
            if len(splitted) > 1:
                _round = splitted[1]
                round_match = re.compile('\d+').search(_round)
                if round_match: 
                    _round = round_match.group(0)
                
            if (_phase == ""):
                _phase = splitted[0] 
        
        if _phase == "":
            _phase = phase_str
        
        return (_phase.strip(), _group.strip(), _round.strip())
    
    match.champ_phase, match.champ_group, match.round = \
        get_phase_group_and_round(group_phase_round_data)        
    
    '''
    Definindo function auxiliar para extrair tempos de gols/cartões/substituições
    Retorna tupla com minuto e tempo (1o ou 2o)
    '''
    def get_time(data):
        if data == None or data == "":
            return ""
        pattern = re.compile('\\d+')
        
        minute = ""
        match_time = ""
        
        minute_match = pattern.search(data.split('/')[0]);
        if minute_match:
            minute = minute_match.group() 
        
        match_time_match = pattern.search(data.split('/')[1])
        if match_time_match:
            match_time = match_time_match.group()
        
        return minute  + '_' + match_time  
    
    '''
    Obtendo nome dos times e placar
    '''    
    try:
        match.home_team = match_driver.find_element_by_xpath("//a[@class='info-time mandante_text']/span[1]").text  
    except:
        print "Página %s não contém dados de jogo" % link
        return match
    
    match.away_team = match_driver.find_element_by_xpath("//a[@class='info-time visitante_text']/span[1]").text  
    match.home_team_goals = match_driver.find_element_by_xpath("//span[@class='placar-mandante font-face']").text
    match.away_team_goals = match_driver.find_element_by_xpath("//span[@class='placar-visitante font-face']").text
    
    '''
    Placar de penalties
    '''
    penalty_divs = match_driver.find_elements_by_xpath("//div[@class='penaltis']")
    if penalty_divs:
       p_result = penalty_divs[0].find_element_by_xpath(".//div[@class='resultado']").text
       match.home_team_penalty_goals = p_result.split('-')[0] 
       match.away_team_penalty_goals = p_result.split('-')[1]
        
    '''
    Data/Hora do Jogo/Estádio/Cidade/País
    Quarta, 17/07/2013 - 21h50, Defensores del Chaco - Assunção, Paraguai 
    '''
    place_data = match_driver.find_element_by_xpath("//div[@class='dados-localizacao']").text
    place_data_parts = place_data.split(',')
    
    '''
    Data/Hora
    '''
    if len(place_data_parts) > 1:    
        if place_data_parts[1].find("-") >-1:
            match.match_date = place_data_parts[1].split('-')[0].strip() 
            match.match_time = place_data_parts[1].split('-')[1].strip() 
        else:
            match.match_date = place_data_parts[1].strip()
    
        if len(place_data_parts) > 2 and place_data_parts[2].find("-") >-1:        
            '''
            Estádio
            '''
            match.stadium = place_data_parts[2].split('-')[0].strip()     
            
            '''
            Cidade/País
            '''
            match.city = place_data_parts[2].split('-')[1].strip()
        else:
            if len(place_data_parts) > 2:
                match.stadium = place_data_parts[2]     
        
    '''
    deu pau aqui: 
    http://futpedia.globo.com/campeonato/campeonato-brasileiro/2013/09/10/internacional-1-x-2-santos
    '''
    if len(place_data_parts) > 3:
        match.country = place_data_parts[3].strip()
    
    '''            
    ************************ Visitante ***********************
    '''
    try:
        div_away_team = match_driver.find_element_by_id("escalacao-visitante")
    except:
        print "o jogo do link %s não possui ficha técnica completa" % link
        return match
    
    '''
    Técnico time visitante
    '''
    try: 
        at_span_coach = div_away_team.find_element_by_xpath(".//span[@itemtype='http://schema.org/Person/Coach']/span[2]")
        match.away_team_coach = at_span_coach.text
    except:
        pass 
    
    '''
    Jogadores do time visitante
    '''
    players_lis = div_away_team.find_elements_by_xpath(".//li[@itemtype='http://schema.org/Person/SoccerPlayer']")
    sub_player = None #controle de substituição
    li_index=0
    for player_li in players_lis:
        
        li_index = li_index+1 
        
        '''
        Obtendo nome e posição e adicionando na lista
        '''
        p_name = player_li.find_element_by_xpath(".//span[@itemprop='name']").text
        p_pos = player_li.find_element_by_xpath(".//span[@class='posicao']").text
        player = PlayerDTO(name=p_name, position=p_pos)
        match.away_team_players.append(player)
        
        '''
        Checando cartões
        '''
        
        '''
        Amarelos
        '''
        yellow_cards_divs = player_li.find_elements_by_xpath(".//div[@class='cartao-amarelo']")
        
        card_index = 1
        for y_card_div in yellow_cards_divs:                    
            _time = get_away_team_yellow_card(match_driver, li_index, card_index)
            _time = get_time(_time)
            y_card = YellowCardDTO(time=_time)
            
            if card_index == 1:
                player.first_yellow_card = y_card
            else:
                player.second_yellow_card = y_card
                                
            card_index = card_index +1;
        
        '''
        Vermelhos
        '''
        red_cards_divs = player_li.find_elements_by_xpath(".//div[@class='cartao-vermelho']")
        for r_card_div in red_cards_divs:                    
            _time = get_away_team_red_card(match_driver, li_index, 1)
            _time = get_time(_time)
            r_card = RedCardDTO(time=_time)
            player.red_card = r_card
        
        '''
        Checando subsituição
        '''
        if (sub_player):
            
            '''
            obtendo minuto/tempo da substituição
            '''
            _time = get_away_team_sub(match_driver, li_index)
            _time = get_time(_time)
            sub = SubDTO(p_in=player, p_out=sub_player, time=_time)
            match.away_team_subs.append(sub)
            player.substitute = True
            
            sub_player = None
        
        if len(player_li.find_elements_by_xpath(".//div[@class='saiu']")) > 0:
                
             sub_player = player
                                        
        '''
        Checando gols a favor
        '''
        goals_divs = player_li.find_elements_by_xpath(".//div[@class='gol']")
        goal_index=1                                     
        for goal_div in goals_divs:
            '''
            obtendo minuto/tempo do gol e adicionando à lista do jogador
            '''
            goal_data = get_away_team_goal_data(match_driver, li_index, goal_index)
            goal_data = get_time(goal_data)
            goal = GoalDTO(time=goal_data)                                        
            player.goals.append(goal)
            
            goal_index = goal_index+1 
            
        '''
        Checando gols contra
        ''' 
        auto_goals_divs = player_li.find_elements_by_xpath(".//div[@class='gol-contra']")
        goal_index=1                                     
        for goal_div in auto_goals_divs:
            '''
            obtendo minuto/tempo do gol e adicionando à lista do jogador
            '''
            goal_data = get_away_team_goal_data(match_driver, li_index, goal_index, True)
            goal_data = get_time(goal_data)
            goal = GoalDTO(time=goal_data, auto=True)                                        
            player.goals.append(goal)
            
            goal_index = goal_index+1 

    
    
    '''
    ************************ Mandante ***********************
    '''
    try:
        div_home_team = match_driver.find_element_by_id("escalacao-mandante")
    except:
        print "o jogo do link %s não possui ficha técnica completa" % link
        return match
    
    '''
    Técnico time mandante
    '''
    try: 
        ht_span_coach = div_home_team.find_element_by_xpath(".//span[@itemtype='http://schema.org/Person/Coach']/span[2]")
        match.home_team_coach = ht_span_coach.text
    except:
        pass
             
    '''
    Jogadores do time mandante
    '''
    players_lis = div_home_team.find_elements_by_xpath(".//li[@itemtype='http://schema.org/Person/SoccerPlayer']")
    sub_player = None #controle de substituição
    li_index=0
    for player_li in players_lis:
        
        li_index = li_index+1 
        
        '''
        Obtendo nome, posição e camisa e adicionando na lista
        '''
        p_name = player_li.find_element_by_xpath(".//span[@itemprop='name']").text
        p_pos = player_li.find_element_by_xpath(".//span[@class='posicao']").text
        player = PlayerDTO(name=p_name, position=p_pos)
        match.home_team_players.append(player)
        
        '''
        Checando cartões
        '''
        
        '''
        Amarelos
        '''
        yellow_cards_divs = player_li.find_elements_by_xpath(".//div[@class='cartao-amarelo']")
        
        card_index = 1
        for y_card_div in yellow_cards_divs:                    
            _time = get_home_team_yellow_card(match_driver, li_index, card_index)
            _time = get_time(_time)
            y_card = YellowCardDTO(time=_time)
            
            if card_index == 1:
                player.first_yellow_card = y_card
            else:
                player.second_yellow_card = y_card
                                
            card_index = card_index +1;

        '''
        Vemelhos
        '''
        red_cards_divs = player_li.find_elements_by_xpath(".//div[@class='cartao-vermelho']")
        for r_card_div in red_cards_divs:                    
            _time = get_home_team_red_card(match_driver, li_index, 1)
            _time = get_time(_time)
            r_card = RedCardDTO(time=_time)
            player.red_card = r_card
        
        '''
        Checando subsituição
        '''
        if (sub_player):
            
            '''
            obtendo minuto/tempo da substituição
            '''
            _time = get_home_team_sub(match_driver, li_index)
            _time = get_time(_time)
            sub = SubDTO(p_in=player, p_out=sub_player, time=_time)
            match.home_team_subs.append(sub)
            player.substitute = True
            
            sub_player = None
        
        if len(player_li.find_elements_by_xpath(".//div[@class='saiu']")) > 0:
                
             sub_player = player
                                        
        '''
        Checando gols a favor
        '''
        goals_divs = player_li.find_elements_by_xpath(".//div[@class='gol']")
        goal_index=1                                     
        for goal_div in goals_divs:
            '''
            obtendo minuto/tempo do gol e adicionando à lista do jogador
            '''
            goal_data = get_home_team_goal_data(match_driver, li_index, goal_index)
            goal_data = get_time(goal_data)
            goal = GoalDTO(time=goal_data)                                        
            player.goals.append(goal)
            
            goal_index = goal_index+1 
            
        '''
        Checando gols contra
        ''' 
        auto_goals_divs = player_li.find_elements_by_xpath(".//div[@class='gol-contra']")
        goal_index=1                                     
        for goal_div in auto_goals_divs:
            '''
            obtendo minuto/tempo do gol e adicionando à lista do jogador
            '''
            goal_data = get_home_team_goal_data(match_driver, li_index, goal_index, True)
            goal_data = get_time(goal_data)
            goal = GoalDTO(time=goal_data, auto=True)                                        
            player.goals.append(goal)
            
            goal_index = goal_index+1 
                                                                
    
    return match 
    
    
        
if __name__ == "__main__":
    dotIt()