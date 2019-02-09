# coding=UTF-8
'''
Created on May 25, 2014

Chamadas para importações das copas

@author: mvgagliotti
'''
from matches.models_importer import import_champ
def doIt():    
    
#     import_champ(champ_name="Copa do Mundo", champ_season=2010)
    import_champ(champ_name="Copa do Mundo", champ_season=2006, skip=15)
    import_champ(champ_name="Copa do Mundo", champ_season=2002)
    import_champ(champ_name="Copa do Mundo", champ_season=1998)
    import_champ(champ_name="Copa do Mundo", champ_season=1994)
    import_champ(champ_name="Copa do Mundo", champ_season=1990)
    import_champ(champ_name="Copa do Mundo", champ_season=1986)
    import_champ(champ_name="Copa do Mundo", champ_season=1982)
    import_champ(champ_name="Copa do Mundo", champ_season=1978)
#     import_champ(champ_name="Copa do Mundo", champ_season=1974)
    import_champ(champ_name="Copa do Mundo", champ_season=1970)
    import_champ(champ_name="Copa do Mundo", champ_season=1966)
    import_champ(champ_name="Copa do Mundo", champ_season=1962)
    import_champ(champ_name="Copa do Mundo", champ_season=1958)
    import_champ(champ_name="Copa do Mundo", champ_season=1954)
    import_champ(champ_name="Copa do Mundo", champ_season=1950)
    import_champ(champ_name="Copa do Mundo", champ_season=1938)
    import_champ(champ_name="Copa do Mundo", champ_season=1934)
    import_champ(champ_name="Copa do Mundo", champ_season=1930)
    
if __name__ == "__main__":
    doIt()
