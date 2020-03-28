#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 06/07/2014

@author: jorgesaw
'''

import sys
sys.path.append('./')

from core.modelo.modelodatos.modeloDatos import ModeloDatos

class Modelo(object):
    u"""Modelo genérico para manejo de datos vinculados a una base de datos."""
    
    def __init__(self, modeloDatos=None, dao=None):
        self.modeloDatos = modeloDatos
        self.dao = dao
    
    def guardarDato(self, lstDatos):
        msg = self.modeloDatos.msg(ModeloDatos.MSG_SAVE)
        dato = self.modeloDatos.creaObjeto(lstDatos)
        
        retorno = self.dao.insert(dato)
        if retorno <= 0:
            dato = None
            msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_SAVE)
        
        return (dato, msg)
    
    def eliminarDato(self, dato):
        msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_DELETE)
        retorno = self.dao.delete(dato)
        
        if retorno > 0:
            msg = self.modeloDatos.msg(ModeloDatos.MSG_DELETE)
            
        return (retorno, msg)
    
    def actualizarDatos(self, datoUpdate, lstDatos):
        #msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_EDIT)
        
        self.modeloDatos.editaObjeto(datoUpdate, lstDatos)
        #retorno = self.dao.update(datoUpdate)
        #if retorno > 0:
        #   msg = self.modeloDatos.msg(ModeloDatos.MSG_EDIT)
            
        #return (retorno > 0, msg)
        return self.actualizarDato(datoUpdate)
    
    def actualizarDato(self, datoUpdate):
        msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_EDIT)
        
        retorno = self.dao.update(datoUpdate)
        if retorno > 0:
            msg = self.modeloDatos.msg(ModeloDatos.MSG_EDIT)
            
        return (retorno > 0, msg)
    
    def listarDatos(self, reverse=False):
        msg = self.modeloDatos.msg(ModeloDatos.MSG_LIST_ERROR)
        datos = list(self.dao.getAll(
            self.modeloDatos.tipo()))
            
        if type(datos) == list:
            msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_LIST)
            if len(datos) > 0:
                msg = self.modeloDatos.msg(ModeloDatos.MSG_LIST)
                if reverse:
                    datos.reverse()
            else:
                datos = None
        return (datos, msg)
    
    def datosModelo(self, dato):
        return self.modeloDatos.datosObjeto(dato)
    