#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''
from __future__ import absolute_import, print_function, unicode_literals
from mate import dao
from mate.core.model.genericmodel.genericModel import Model
from mate.core.model.modelotable.modeloTabla import ModeloTabla
from mate.model import dto
from mate.vista import factoria
from mate.vista.factoria.mostrarVentanaGui import MostrarVentanaGui
from mate.vista.gui import dlg

class FactoriaVentanas(object):
    u"""Fábrica para crear las distintas instancias de cada ventana de la aplicación."""

    @staticmethod
    def crearVentanaGui(tipo, parent=None, mapParam={}):
        ventana = None
        
        if tipo in factoria.LST_GENERIC_WINDOW:
            ventana = MostrarVentanaGui(tipo, parent, mapParam)
            
        return ventana
    
    @staticmethod
    def __setearParametros(tipo, mapParam):
        pass
        #mapParam['clase_modelo'] = dto.getClaseModelo(tipo)
        #mapParam['dao'] = dao.getClaseModelo(tipo)
        #mapParam['modelo'] = Model
        
        #mapParam['modelo_tabla'] = ModeloTabla
        #mapParam['modelo_datos_tabla'] = dao.getClaseModelo(tipo)
        
        #mapParam['ventana'] = dlg.getClaseModelo(tipo)