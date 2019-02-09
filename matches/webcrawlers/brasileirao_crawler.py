# coding=UTF-8
'''
Created on Jul 23, 2014

@author: mvgagliotti
'''
from matches.crawler_selenium import scan_champ_pontos_corridos,\
    scan_champ_first_phase, scan_champ_final_phase, scan_champ
from matches.models import ConcreteChampionship
from matches.models_dtos import ChampDTO
def doIt():
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2013, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2013-2013", 38)
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2014, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2014", 38)
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2012, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2012", 38)
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2011, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2011", 38)
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2010, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2010", 38)
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2009, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2009", 38)
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2008, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2008", 38)
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2007, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2007", 38)
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2006, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2006", 38)
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2005, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2005", 42)
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2004, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2004", 46)
#     scan_champ_pontos_corridos("Campeonato Brasileiro", 2003, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2003", 46)
#     champ_2002 = scan_champ_first_phase("Campeonato Brasileiro", 2002, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2002#/fase=primeira-fase-brasileiro-serie-a-2002")
#     scan_champ_final_phase(champ_2002, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2002#/fase=quartas-brasileiro-2002")
    
#     '''
#     2001
#     '''
#     champ_2001 = scan_champ_first_phase("Campeonato Brasileiro", 2001, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2001#/fase=primeira-fase-brasileiro-2001")
#     scan_champ_final_phase(champ_2001, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2001#/fase=quartas-brasileiro-2001")
#      
#     '''
#     2000
#     '''
#     champ_2000 = scan_champ_first_phase("Campeonato Brasileiro", 2000, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2000#/fase=primeira-fase-brasileiro-2000")
#     scan_champ_final_phase(champ_2000, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/2000#/fase=oitavas-brasileiro-2000")
#  
#     '''
#     1999
#     '''
#     champ_1999 = scan_champ_first_phase("Campeonato Brasileiro", 1999, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1999#/fase=primeira-fase-brasileiro-1999")
#     scan_champ_final_phase(champ_1999, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1999#/fase=quartas-brasileiro-1999")
#  
#     '''
#     1998
#     '''
#     champ_1998 = scan_champ_first_phase("Campeonato Brasileiro", 1998, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1998#/fase=primeira-fase-brasileiro-1998")
#     scan_champ_final_phase(champ_1998, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1999#/fase=quartas-brasileiro-1999")
#  
#     '''
#     1997
#     TODO: testar segunda fase
#     '''
#     champ_1997 = scan_champ_first_phase("Campeonato Brasileiro", 1997, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1997#/fase=primeira-fase-brasileiro-1997")
#     scan_champ_final_phase(champ_1997, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1997#/fase=final-brasileiro-1997")
#  
#      
#     '''
#     1996
#     '''
#     champ_1996 = scan_champ_first_phase("Campeonato Brasileiro", 1996, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1996#/fase=primeira-fase-brasileiro-1996")
#     scan_champ_final_phase(champ_1996, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1996#/fase=quartas-brasileiro-1996")
#  
#     '''
#     1995
#     TODO: TESTAR
#     '''
#     champ_1995 = scan_champ_first_phase("Campeonato Brasileiro", 1995, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1995#/fase=primeiro-turno-brasileiro-1995")
#     scan_champ_final_phase(champ_1995, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1995#/fase=semifinal-brasileiro-1995")
 
#     '''
#     1994
#     TODO: TESTAR
#     '''
#     champ_1994 = scan_champ_first_phase("Campeonato Brasileiro", 1994, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1994#/fase=primeira-fase-brasileiro-1994")
#     scan_champ_final_phase(champ_1994, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1994#/fase=quartas-brasileiro-1994")
     
 
    '''
    1993
    TODO: formato com playoffs, antes da segunda-fase
    Não deve estar pegando os jogos do playoff: uma possível solução seria dar scan_champ_final_fase
    duas vezes (adicinar booleano que nao grava o arquivo e retorna o champ)
    '''
#     champ_1993 = scan_champ_first_phase("Campeonato Brasileiro", 1993, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1993#/fase=primeira-fase-brasileiro-1993")
#     
#     scan_champ_final_phase(champ_1993, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1993#/fase=playoffs-brasileiro-1993")     
#     
# 
#     '''
#     1992
#     '''
#     champ_1992 = scan_champ_first_phase("Campeonato Brasileiro", 1992, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1992#/fase=primeira-fase-brasileiro-1992")
#     scan_champ_final_phase(champ_1992, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1992#/fase=final-brasileiro-1992")    
#  
#     '''
#     1991
#     '''
#     champ_1991 = scan_champ_first_phase("Campeonato Brasileiro", 1991, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1991#/fase=primeira-fase-brasileiro-1991")
#     scan_champ_final_phase(champ_1991, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1991#/fase=semifinal-brasileiro-1991")
#  
#     '''
#     1990
#     '''
#     champ_1990 = scan_champ_first_phase("Campeonato Brasileiro", 1990, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1990#/fase=primeiro-turno-brasileiro-1990")
#     scan_champ_final_phase(champ_1990, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1990#/fase=quartas-brasileiro-1990")
#          
#     '''
#     1989
#     Formato em listagem paginada
#     '''
#     scan_champ("Campeonato Brasileiro", 1989, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1989", 13, 1)
#  
#     '''
#     1988
#     '''
#     champ_1988 = scan_champ_first_phase("Campeonato Brasileiro", 1988, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1988#/fase=primeiro-turno-brasileiro-1988")
#     scan_champ_final_phase(champ_1988, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1988#/fase=semifinal-brasileiro-1988")
#      
#     '''
#     1987
#     Formato em listagem paginada
#     '''
#     scan_champ("Campeonato Brasileiro", 1987, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1987", 17, 1)
     
#     '''
#     1986
#     '''
#     champ_1986 = scan_champ_first_phase("Campeonato Brasileiro", 1986, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1986#/fase=primeira-fase-brasileiro-1986")
#     scan_champ_final_phase(champ_1986, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1986#/fase=oitavas-de-final-brasileiro-1986")
#      
#     '''
#     1985
#     Formato em listagem paginada
#     '''
#     scan_champ("Campeonato Brasileiro", 1985, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1985", 35, 1)
#  
    '''
    1984
    Formato em listagem paginada
    '''
    scan_champ("Campeonato Brasileiro", 1984, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1984", 21, 1)
 
#     '''
#     1983
#     TODO: testar
#     Repescagem: mesma hipótese do ano de 1993
#     '''
#     champ_1983 = scan_champ_first_phase("Campeonato Brasileiro", 1983, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1983#/fase=segunda-fase-brasileiro-1983")
#     scan_champ_final_phase(champ_1983, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1983#/fase=quartas-de-final-brasileiro-1983")
# 
    '''
    1982
    TODO: testar
    Repescagem: mesma hipótese do ano de 1993
    '''
    champ_1982 = scan_champ_first_phase("Campeonato Brasileiro", 1982, 
                                        "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1982#/fase=segunda-fase-brasileiro-1982")
    scan_champ_final_phase(champ_1982, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1982#/fase=oitavas-de-final-brasileiro-1982")
     
    '''
    1981
    TODO: testar
    '''
    champ_1981 = scan_champ_first_phase("Campeonato Brasileiro", 1981, 
                                        "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1981#/fase=primeira-fase-brasileiro-1981")
    scan_champ_final_phase(champ_1981, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1981#/fase=oitavas-de-final-brasileiro-1981")
# 
#     '''
#     1980
#     TODO: testar
#     Problema: futpedia aponta 307 jogos: 
#     O campeonato tem uma fase de jogo extra + 6 jogos da fase final + 298 das fases primeiras, totalizando 305 jogos 
#     '''
#     champ_1980 = scan_champ_first_phase("Campeonato Brasileiro", 1980, 
#                                         "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1980#/fase=primeira-fase-brasileiro-1980")
#     scan_champ_final_phase(champ_1980, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1980#/fase=semifinal-brasileiro-1980")
#     
    '''
    1979
    TODO: testar
    '''
    champ_1979 = scan_champ_first_phase("Campeonato Brasileiro", 1979, 
                                        "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1979#/fase=primeira-fase-brasileiro-1979")
    scan_champ_final_phase(champ_1979, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1979#/fase=semifinal-brasileiro-1979")
     
    '''
    1978
    TODO: testar
    '''
    champ_1978 = scan_champ_first_phase("Campeonato Brasileiro", 1978, 
                                        "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1978#/fase=primeira-fase-brasileiro-1978")
    scan_champ_final_phase(champ_1978, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1978#/fase=quartas-de-final-brasileiro-1978")
 
    '''
    1977
    TODO: testar
    '''
    champ_1977 = scan_champ_first_phase("Campeonato Brasileiro", 1977, 
                                        "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1977#/fase=primeira-fase-brasileiro-1977    ")
    scan_champ_final_phase(champ_1977, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1977#/fase=semifinal")
 
    '''
    1976
    TODO: testar
    '''
    champ_1976 = scan_champ_first_phase("Campeonato Brasileiro", 1976, 
                                        "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1976#/fase=primeira-fase")
    scan_champ_final_phase(champ_1976, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1976#/fase=semifinal")
 
    '''
    1975
    Formato em listagem paginada
    '''
    scan_champ("Campeonato Brasileiro", 1975, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1975", 29, 1)
 
    '''
    1974
    TODO: testar
    '''
    champ_1974 = scan_champ_first_phase("Campeonato Brasileiro", 1974, 
                                        "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1974#/fase=primeirafase")
    scan_champ_final_phase(champ_1974, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1974#/fase=final-classificacao")
 
    '''
    1973
    Formato em listagem paginada
    '''
    scan_champ("Campeonato Brasileiro", 1973, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1973", 44, 1)
 
    '''
    1972
    Formato em listagem paginada
    '''
    scan_champ("Campeonato Brasileiro", 1972, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1972", 24, 1)
 
    '''
    1971
    Formato em listagem paginada
    '''
    scan_champ("Campeonato Brasileiro", 1971, "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1971", 16, 1)
    
    
def test_it():
    champ_1974 = scan_champ_first_phase("Campeonato Brasileiro", 1974, 
                                        "http://futpedia.globo.com/campeonato/campeonato-brasileiro/1974#/fase=primeirafase")
    
if __name__ == "__main__":
#     test_it()
    doIt()
