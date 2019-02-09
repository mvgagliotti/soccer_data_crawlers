# coding=UTF-8
'''
Created on Apr 5, 2014

@author: mvgagliotti
'''
import codecs
import os
import re

from fut_friends import settings
from fut_friends.common import JsonHelper


class ChampDTO:    
    def __init__(self, **kwargs):
        self.season = 0
        self.name = ""
        self.match_count=0
        self.champion=""            
        vars(self).update(kwargs) 
    
    def save_to_file(self):
        '''
        Salva arquivo json do matchDTO
        '''
        json_string = JsonHelper().to_json(self);
        f_name = os.path.join(settings.IMPORTER_PATH, self.name.replace(" ","_") + "_" + unicode(self.season) + '.json')
        match_file = open(f_name,"w")
        match_file.write(json_string)
        match_file.close()

class PersonDTO:
    def __init__(self, **kwargs):
        self.name = ""
        self.birth_data = ""
        vars(self).update(kwargs)
    
    def __unicode__(self):
        return unicode(self.name)
    
    def __str__(self):            
        return unicode(self.name)
    
    

class MatchDTO:
    
    def __init__(self, **kwargs):
        
        self.champ = ""
        self.stadium = ""
        self.city = ""
        self.country = ""
        self.champ_season = ""
        self.champ_phase = ""
        self.champ_group = ""
        self.round = ""
        self.match_date = ""
        self.match_time = ""
        self.link = ""
        self.home_team = ""
        self.away_team = ""
        self.home_team_coach = ""
        self.away_team_coach = ""
        self.home_team_goals = 0
        self.away_team_goals = 0
        self.home_team_penalty_goals = 0
        self.away_team_penalty_goals = 0        
        self.referee = ""
        self.referee_aux1 = ""
        self.referee_aux2 = ""
        self.home_team_players = []
        self.away_team_players = []
        self.home_team_subs = []
        self.away_team_subs = []

        vars(self).update(kwargs)
    
    def match_filename(self):
        
        def season_to_string(season):
            if type(season) == str:
                return season.replace("-","_")
            return unicode(season)
                    
        '''
        Campeonato + Temporada + Data + TimeA + TimeB
        '''
        return self.champ.replace(" ","_") + \
            '_' + season_to_string(self.champ_season) + \
            '_' + self.match_date.replace("/", "_") + \
            '_' + self.home_team.replace(" ", "_") + \
            '_' + self.away_team.replace(" ", "_")
        
    def __unicode__(self):
        '''
        Para debug: ficha do jogo
        '''
        str_result = unicode(self.home_team) + " " + unicode(self.home_team_goals) + " X " + unicode(self.away_team_goals) + " " +  unicode(self.away_team)
        return str_result
    
    def __str__(self):
        return unicode(self)
    
    def save_to_file(self):
        '''
        Salva arquivo json do matchDTO
        '''
        json_string = JsonHelper().to_json(self);
        f_name = os.path.join(settings.IMPORTER_PATH,self.match_filename() + '.json')
#         match_file = open(f_name,"w")
        match_file = codecs.open(f_name, "w", "utf-8-sig")
        match_file.write(json_string)
        match_file.close()


class SubDTO:
    def __init__(self, **kwargs):
        self.p_in = ""
        self.p_out = ""
        self.time = "" 
        
        vars(self).update(kwargs)
    
class PlayerDTO:

    def __init__(self, **kwargs):
        self.name = ""
        self.position = ""
        self.goals = []
        self.first_yellow_card = False
        self.second_yellow_card = False
        self.red_card = False
        self.substitute = False
        self.t_shirt = ""
        
        vars(self).update(kwargs)
    
    def __unicode__(self):
        return self.name

class GoalDTO:
    
    def __init__(self, **kwargs):
        self.time = ""
        self.auto = False
        
        vars(self).update(kwargs) 

class YellowCardDTO:
    
    def __init__(self, **kwargs):
        self.time = ""
        
        vars(self).update(kwargs) 
        
class RedCardDTO:
        
    def __init__(self, **kwargs):
        self.time = ""
    
        vars(self).update(kwargs) 


if __name__ == "__main__":
    a = [1,2]
    try:
        a[3]
    except Exception as e:
        print "does something "
        
        if unicode(e).find("index") > -1:
            raise e
        