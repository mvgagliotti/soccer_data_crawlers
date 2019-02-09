# coding=UTF-8
'''
Created on Apr 5, 2014

@author: mvgagliotti
'''
from bs4 import BeautifulSoup
import urllib2
import os
from matches.models_dtos import MatchDTO, PlayerDTO, SubDTO

def doIt():
    
    #campeonato brasileiro 20013
#    brasil_2013 = 'http://futpedia.globo.com/campeonato/campeonato-brasileiro/2013-2013#/fase=fase-unica'        
#    scan_matches(brasil_2013, 'br_2013')
    #campeonato brasileiro 20013
    
    brasil_2012 = 'http://futpedia.globo.com/campeonato/campeonato-brasileiro/2012'        
    scan_matches(brasil_2012, 'br_2012')            

'''
 ****************************************Métodos de extração de conteúdo************************************
'''
def scan_matches(url, champ_alias_for_file_name):
    '''
    Varre os jogos de um campeonato
    '''
    html = open_champ(url, champ_alias_for_file_name)            
    soup = BeautifulSoup(html)    

    '''
    Iterando nas rodadas e obtendo os jogos!
    '''    
    for i in range(38):        
        
        _round = i+1;
        
        print "*********rodada %d ***********" % _round
        
        '''
        Obtém os LIs dos jogos da rodada X
        '''
        lis = soup.findAll("li", {"class" : "lista-classificacao-jogo", "data-rodada" : _round})
        
        matches_list = get_matches_from_round(lis)
        
        for match in matches_list:
            print unicode(match)
    
                    
def get_matches_from_round(list_items):
    '''
    Dada uma lista de LI, extrai os jogos em cada LI
    '''
    #obtendo os links para os jogos    
    #def get_link(li): return li.link
    #links = map(get_link, lis)
    
    result = []
    
    #obtendo dados dos jogos
    for li in list_items:
        
        #obtendo o time mandante
        div_team = li.find_all('div', {"class" : "time mandante"})[0]
        home_team_str = div_team.meta['content']
        
        #obtendo o time visitante
        div_away_team = li.find_all('div', {"class" : "time visitante"})[0]
        away_team_str = div_away_team.meta['content']
        
        '''
        Coloca no domain MatchDTO
        '''
        match = MatchDTO(home_team=home_team_str, 
                             away_team=away_team_str, 
                             link=li.link['href'])
        
        result.append(match)
        
        '''
        Abrindo a página do jogo e coletando dados: 
        '''
        match_html = urllib2.urlopen(match.link).read()
        print 'Página do jogo aberta com sucesso!'
        match_soup = BeautifulSoup(match_html)
        
        '''
        Mandante
        '''
        div_home_team = match_soup.find_all('div', {'id':'escalacao-mandante'})[0]        
        get_home_team_data(div_home_team, match)
        
        '''
        Visitante
        '''        
        div_away_team = match_soup.find_all('div', {'id':'escalacao-visitante'})[0]        
        get_away_team_data(div_away_team, match)
                    
    return result 


def get_home_team_data(div_team, match):
        '''
        Obtém os dados do time no jogo
        '''
        #técnico
        div_coach = div_team.find_all('span', {'itemtype':'http://schema.org/Person/Coach'})[0]
        match.home_team_coach = div_coach.find_all('span', {'itemprop':'name'})[0].text
        
        #jogadores
        lis_players = div_team.find_all('li', {'itemtype':'http://schema.org/Person/SoccerPlayer'})
        before_p = None
        for li_p in lis_players:
            
                        
            p_name = li_p.p.find_all('span', {'itemprop':'name'})[0].text
            p_position = li_p.p.find_all('span', {'class':'posicao'})[0].text            
            player = PlayerDTO(name=p_name, position=p_position)
            match.home_team_players.append(player)
            
            #definindo se fez gol(s)
            div_goals = li_p.find_all('div', {'class':'gol'})
            for div_goal in div_goals:
                div_goal_info = div_goal.find('div', {'class':'content'})
                player.goals.append(div_goal_info.text)
                         
            #definindo se levou cartões: TODO:
            div_y_card = li_p.find('div', {'class':'cartao-amarelo'})            
            player.first_yellow_card = not (div_y_card == None)
            
            div_r_card = li_p.find('div', {'class':'cartao-vermelho'})
            player.red_card = not (div_r_card == None)
           
            if (before_p): #se guardou o anterior eh pq foi substituído
                sub = SubDTO(p_in=before_p, p_out=player)
                match.home_team_subs.append(sub)
                before_p = None
                
            #subs
            if 'class' in li_p.attrs and li_p.attrs['class'][0] == "sem-linha": 
                before_p = player
    
def get_away_team_data(div_team, match):
        '''
        Obtém os dados do time visitante no jogo
        '''
        #técnico
        div_coach = div_team.find_all('span', {'itemtype':'http://schema.org/Person/Coach'})[0]
        match.away_team_coach = div_coach.find_all('span', {'itemprop':'name'})[0].text
        
        #jogadores
        lis_players = div_team.find_all('li', {'itemtype':'http://schema.org/Person/SoccerPlayer'})
        before_p = None
        for li_p in lis_players:
            
            '''
            testa se houve substituição:
            '''
                        
            p_name = li_p.p.find_all('span', {'itemprop':'name'})[0].text
            p_position = li_p.p.find_all('span', {'class':'posicao'})[0].text            
            player = PlayerDTO(name=p_name, position=p_position)
            match.away_team_players.append(player)
            
            #definindo se fez gol(s)
            div_goals = li_p.find_all('div', {'class':'gol'})
            for div_goal in div_goals:
                div_goal_info = div_goal.find('div', {'class':'content'})
                player.goals.append(div_goal_info.text)
                         
            #definindo se levou cartões: TODO:
            div_y_card = li_p.find('div', {'class':'cartao-amarelo'})            
            player.first_yellow_card = not (div_y_card == None)
            
            div_r_card = li_p.find('div', {'class':'cartao-vermelho'})
            player.red_card = not (div_r_card == None)
           
            if (before_p): #se guardou o anterior eh pq foi substituído
                sub = SubDTO(p_in=before_p, p_out=player)
                match.away_team_subs.append(sub)
                before_p = None
                
            #subs
            if 'class' in li_p.attrs and li_p.attrs['class'][0] == "sem-linha": 
                before_p = player

def open_champ(champ_url, champ_alias_for_file_name):
    '''
    Abre um campeonato: na teoria, vem todos os jogos no html
    '''
    
    file_path = os.path.expanduser('~')+'/' + champ_alias_for_file_name + '.html'
    html = ""
    
    if not os.path.isfile(file_path):
        html = urllib2.urlopen(champ_url).read()
        
        _file = open(file_path,"w")
        _file.write(html)
        _file.close()
    
    html_file = open(file_path)
    html = html_file.read()
    
    return html
    
if __name__ == "__main__":
    doIt()