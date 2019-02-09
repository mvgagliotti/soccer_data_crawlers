# coding=UTF-8
'''
Created on Sep 7, 2014

@author: mvgagliotti

'''
from matches.crawler_selenium import scan_champ
def do_it():
    '''
    1970 
    Listagem Paginada
    '''
    scan_champ("Torneio Roberto Gomes Pedrosa ", 1970, 
                "http://futpedia.globo.com/campeonato/torneio-roberto-gomes-pedrosa/1970", 10, 10)

    '''
    1969 
    Listagem Paginada
    '''
#     scan_champ("Torneio Roberto Gomes Pedrosa ", 1969, 
#                 "http://futpedia.globo.com/campeonato/torneio-roberto-gomes-pedrosa/1969", 10, 1)
#     
#     '''
#     1968 
#     Listagem Paginada
#     '''
#     scan_champ("Torneio Roberto Gomes Pedrosa ", 1968, 
#                 "http://futpedia.globo.com/campeonato/torneio-roberto-gomes-pedrosa/1968", 10, 1)
# 
#     '''
#     1967 
#     Listagem Paginada
#     '''
#     scan_champ("Torneio Roberto Gomes Pedrosa ", 1967, 
#                 "http://futpedia.globo.com/campeonato/torneio-roberto-gomes-pedrosa/1967", 8, 1)

if __name__ == "__main__":
    do_it()