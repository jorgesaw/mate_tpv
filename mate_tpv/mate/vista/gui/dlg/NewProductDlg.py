#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 19/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from mate.model.listmodel import listService
from mate.model.models import Category
from mate.vista.gui.dlg.ui_dlgNuevoProducto import Ui_dlgNuevoProducto
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

MAC = hasattr(_qg, "qt_mac_set_native_menubar")

class NewProductDlg(_qg.QDialog, Ui_dlgNuevoProducto):
    def __init__(self, modelo=None, parent=None):
        u"""Diálogo para agregar un nuevo producto."""
        super(NewProductDlg, self).__init__(parent)

        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.modelo = modelo
        self.category = None
        
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setText("&Agregar")
        self.buttonBox.button(_qg.QDialogButtonBox.Cancel).setText("&Cancelar")
        
        if not MAC: 
            self.buttonBox.button(_qg.QDialogButtonBox.Ok).setFocusPolicy(_qc.Qt.NoFocus)
            self.buttonBox.button(_qg.QDialogButtonBox.Cancel).setFocusPolicy(_qc.Qt.NoFocus)
            
        self.setModeloCategories(listService.getListaDatos(
                        Category, seleccionar=True))
        
        self.updateUi()
        
    @_qc.pyqtSlot("QString")
    def on_lineCod_textEdited(self, text):
        self.updateUi()
        
    @_qc.pyqtSlot("QString")
    def on_lineNombre_textEdited(self, text):
        self.updateUi()
        
    @_qc.pyqtSlot("QString")
    def on_lineCodExt_textEdited(self, text):
        self.updateUi()
        
    @_qc.pyqtSlot("QString")
    def on_lineDesc_textEdited(self, text):
        self.updateUi()
        
    @_qc.pyqtSlot(int)
    def on_spinStockMin_valueChanged(self, value):
        if self.spinStockIdeal.value() == 0 or self.spinStockIdeal.value() < value:
            self.spinStockIdeal.setValue(value)
        self.updateUi()
        
    @_qc.pyqtSlot(int)
    def on_spinStockIdeal_valueChanged(self, value):
        self.updateUi()
        
    @_qc.pyqtSlot(int)
    def on_comboRubro_currentIndexChanged(self, index):
        if index >= 1:
            self.category = self.comboRubro. \
                            model().getData(index)
        else:
            self.category = None
        self.updateUi()

    @_qc.pyqtSlot(float)
    def on_spinRatio_valueChanged(self, value):
        self.calcularPrecioVenta()
    
    @_qc.pyqtSlot(float)
    def on_dSpinBoxPrecioCompra_valueChanged(self, value):
        self.calcularPrecioVenta()
    
    @_qc.pyqtSlot(float)
    def on_dSpinBoxPrecio_valueChanged(self, value):
        self.calcularRatio()
    
    def calcularRatio(self):
        if self.dSpinBoxPrecioCompra.value() > 0:
            ratio = (self.dSpinBoxPrecio.value() * \
                     (100/self.dSpinBoxPrecioCompra.value())) - 100
            self.spinRatio.setValue(ratio)
                
    def calcularPrecioVenta(self):
        precio_compra = self.dSpinBoxPrecioCompra.value()
        precio_venta = round(precio_compra * (1 + self.spinRatio.value() / 100.0), 2)
        self.dSpinBoxPrecio.setValue(precio_venta)
                                    
    def setModeloCategories(self, modeloCategories):
        self.comboRubro.setModel(modeloCategories)
        self.comboRubro.setCurrentIndex(0) # Seleccionar.
        
    def data(self):
        return [unicode(self.lineNombre.text()), unicode(self.lineCod.text()),
                unicode(self.lineCodExt.text()) if len(self.lineCodExt.text()) > 0 else None, 
                self.dSpinBoxPrecio.value(), self.dSpinBoxPrecioCompra.value(),   
                self.spinStock.value(), 1, #Cantidad de packs por unidad. 
                self.category, self.spinStockMin.value(), self.spinStockIdeal.value(), 
                unicode(self.lineDesc.text())]
        
    def accept(self):
        if self.modelo:
            self.guardarDatos()
        else:
            _qg.QDialog.accept(self)
            
    def guardarDatos(self):
        tit = u"Nuevo Producto"
        ok, msg = self.modelo.guardarDatos(self.data())
        if ok:
            _qg.QMessageBox.information(self, tit, msg)
            self.buttonBox.button(_qg.QDialogButtonBox.Ok).setEnabled(False)
            self.resetValues()
        else:
            _qg.QMessageBox.information(self, tit, msg)
        
    def resetValues(self):
        self.lineNombre.clear()
        self.lineCod.clear()
        self.lineCodExt.clear()
        self.lineDesc.clear()
        self.dSpinBoxPrecio.setValue(0.00)
        self.dSpinBoxPrecioCompra.setValue(0.00)
        self.spinStock.setValue(0)
        self.spinStockMin.setValue(0)
        self.spinStockIdeal.setValue(0)
        self.category = None
        
    def updateUi(self):
        enable = not (self.lineCod.text().isEmpty() or \
                      len(self.lineCod.text()) < 4 or \
                      self.lineNombre.text().isEmpty() or \
                      not (self.spinStockMin.value() <= self.spinStockIdeal.value()) or \
                      self.category is None)
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setEnabled(enable)
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setDefault(False)