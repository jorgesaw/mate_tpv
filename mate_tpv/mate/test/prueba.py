#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 14/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals

class A(object):

    def __init__(self, msg):
        self.msg = msg
        
    @staticmethod
    def met1(msg):
        return msg
    
    @staticmethod
    def creaObjeto(msg):
        return A(msg)
        
    def met2(self):
        print(self.msg)

class B(object):

    @staticmethod
    def met3(msg):
        return msg
        
    def met4(self, msg):
        print(msg)
#clase = A

#clase.met1()



import importlib

mod = importlib.import_module('mate.test.prueba')
clase = getattr(mod, 'A')
lst = []
lst.append(clase.met1("Jaja"))
#print(len(lst))

from mate.core.util.util import import_class
clase = import_class('mate.test.prueba.A')
#print(clase().met2('Hollllla'))

instancia = clase.creaObjeto('Me crearon!!!')
print(instancia.met2())