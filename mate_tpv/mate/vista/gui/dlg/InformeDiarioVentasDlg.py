#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 27/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from mate.vista.gui.dlg.ui_dlgInformeDiarioVentas import Ui_DlgInformeDiarioVentas
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import datetime

class InformeDiarioVentasDlg(_qg.QDialog, Ui_DlgInformeDiarioVentas):
    u"""Diálogo para control de stock de productos."""
    
    def __init__(self, modelo=None, parent=None):
        super(InformeDiarioVentasDlg, self).__init__(parent)

        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.modelo = modelo
        
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setText("&Cerrar")
        self.buttonBox.button(_qg.QDialogButtonBox.Cancel).setVisible(False)
        
        self.lstLinesVentas = [self.lineEditVentas, self.lineEditVentTel, 
                     self.lineEditVentCol, self.lineEditTotVentas]
        
        self.dateEditVentas.setDate(datetime.date.today())
        
        self.dateEditVentas.dateChanged.connect(self.buscarTotalVentas)
        
        self.buscarTotalVentas(self.dateEditVentas.date())
    
    @_qc.pyqtSlot("QDate")
    def buscarTotalVentas(self, fecha):
        tit = u"Informe de ventas diario"
        ok, msg = self.modelo.buscarVentasPorFecha([fecha.toPyDate(),])
        if ok:
            self.setData(self.modelo.datosVenta)
        else:
            _qg.QMessageBox.information(self, tit, msg)
            self.resetValues()

    def resetValues(self):
        for line in self.lstLinesVentas:
            line.clear()

    def setData(self, lstDatos):
        for dato, line in zip(lstDatos, self.lstLinesVentas):
            line.setText(unicode(dato))