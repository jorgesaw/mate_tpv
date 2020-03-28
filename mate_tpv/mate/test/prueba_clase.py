#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 14/02/2015

@author: jorgesaw
'''

class PruebaNombre(object):

    def __init__(self, nombre):
        self.nombre = nombre
        
    @staticmethod
    def creaObjeto(lst_datos):
        pn = PruebaNombre(lst_datos[0])
        return pn
    
from mate.core.util.util import import_class
clase = import_class('mate.test.prueba_clase.PruebaNombre')
#print(clase('Juanito').nombre)
instancia = clase.creaObjeto(['Juanito Lobo'])
print(instancia.nombre)
