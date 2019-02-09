# coding=UTF-8
'''
Created on Feb 16, 2014

@author: mvgagliotti
'''
from ajax_select import LookupChannel
from matches.models import ConcreteChampionship, ConcreteTeam, TeamPlayer,\
    Player, Referee, Coach, Stadium, ChampionshipPhase, PhaseGroup
from django.utils.html import escape

class ItalicDisplayLookup(LookupChannel):
    '''
    Classe base para lookups que mostram as coisas em itálico
    '''
    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return u"<div><i>%s</i></div>" % (escape(obj))
    
    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        return u"<div><i>%s</i></div>" % (escape(obj))

    def get_result(self, obj):
        return str(obj)
    

class RefereeLookup(ItalicDisplayLookup):
    model = Referee
    
    def get_query(self, q, request):        
        if len(q) < 3:
            return []
        return Referee.objects.filter(name__istartswith=q)

class CoachLookup(ItalicDisplayLookup):
    model = Coach
    
    def get_query(self, q, request):        
        if len(q) < 3:
            return []
        return Coach.objects.filter(nick__istartswith=q)
        

class PlayerLookup(ItalicDisplayLookup):
    model = Player
    
    def get_query(self, q, request):
        # Se o tamanho for inferior a três pesquiso mick completo, tipo "Jô" 
        if len(q) < 3:
            return Player.objects.filter(nick__iexact=q)

        return Player.objects.filter(nick__istartswith=q)
    
class StadiumLookup(ItalicDisplayLookup):
    model = Stadium
    
    def get_query(self, q, request):
        if len(q) < 3:
            return []
        return Stadium.objects.filter(short_name__istartswith=q)

class TemPlayerLookup(ItalicDisplayLookup):
    
    model = TeamPlayer
    
    def get_query(self, q, request):
        # Se o tamanho for inferior a três pesquiso mick completo, tipo "Jô" 
        if len(q) < 3:
            return TeamPlayer.objects.filter(player__nick__iexact=q)

        return TeamPlayer.objects.filter(player__nick__istartswith=q)
    
    def get_result(self, obj):
        return str(obj)
            
class ConcreteTeamLookup(ItalicDisplayLookup):
    
    model = ConcreteTeam
    
    def get_query(self, q, request):
        #TODO: poderia filtrar aqui pela "temporada corrente"
        
        if len(q) < 3:
            return [] 
         
        return ConcreteTeam.objects.filter(team__short_name__istartswith=q)
    
    def get_result(self, obj):
        return str(obj)
    
    
class ConcreteChampionshipLookup(ItalicDisplayLookup):
    
    model = ConcreteChampionship
    
    def get_query(self, q, request):
        if len(q) < 3:
            return [] 
        
        #TODO: poderia filtrar aqui pela "temporada corrente"         
        return ConcreteChampionship.objects.filter(championship__name__istartswith=q)
    
    def get_result(self, obj):
        return str(obj)
    
class ChampPhaseLookup(ItalicDisplayLookup):
    model = ChampionshipPhase
    
    def get_query(self, q, request):
        if request.GET['id_championship'] == "":
            return []
        
        if len(q) < 1: 
            return []
        
        return ChampionshipPhase.objects.filter(name__istartswith=q) \
                                        .filter(championship__id=request.GET['id_championship'])
    
class PhaseGroupLookup(ItalicDisplayLookup):
    model = PhaseGroup
    
    def get_query(self, q, request):
        
        champ_phase_key = 'id_championshipPhase'        
        if not(champ_phase_key in request.GET) or request.GET[champ_phase_key] == "":
            return []
        
        if len(q) < 1:
            return []
        
        return PhaseGroup.objects.filter(name__istartswith=q) \
                                 .filter(phase__id=request.GET[champ_phase_key])