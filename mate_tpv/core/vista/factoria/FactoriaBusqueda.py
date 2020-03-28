#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.vista.factoria.BusquedaGui import BusquedaGui
from superbingo.vista.busqueda.factoria.BusquedaBingoGui import BusquedaBingoGui
from superbingo.vista.busqueda.factoria.BusquedaCiudadGui import \
    BusquedaCiudadGui
from superbingo.vista.busqueda.factoria.BusquedaEmpleadoGui import \
    BusquedaEmpleadoGui
from superbingo.vista.busqueda.factoria.BusquedaInstitGui import \
    BusquedaInstitGui
from superbingo.vista.busqueda.factoria.BusquedaInstitPorBingoGui import \
    BusquedaInstitPorBingoGui
from superbingo.vista.busqueda.factoria.BusquedaLoteriaGui import \
    BusquedaLoteriaGui
import sys
sys.path.append('./')


class FactoriaBusqueda(object):
    u"""Fábrica para crear las distintas instancias para interfaces de búsqueda."""

    @staticmethod
    def crearBusquedaGui(tipo, mapParam=None):
        busqueda = None

        if tipo == BusquedaGui.CIUDAD:
            busqueda = BusquedaCiudadGui(mapParam)
        elif tipo == BusquedaGui.INSTIT:
            busqueda = BusquedaInstitGui(mapParam)
        elif tipo == BusquedaGui.INSTIT_POR_BINGO:
            busqueda = BusquedaInstitPorBingoGui(mapParam)
        elif tipo == BusquedaGui.LOTERIA:
            busqueda = BusquedaLoteriaGui(mapParam)
        elif tipo == BusquedaGui.EMPLEADO:
            busqueda = BusquedaEmpleadoGui(mapParam)
        elif tipo == BusquedaGui.BINGO:
            busqueda = BusquedaBingoGui(mapParam)

        return busqueda 