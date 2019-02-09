# coding=UTF-8
'''
Created on May 25, 2014

@author: mvgagliotti

Chamadas para obter dados das copas do mundo

'''
from matches.crawler_selenium import scan_champ, scan_champ_first_phase,\
    scan_champ_final_phase

def doIt():
    '''
    *************************************Copas do mundos****************************************************
    '''
#     champ_1930 = scan_champ_first_phase("Copa do Mundo", 1930, "http://futpedia.globo.com/campeonato/copa-do-mundo/1930#/fase=primeira-fase")
#     scan_champ_final_phase(champ_1930, "http://futpedia.globo.com/campeonato/copa-do-mundo/1930#/fase=final")
#     
#     scan_champ("Copa do Mundo", 1934, "http://futpedia.globo.com/campeonato/copa-do-mundo/1934", 2, 1) #page_count, ini_page
#     scan_champ("Copa do Mundo", 1938, "http://futpedia.globo.com/campeonato/copa-do-mundo/1938", 2, 1) #page_count, ini_page
#     scan_champ("Copa do Mundo", 1950, "http://futpedia.globo.com/campeonato/copa-do-mundo/1950", 2, 1) #page_count, ini_page
#     scan_champ("Copa do Mundo", 1954, "http://futpedia.globo.com/campeonato/copa-do-mundo/1954", 2, 1) #page_count, ini_page
#     scan_champ("Copa do Mundo", 1958, "http://futpedia.globo.com/campeonato/copa-do-mundo/1958", 3, 1) #page_count, ini_page
#     scan_champ("Copa do Mundo", 1962, "http://futpedia.globo.com/campeonato/copa-do-mundo/1962", 3, 1) #page_count, ini_page

    champ_1966 = scan_champ_first_phase("Copa do Mundo", 1966, "http://futpedia.globo.com/campeonato/copa-do-mundo/1966#/fase=primeira-fase")
    scan_champ_final_phase(champ_1966, "http://futpedia.globo.com/campeonato/copa-do-mundo/1966#/fase=quartas-de-final")
  
    champ_1970 = scan_champ_first_phase("Copa do Mundo", 1970, "http://futpedia.globo.com/campeonato/copa-do-mundo/1970#/fase=primeira-fase")
    scan_champ_final_phase(champ_1970, "http://futpedia.globo.com/campeonato/copa-do-mundo/1970#/fase=quartas-de-final")
    
    #TODO: Copa de 1974 em formato diferente
    
    scan_champ("Copa do Mundo", 1978, "http://futpedia.globo.com/campeonato/copa-do-mundo/1978", 3, 1) #page_count, ini_page
    scan_champ("Copa do Mundo", 1982, "http://futpedia.globo.com/campeonato/copa-do-mundo/1982", 4, 1) #page_count, ini_page
    
    scan_champ("Copa do Mundo", 1986, "http://futpedia.globo.com/campeonato/copa-do-mundo/1986", 4, 1) #page_count, ini_page
    scan_champ("Copa do Mundo", 1990, "http://futpedia.globo.com/campeonato/copa-do-mundo/1990", 4, 1) #page_count, ini_page
      
    scan_champ("Copa do Mundo", 1994, "http://futpedia.globo.com/campeonato/copa-do-mundo/1994", 4)
    scan_champ("Copa do Mundo", 1998, "http://futpedia.globo.com/campeonato/copa-do-mundo/1998", 5)
    scan_champ("Copa do Mundo", 2002, "http://futpedia.globo.com/campeonato/copa-do-mundo/2002", 5)
    
    champ_2006 = scan_champ_first_phase("Copa do Mundo", 2006, "http://futpedia.globo.com/campeonato/copa-do-mundo/2006#/fase=copa2006-primeira-fase")
    scan_champ_final_phase(champ_2006, "http://futpedia.globo.com/campeonato/copa-do-mundo/2006#/fase=copa2006-final")
    
    champ_2010 = scan_champ_first_phase("Copa do Mundo", 2010, "http://futpedia.globo.com/campeonato/copa-do-mundo/2010#/fase=primeira-fase")
    scan_champ_final_phase(champ_2010, "http://futpedia.globo.com/campeonato/copa-do-mundo/2010#/fase=oitavas-de-final")
        

if __name__ == "__main__":
    doIt()
