#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 24/01/2015

@author: jorgesaw
'''

from bs4 import BeautifulSoup
import urllib2
from core.scrapping.ScrapBase import ScrapBase
import sys
from core.util.ManejaFechas import ManejaFechas
sys.path.append('./')



class ScrapLotNacional(ScrapBase):
    
    ScrapBase.BASE_URL = 'http://www.loteria-nacional.gov.ar'
    
    LST_STR_HORA = ['pre', 'mat', 'ves',  'noc']
    
    def __init__(self, fechaSorteo, horario, loteria = None):
        ScrapBase.SEARCH_URL = \
            '/Internet/Extractos/resultados_i.php?juego=quiniela&fechasorteo={0}&tiposorteo={1}'\
                .format(ManejaFechas.date2Str(fechaSorteo, '%d%m%Y'), 
                    ScrapLotNacional.LST_STR_HORA[horario])

        super(ScrapLotNacional, self).__init__()
        
                
        #uLista con los 20 números de la lotería.
        self.numeros = []
        
        self._process()
        
    def _process(self):
        ScrapBase._process(self)
        
        try:
            p_tags_col1 = self.soup.select('#Columna1Quiniela p')
            p_tags_col2 = self.soup.select('#Columna2Quiniela p')
            
            numeros = [int(p.text) for p in (p_tags_col1 + p_tags_col2)]
            
            self.found = len(numeros) == 20
            if self.found:
                self.numeros = numeros
        
        except:
            pass
