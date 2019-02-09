# coding=UTF-8
'''
Created on Feb 16, 2015

@author: mvgagliotti
'''
from matches.crawler_selenium import scan_champ, scan_champ_first_phase, \
    scan_champ_final_phase, scan_champ_pontos_corridos
from matches.models_dtos import ChampDTO


def doIt():
#     scan_champ("Copa Libertadores", 2013, "http://futpedia.globo.com/campeonato/taca-libertadores/2013", 10, 1) #page_count, ini_page
    
    '''
    2012: Fase prévia (listagem) + Fase de grupos + Fase Final
    Página da pre estrutura dados da fase-previa em tabela-jogos e demais no esquema de grupos.
    '''
#     champ_2012 = scan_champ_first_phase("Copa Libertadores", 2012, 
#                                         "http://futpedia.globo.com/campeonato/taca-libertadores/2012#/fase=pre-libertadores-2012")
#  
#     scan_champ_final_phase(champ_2012, "http://futpedia.globo.com/campeonato/copa-do-brasil/2012#/fase=oitavas-copa-do-brasil-2012")
    
    '''
    2011
    '''
#     champ_2011 = scan_champ_first_phase("Copa Libertadores", 2011, 
#                                         "http://futpedia.globo.com/campeonato/taca-libertadores/2011#/fase=pre-libertadores")
#     scan_champ_final_phase(champ_2011, "http://futpedia.globo.com/campeonato/taca-libertadores/2011#/fase=oitavas-de-final")
    

#     scan_champ("Copa Libertadores", 2010, "http://futpedia.globo.com/campeonato/taca-libertadores/2010", 10, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 2009, "http://futpedia.globo.com/campeonato/taca-libertadores/2009", 9, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 2008, "http://futpedia.globo.com/campeonato/taca-libertadores/2008", 10, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 2007, "http://futpedia.globo.com/campeonato/taca-libertadores/2007", 10, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 2006, "http://futpedia.globo.com/campeonato/taca-libertadores/2006", 10, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 2005, "http://futpedia.globo.com/campeonato/taca-libertadores/2005", 10, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 2004, "http://futpedia.globo.com/campeonato/taca-libertadores/2004", 10, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 2003, "http://futpedia.globo.com/campeonato/taca-libertadores/2003", 10, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 2002, "http://futpedia.globo.com/campeonato/taca-libertadores/2002", 10, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 2001, "http://futpedia.globo.com/campeonato/taca-libertadores/2001", 10, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 2000, "http://futpedia.globo.com/campeonato/taca-libertadores/2000", 10, 1) #page_count, ini_page
# 
#     scan_champ("Copa Libertadores", 1999, "http://futpedia.globo.com/campeonato/taca-libertadores/1999", 7, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1998, "http://futpedia.globo.com/campeonato/taca-libertadores/1998", 7, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1997, "http://futpedia.globo.com/campeonato/taca-libertadores/1997", 6, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1996, "http://futpedia.globo.com/campeonato/taca-libertadores/1996", 6, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1995, "http://futpedia.globo.com/campeonato/taca-libertadores/1995", 7, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1994, "http://futpedia.globo.com/campeonato/taca-libertadores/1994", 6, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1993, "http://futpedia.globo.com/campeonato/taca-libertadores/1993", 7, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1992, "http://futpedia.globo.com/campeonato/taca-libertadores/1992", 7, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1991, "http://futpedia.globo.com/campeonato/taca-libertadores/1991", 7, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1990, "http://futpedia.globo.com/campeonato/taca-libertadores/1990", 6, 1) #page_count, ini_page

#     scan_champ("Copa Libertadores", 1989, "http://futpedia.globo.com/campeonato/taca-libertadores/1989", 7, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1988, "http://futpedia.globo.com/campeonato/taca-libertadores/1988", 6, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1987, "http://futpedia.globo.com/campeonato/taca-libertadores/1987", 6, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1986, "http://futpedia.globo.com/campeonato/taca-libertadores/1986", 5, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1985, "http://futpedia.globo.com/campeonato/taca-libertadores/1985", 5, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1984, "http://futpedia.globo.com/campeonato/taca-libertadores/1984", 5, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1983, "http://futpedia.globo.com/campeonato/taca-libertadores/1983", 5, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1982, "http://futpedia.globo.com/campeonato/taca-libertadores/1982", 5, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1981, "http://futpedia.globo.com/campeonato/taca-libertadores/1981", 6, 1) #page_count, ini_page
#     scan_champ("Copa Libertadores", 1980, "http://futpedia.globo.com/campeonato/taca-libertadores/1980", 5, 1) #page_count, ini_page

    scan_champ("Copa Libertadores", 1979, "http://futpedia.globo.com/campeonato/taca-libertadores/1979", 5, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1978, "http://futpedia.globo.com/campeonato/taca-libertadores/1978", 5, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1977, "http://futpedia.globo.com/campeonato/taca-libertadores/1977", 5, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1976, "http://futpedia.globo.com/campeonato/taca-libertadores/1976", 6, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1975, "http://futpedia.globo.com/campeonato/taca-libertadores/1975", 6, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1974, "http://futpedia.globo.com/campeonato/taca-libertadores/1974", 6, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1973, "http://futpedia.globo.com/campeonato/taca-libertadores/1973", 5, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1972, "http://futpedia.globo.com/campeonato/taca-libertadores/1972", 5, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1971, "http://futpedia.globo.com/campeonato/taca-libertadores/1971", 5, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1970, "http://futpedia.globo.com/campeonato/taca-libertadores/1970", 6, 1) #page_count, ini_page

    scan_champ("Copa Libertadores", 1969, "http://futpedia.globo.com/campeonato/taca-libertadores/1969", 5, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1968, "http://futpedia.globo.com/campeonato/taca-libertadores/1968", 7, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1967, "http://futpedia.globo.com/campeonato/taca-libertadores/1967", 8, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1966, "http://futpedia.globo.com/campeonato/taca-libertadores/1966", 7, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1965, "http://futpedia.globo.com/campeonato/taca-libertadores/1965", 2, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1964, "http://futpedia.globo.com/campeonato/taca-libertadores/1964", 2, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1963, "http://futpedia.globo.com/campeonato/taca-libertadores/1963", 2, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1962, "http://futpedia.globo.com/campeonato/taca-libertadores/1962", 2, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1961, "http://futpedia.globo.com/campeonato/taca-libertadores/1961", 2, 1) #page_count, ini_page
    scan_champ("Copa Libertadores", 1960, "http://futpedia.globo.com/campeonato/taca-libertadores/1960", 1, 1) #page_count, ini_page


if __name__ == "__main__":
    doIt()