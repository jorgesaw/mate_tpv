#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 21/01/2015

@author: jorgesaw
'''

from core.modelo.modelodatos.modeloDatos import ModeloDatos
from core.modelo.modelogenerico.modeloGenerico import Modelo
import sys
sys.path.append('./')

class ModeloListas(Modelo):
    u""""""
    
    def __init__(self, modeloDatos=None, dao=None):
        super(ModeloListas, self).__init__(modeloDatos, dao)
        
    def guardarListaObjetos(self, lstObjetos):
        msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_SAVE)
        retorno = self.dao.insertMasivo(lstObjetos)
        
        if retorno > 0:
            msg = self.modeloDatos.msg(ModeloDatos.MSG_SAVE)
            
        return (retorno > 0, msg)
    
    def guardarListaDatos(self, matrizDatos):
        self.actualizarListaObjetos(
                                    [self.modeloDatos.creaObjeto(lstDatos) \
                                        for lstDatos in matrizDatos]
                                    )
        
    def actualizarListaObjetos(self, lstObjetos):
        msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_EDIT)
        retorno = self.dao.updateMasivo(lstObjetos)
        
        if retorno > 0:
            msg = self.modeloDatos.msg(ModeloDatos.MSG_EDIT)
            
        return (retorno > 0, msg)
    
    def actualizarListaDatos(self, matrizDatos):
        self.actualizarListaObjetos(
                                    [self.modeloDatos.creaObjeto(lstDatos) \
                                        for lstDatos in matrizDatos]
                                    )
        
    
    def eliminarListaObjetos(self, lstObjetos):
        msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_DELETE)
        retorno = self.dao.deleteMasivo(lstObjetos)
        
        if retorno > 0:
            msg = self.modeloDatos.msg(ModeloDatos.MSG_DELETE)
            
        return (retorno > 0, msg)
    