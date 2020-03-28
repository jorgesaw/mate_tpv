#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 06/07/2014

@author: jorgesaw
'''

from core.modelo.modelodatos.modeloDatos import ModeloDatos
from core.modelo.modelogenerico.modeloGenerico import Modelo
import sys
sys.path.append('./')

class ModeloGenBusqueda(Modelo):
    u"""Modelo para buscar datos filtrados en la base de datos."""
    
    def __init__(self, modeloDatos, dao):
        super(ModeloGenBusqueda, self).__init__(modeloDatos, dao)
        
    def getListaDatos(self, mapParam):    
        msg = self.modeloDatos.msg(ModeloDatos.MSG_LIST_ERROR)
        datos = self.dao.getListaDatos(mapParam)
        if datos != None:
            msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_LIST)
            if len(datos) > 0:
                msg = self.modeloDatos.msg(ModeloDatos.MSG_LIST)
            else:
                datos = None
            if mapParam.get('reverse'):
                datos.reverse()
        return (datos, msg)
    