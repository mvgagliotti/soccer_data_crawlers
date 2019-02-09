# coding=UTF-8
'''
Created on May 25, 2014

Chamadas para importações das partidas do campeonato brasileiro

@author: mvgagliotti
'''
from matches.models_importer import import_champ, import_match
from matches.models import ConcreteChampionship
from profile.models import Profile
import profile

def doIt():    
    
    print profile.__name__
    
    profile_count = Profile.objects.count()
    print profile_count
    
#     import_champ("Campeonato Brasileiro", 2010, False, 368)    
#     import_champ("Campeonato Brasileiro", 2011, False, 291)
#     import_champ("Campeonato Brasileiro", 2012, False, 197)    
    import_champ("Campeonato Brasileiro", 2009, False)            
    import_champ("Campeonato Brasileiro", 2008, False)            
    import_champ("Campeonato Brasileiro", 2007, False)                
#     br2013 = ConcreteChampionship.objects.filter(championship__name__startswith="Campe")[0]
#     import_match("Campeonato_Brasileiro_2013_31_07_2013_Bahia_Flamengo.json", br2013, False)
    
    
if __name__ == "__main__":
    doIt()
