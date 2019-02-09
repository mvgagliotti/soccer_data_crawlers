# coding=UTF-8
'''
Created on Apr 12, 2014

@author: mvgagliotti
'''
def get_home_team_goal_data(driver, li_index, goal_index, auto=False):
    '''
        Retorna string com minuto e tempo de jogo que ocorreu o gol
        ie. 17' / 1TR
    '''
    
    if auto:
        str_auto = "-contra"
    else:
        str_auto = ""
    
    script = """
        var elements = jQuery.find('#escalacao-mandante > ul > li:nth-child({0}) > div.gol{1} > div > div.content')
        var _index = {2};
        
        if (elements && elements[_index]) {{ 
         return elements[_index].textContent;         
        }} else {{ 
         return "";
        }}         
    """.format(li_index, str_auto, goal_index-1)
        
    return driver.execute_script(script, None)


def get_home_team_sub(driver, li_index):
    '''
    '''
    script = """
        var elements = jQuery.find('#escalacao-mandante > ul > li:nth-child({0}) > div.entrou > div > div.content');
                
        if (elements && elements.length > 0) {{ 
         return elements[0].textContent;         
        }} else {{ 
         return "";
        }}         
    """.format(li_index)
    
    return driver.execute_script(script, None)

def get_home_team_yellow_card(driver, li_index, card_index):
    '''
        Retorna string com minuto e tempo de jogo que ocorreu o cartão
        ie. 17' / 1TR
    '''
        
    script = """
        var elements = jQuery.find('#escalacao-mandante > ul > li:nth-child({0}) > div.cartao-amarelo')
        var _index = {1};
        
        if (elements && elements[_index]) {{ 
         return elements[_index].textContent;         
        }} else {{ 
         return "";
        }}         
    """.format(li_index, card_index-1)
        
    return driver.execute_script(script, None)

def get_home_team_red_card(driver, li_index, card_index):
    '''
        Retorna string com minuto e tempo de jogo que ocorreu o cartão
        ie. 17' / 1TR
    '''
        
    script = """
        var elements = jQuery.find('#escalacao-mandante > ul > li:nth-child({0}) > div.cartao-vermelho')
        var _index = {1};
        
        if (elements && elements[_index]) {{ 
         return elements[_index].textContent;         
        }} else {{ 
         return "";
        }}         
    """.format(li_index, card_index-1)
        
    return driver.execute_script(script, None)


def get_away_team_goal_data(driver, li_index, goal_index, auto=False):
    '''
        Retorna string com minuto e tempo de jogo que ocorreu o gol
        ie. 17' / 1TR
    '''
    
    if auto:
        str_auto = "-contra"
    else:
        str_auto = ""
    
    script = """
        var elements = jQuery.find('#escalacao-visitante > ul > li:nth-child({0}) > div.gol{1} > div > div.content')
        var _index = {2};
        
        if (elements && elements[_index]) {{ 
         return elements[_index].textContent;         
        }} else {{ 
         return "";
        }}         
    """.format(li_index, str_auto, goal_index-1)
        
    return driver.execute_script(script, None)


def get_away_team_sub(driver, li_index):
    '''
    '''
    script = """
        var elements = jQuery.find('#escalacao-visitante > ul > li:nth-child({0}) > div.entrou > div > div.content');
                
        if (elements && elements.length > 0) {{ 
         return elements[0].textContent;         
        }} else {{ 
         return "";
        }}         
    """.format(li_index)
    
    return driver.execute_script(script, None)

def get_away_team_yellow_card(driver, li_index, card_index):
    '''
        Retorna string com minuto e tempo de jogo que ocorreu o cartão
        ie. 17' / 1TR
    '''
        
    script = """
        var elements = jQuery.find('#escalacao-visitante > ul > li:nth-child({0}) > div.cartao-amarelo')
        var _index = {1};
        
        if (elements && elements[_index]) {{ 
         return elements[_index].textContent;         
        }} else {{ 
         return "";
        }}         
    """.format(li_index, card_index-1)
        
    return driver.execute_script(script, None)
    
    
def get_away_team_red_card(driver, li_index, card_index):
    '''
        Retorna string com minuto e tempo de jogo que ocorreu o cartão
        ie. 17' / 1TR
    '''
        
    script = """
        var elements = jQuery.find('#escalacao-visitante > ul > li:nth-child({0}) > div.cartao-vermelho')
        var _index = {1};
        
        if (elements && elements[_index]) {{ 
         return elements[_index].textContent;         
        }} else {{ 
         return "";
        }}         
    """.format(li_index, card_index-1)
        
    return driver.execute_script(script, None)


if __name__ == "__main__":
    get_home_team_goal_data(None, 14, 1)