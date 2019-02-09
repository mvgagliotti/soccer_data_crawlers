# coding=UTF-8
'''
Created on Feb 16, 2015

@author: mvgagliotti
'''
from matches.crawler_selenium import scan_champ, scan_champ_first_phase, \
    scan_champ_final_phase


def doIt():
#     scan_champ("Copa do Brasil", 2014, "http://futpedia.globo.com/campeonato/copa-do-brasil/2014", 11, 1) #page_count, ini_page
#     scan_champ("Copa do Brasil", 2013, "http://futpedia.globo.com/campeonato/copa-do-brasil/2013", 11, 1) #page_count, ini_page
#     '''
#     Copa do Brasil 2012: primeira fase + segunda fase + fase final
#     '''
#     champ_2012 = scan_champ_first_phase("Copa do Brasil", 2012, 
#                                         "http://futpedia.globo.com/campeonato/copa-do-brasil/2012#/fase=primeira-fase-copa-do-brasil-2012")
#     scan_champ_final_phase(champ_2012, "http://futpedia.globo.com/campeonato/copa-do-brasil/2012#/fase=oitavas-copa-do-brasil-2012")
# 
#     '''
#     Copa do Brasil 2011: primeira fase + segunda fase + fase final
#     '''
#     champ_2011 = scan_champ_first_phase("Copa do Brasil", 2011, 
#                                         "http://futpedia.globo.com/campeonato/copa-do-brasil/2011#/fase=primeira-fase")
#     scan_champ_final_phase(champ_2011, "http://futpedia.globo.com/campeonato/copa-do-brasil/2011#/fase=oitavas")
#     
#     scan_champ("Copa do Brasil", 2010, "http://futpedia.globo.com/campeonato/copa-do-brasil/2010", 8, 1) #page_count, ini_page
#     scan_champ("Copa do Brasil", 2009, "http://futpedia.globo.com/campeonato/copa-do-brasil/2009", 8, 1) #page_count, ini_page
#     scan_champ("Copa do Brasil", 2008, "http://futpedia.globo.com/campeonato/copa-do-brasil/2008", 8, 1) #page_count, ini_page
#     scan_champ("Copa do Brasil", 2007, "http://futpedia.globo.com/campeonato/copa-do-brasil/2007", 8, 1) #page_count, ini_page
#     scan_champ("Copa do Brasil", 2006, "http://futpedia.globo.com/campeonato/copa-do-brasil/2006", 8, 1) #page_count, ini_page
#     scan_champ("Copa do Brasil", 2005, "http://futpedia.globo.com/campeonato/copa-do-brasil/2005", 8, 1) #page_count, ini_page    
#     scan_champ("Copa do Brasil", 2004, "http://futpedia.globo.com/campeonato/copa-do-brasil/2004", 8, 1) #page_count, ini_page
#     scan_champ("Copa do Brasil", 2003, "http://futpedia.globo.com/campeonato/copa-do-brasil/2003", 8, 1) #page_count, ini_page
#     scan_champ("Copa do Brasil", 2002, "http://futpedia.globo.com/campeonato/copa-do-brasil/2002", 8, 1) #page_count, ini_page
#     scan_champ("Copa do Brasil", 2001, "http://futpedia.globo.com/campeonato/copa-do-brasil/2001", 8, 1) #page_count, ini_page
#     scan_champ("Copa do Brasil", 2000, "http://futpedia.globo.com/campeonato/copa-do-brasil/2000", 9, 1) #page_count, ini_page
# 
    scan_champ("Copa do Brasil", 1999, "http://futpedia.globo.com/campeonato/copa-do-brasil/1999", 8, 1) #page_count, ini_page
    scan_champ("Copa do Brasil", 1998, "http://futpedia.globo.com/campeonato/copa-do-brasil/1998", 5, 1) #page_count, ini_page
    scan_champ("Copa do Brasil", 1997, "http://futpedia.globo.com/campeonato/copa-do-brasil/1997", 6, 1) #page_count, ini_page
    scan_champ("Copa do Brasil", 1996, "http://futpedia.globo.com/campeonato/copa-do-brasil/1996", 5, 1) #page_count, ini_page
    scan_champ("Copa do Brasil", 1995, "http://futpedia.globo.com/campeonato/copa-do-brasil/1995", 5, 1) #page_count, ini_page
     
    scan_champ("Copa do Brasil", 1994, "http://futpedia.globo.com/campeonato/copa-do-brasil/1994", 5, 1) #page_count, ini_page
    scan_champ("Copa do Brasil", 1993, "http://futpedia.globo.com/campeonato/copa-do-brasil/1993", 5, 1) #page_count, ini_page
    scan_champ("Copa do Brasil", 1992, "http://futpedia.globo.com/campeonato/copa-do-brasil/1992", 5, 1) #page_count, ini_page
    scan_champ("Copa do Brasil", 1991, "http://futpedia.globo.com/campeonato/copa-do-brasil/1991", 5, 1) #page_count, ini_page
    scan_champ("Copa do Brasil", 1990, "http://futpedia.globo.com/campeonato/copa-do-brasil/1990", 5, 1) #page_count, ini_page
    scan_champ("Copa do Brasil", 1989, "http://futpedia.globo.com/campeonato/copa-do-brasil/1989", 5, 1) #page_count, ini_page


if __name__ == "__main__":
    doIt()