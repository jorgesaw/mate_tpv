#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 23/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from mate.core.model.datamodel.dataModel import DataModel
from mate.core.model.genericmodel.genericModel import Model

class ModelControlStock(Model):
    '''
    Modelo para control de stock de productos.
    '''
    
    def __init__(self, dao=None, dataClase=None, modeloDatos=None):
        super(ModelControlStock, self).__init__(dao, dataClase, modeloDatos)
        
    def listarDatos(self, reverse=False):
        msg = DataModel.LST_MSG[DataModel.MSG_LIST_ERROR]
        datos = list(self.dao.getAllByStockIdealMin())
        
        if type(datos) == list:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_LIST]
            #msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_LIST)
            if len(datos) > 0:
                msg = DataModel.LST_MSG[DataModel.MSG_LIST]
                #msg = self.modeloDatos.msg(ModeloDatos.MSG_LIST)
                #if reverse:
                #   datos.reverse()
            else:
                datos = None
        return (datos, msg)
