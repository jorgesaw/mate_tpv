#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 25/01/2015

@author: jorgesaw
'''

import sys
sys.path.append('./')
from bs4 import BeautifulSoup
from core.scrapping.ScrapBase import ScrapBase
from core.scrapping.ScrapLotNacional import ScrapLotNacional
from core.util.ManejaFechas import ManejaFechas
import urllib2
import urllib

class ScrapLoterias(ScrapBase):
    #uhttps://www.google.com.ar/search?q=tu+jugada&oq=tu+jugada&aqs=chrome..69i57j69i65l3j69i60l2.1843j0j7&sourceid=chrome&es_sm=122&ie=UTF-8
    #http://stackoverflow.com/questions/4375669/logging-in-python-with-config-file-using-handlers-defined-in-file-through-code
    #http://stackoverflow.com/questions/7922602/python-2-4-3-configparser-nosectionerror-no-section-formatters
 
    ScrapBase.BASE_URL = 'http://www.quinielasargentinas.com/verResultadosQuiniela.php'
    
    NAC, BSA, SFE, ERI = range(4)

    PRE, MAT, VES, NOC = range(4)
    
    def __init__(self, fechaSorteo, horario, loteria):
        super(ScrapLoterias, self).__init__(param = urllib.urlencode({'fecha_sorteo': fechaSorteo}))
        self.horario = horario
        self.loteria = loteria
        
        #uLista con los 20 números de la lotería.
        self.numeros = []
            
        self._process()
        
    def _process(self):
        ScrapBase._process(self)
        
        if not self.soup:
            return
        
        td_tags = self.soup.select('td')
        
        cont = -1
        cant_1 = 0
        intervalo = 5
        
        #horario = PRE
        cant_num = 99
        #lot = ERI
        if self.horario > ScrapLoterias.MAT:# and lot > SFE: #Si la loteria es VES o NOC y se quiere 
            intervalo = 6
            cant_num = 119
            if self.loteria > ScrapLoterias.SFE:
                self.loteria = self.loteria + 1
        if self.horario > ScrapLoterias.VES:
            intervalo = 7
            cant_num = 140
            
        
        for td in td_tags:
            cont = cont + 1
            
            if td.text == '1':
                cant_1 = cant_1 + 1
                if cant_1  == self.horario + 1:
                    break
        
        #Quiniela de Santa fe
        pos = self.loteria + 1
        lstNumeros = []
        for i in range(cont + pos, cont+pos+cant_num, intervalo):
            lstNumeros.append(td_tags[i].text)
        
        #print lstNumeros
        numeros = [int(num) for num in lstNumeros]
            
        self.found = len(numeros) == 20
        if self.found:
            self.numeros = numeros
        