# coding=UTF-8
'''
Created on Oct 12, 2014

@author: mvgagliotti
'''
from django.core.management.base import BaseCommand
import logging
import datetime

from matches.models import MatchImporter
import os
from fut_friends import settings
from matches.models_importer import read_zip_file, import_champ
from django.utils._os import npath
import sys
import traceback
from fut_friends.common import JsonHelper
import json
from django.utils import timezone

class Command(BaseCommand):
    """
    Classe que dispara uma importação, caso haja na tabela de controle 
    de importações um registro indicando que alguém disparou (via interface web)
    uma nova importação. 
    
    O shell script "importer_checker.sh" deve ser configurado no cron
    da máquina para disparar a cada 1 minuto o comando: 
    
    python manage.py run_importer
    
    A seguinte linha deve ser adicionada ao crontab da máquina, sendo que PATH corresponde ao caminho
    na máquina antes da pasta "f-friends": 
    
    * * * * * <PATH>/f-friends/fut_friends/importer_checker.sh     
    
    """    
    
    def handle(self, *args, **options):        
        logger = logging.getLogger('match_importer')
        try:
            self.do_import(logger)
        except Exception, e:
            logger.debug(e)

    def do_import(self, logger):
        logger.debug("Verificando se há importação a ser processada")
        
        '''
        Obtém o primeiro registro nao iniciado
        TODO: filtrar por usuário ?       
        '''
        try:
            result_set = MatchImporter.objects.filter(start_time__isnull=True)
            if not result_set:
                logger.debug("sem importações pendentes no momento")
                return
            
            importer_entry = result_set[0]
            importer_entry.start_time = timezone.now()
            importer_entry.save()

            print "Antes de importar"
            self.run_importer(importer_entry, logger)
            print "Depois de importar"
            importer_entry.set_imported()
        except Exception, e:
            logger.debug("Ocorreu um erro ao importar %s: %s" % (importer_entry.filename, traceback.format_exc()))
            importer_entry.set_not_imported()
            print traceback.format_exc()
            
            raise e
            
    
    def run_importer(self, importer_entry, logger):
        
        filename = os.path.join(settings.IMPORTER_PATH, importer_entry.filename)
        logger.debug("Importando %s" % (filename))
        
        '''
        Extraindo o zip para a pasta de importação
        '''
        read_zip_file(filename, settings.IMPORTER_PATH)
        
        '''
        Começando a importação
        TODO: **********ver se eh seleção ou não!!**************
        
        * * * * * /home/mvgagliotti/python-stuff/f-friends/fut_friends/importer_checker.sh        
        '''
        
        def name_and_season(f_name):
            result = {}
            f_name_withou_ext = os.path.splitext(os.path.basename(f_name))[0]
            underline_splitted = f_name_withou_ext.split('_')
            
            result['champ_name'] = '_'.join(underline_splitted[:len(underline_splitted)-1])
            result['champ_season'] = int(underline_splitted[len(underline_splitted)-1]) 
            
            return result
        
        '''
        Cria dictionary com os argumentos e chama a funçao
        '''
        args_dict = name_and_season(filename)
        args_dict['is_from_national_team'] = False #TODO: rever isto aqui!!
        args_dict['importer_entry'] = importer_entry
        
        '''
        Faz a importação!
        '''
        import_champ(**args_dict)
                

if __name__ == "__main__":
    
    my_dict = {'id':'1'}
    _str = JsonHelper().to_json(my_dict)
    print _str
    
#     Command().do_import(logging.getLogger('match_importer'))