#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 23/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from mate.core.model.modelotable.modeloTabla import ModeloTabla

class ModelTableTPV(ModeloTabla):
    u''''''
    
    def __init__(self, modelo, modeloDatosTabla, parent=None):
        super(ModelTableTPV, self).__init__(modelo, modeloDatosTabla, parent)
        
    def nuevaVenta(self):
        self.modelo.nuevaVenta()
        
    def totalVenta(self):
        return self.modelo.totalVenta()
    
    def cerrarVenta(self):
        bill, msg = self.modelo.cerrarVenta()
        
        return(bill != None, msg)
            