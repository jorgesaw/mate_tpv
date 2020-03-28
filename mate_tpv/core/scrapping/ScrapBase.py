#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 24/01/2015

@author: jorgesaw
'''

import logging
logger = logging.getLogger(__name__)

from bs4 import BeautifulSoup
from urllib2 import URLError
import sys
import urllib2
sys.path.append('./')
    
class ScrapBase(object):
    
    BASE_URL = ''
    SEARCH_URL = ''
    
    def __init__(self, param=None):
        #uURL de búsqueda
        self.url = '{0}{1}'.format(ScrapBase.BASE_URL, ScrapBase.SEARCH_URL)
        
        self.param = param
        
        self.soup = None
        #uEncontró un resultado?
        self.found = False
        
        #print self.url
        
        #self._process()
        
    def _process(self):
        response = None
        
        try:
            response = urllib2.urlopen(self.url, self.param)
        except URLError, e:
            logger.error('Error al abrir la url', exc_info=True)
        
        if response:
            self.soup = BeautifulSoup(response.read())
    
        #print "SCRAP BASE"
        #except:
         #   pass
        