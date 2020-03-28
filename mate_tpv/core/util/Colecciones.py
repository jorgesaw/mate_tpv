#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/01/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals

class Colecciones(object):

    @staticmethod
    def binarySearch(datos, elemBusqueda):
        datos.sort()
        inferior = 0
        superior = len(datos) - 1
        medio = (inferior + superior + 1) / 2
        ubicacion = -1

        while inferior <= superior and ubicacion == -1:
            if elemBusqueda == datos[medio]:
                ubicacion = medio
            elif elemBusqueda < datos[medio]:
                superior = medio -1
            else:
                inferior = medio + 1
            medio = (inferior + superior + 1) / 2

        return ubicacion
