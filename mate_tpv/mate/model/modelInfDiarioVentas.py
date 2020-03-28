#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 27/03/2015

@author: jorgesaw
'''
from mate.core.model.datamodel.dataModel import DataModel
from mate.core.model.genericmodel.genericModel import Model
from mate.model import models

class ModelInfDiarioVentas(Model):
    
    def __init__(self, dao=None, dataClase=None, modeloDatos=None):
        super(ModelInfDiarioVentas, self).__init__(dao, dataClase, modeloDatos)
        
        self.datosVenta = []
        
    def buscarVentasPorFecha(self, lstDatos):
        msg = DataModel.LST_MSG[DataModel.MSG_LIST_ERROR]
        datosEncontrados = False
        ventas = list(self.dao.getVentasPorFecha(lstDatos[0]))
        
        if type(ventas) == list:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_LIST]
            if len(ventas) > 0:
                msg = DataModel.LST_MSG[DataModel.MSG_LIST]
                datosEncontrados = True
                self.datosVenta = ventas
                self.calcularSubTotales()
        
        return (datosEncontrados, msg)
    
    def calcularSubTotales(self):
        totTarjTel = 0.0; totTarjCol = 0.0
        ventas = 0.0; totVentas = 0.0
        
        for venta in self.datosVenta:
            #print("TOTAL_VENTA:", venta.claculate)
            for item in venta.items:
                if item.product.category.id == models.ID_CATEGORY_TARJ_TEL:
                    totTarjTel += item.calculate()
                elif item.product.category.id == models.ID_CATEGORY_TARJ_COL:
                    totTarjCol += item.calculate()
            venta.calculate()
            totVentas += venta.total
            
        ventas = totVentas - (totTarjTel + totTarjCol) 
        
        self.datosVenta = [ventas, totTarjTel, 
                           totTarjCol, totVentas]