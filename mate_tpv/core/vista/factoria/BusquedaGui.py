#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BusquedaGui(object):

    CIUDAD, \
    INSTIT, \
    LOTERIA, \
    EMPLEADO, \
    INSTIT_POR_BINGO, \
    BINGO = range(6)

    def __init__(self, mapParam=None):
        self.mapParam = mapParam
        self.dato = None
        
    def datoBuscado(self):
        return self.dato

    def setDatoBuscado(self, dato):
        self.dato = dato
    