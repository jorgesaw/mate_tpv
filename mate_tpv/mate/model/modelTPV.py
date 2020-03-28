#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 23/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from mate.core.model.datamodel.dataModel import DataModel
from mate.core.model.genericmodel.genericModel import Model
from mate.model.models import Bill, Item, Product

class ModelTPV(Model):
    u''''''
    
    def __init__(self, dao=None, dataClase=None, modeloDatos=None):
        super(ModelTPV, self).__init__(dao, dataClase, modeloDatos)
        
        self.bill = None
        
    def nuevaVenta(self):
        self.bill = Bill()
        
    def cerrarVenta(self):
        #self.bill.close()
        
        #self.bill, msg = Model.guardarDato(self, self.bill)
        
        #uPara evitar cambios en el stock de los productos 
        #u si la factura no puede guardarse.
        bill = self.bill.copy()
        bill.close()
        #self.bill, msg = Model.guardarDato(self, self.bill)
        
        bill, msg = Model.guardarDato(self, bill)
        
        if bill: #uSi se guardó 
            self.bill = bill
        
        return (self.bill, msg)
        
    def guardarDatos(self, lstDatos):
        msg = DataModel.LST_MSG[DataModel.MSG_NOT_GET_DATO]
        item = None
        #uBusco el producto en la DB.
        prod = self.dao.get(lstDatos[1], Product) #uCódigo del producto.
        if prod:
            msg = DataModel.LST_MSG[DataModel.MSG_GET_DATO]
            #uSi existe el producto creamos un ítem.
            item = Item(prod, lstDatos[0])
            self.bill.addItem(item)
            
        return (item, msg)
    
    def totalVenta(self):
        self.bill.calculate()
        return self.bill.total