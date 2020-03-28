#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 06/07/2014

@author: jorgesaw
'''

from core.modelo.modelodatos.modeloDatos import ModeloDatos
from core.modelo.modelotable.modeloTabla import ModeloTabla
import sys
sys.path.append('./')

class ModeloTablaBusqueda(ModeloTabla):
    u"""Modelo para manejar los datos de forma tabular."""
    
    def __init__(self, modelo, modeloDatosTabla):
        super(ModeloTablaBusqueda, self).__init__(modelo, modeloDatosTabla)
        self.filaSeleccionada = -1
        
    def listarDatosBuscados(self, mapParam):
        retorno = 0
        datos, msg = self.modelo.getListaDatos(mapParam)
        if datos:
            self.datos = []
            self.datos = datos
            retorno = 1 # uHaydatos para mostrar.
            
        return (retorno > 0, msg) 

    def setFilaSeleccionada(self, fila):
        self.filaSeleccionada = fila
        