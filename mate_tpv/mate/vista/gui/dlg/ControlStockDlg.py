#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 23/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from mate.vista.gui.dlg.ui_dlgControlStock import Ui_DlgInformeStock
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

class ControlStockDlg(_qg.QDialog, Ui_DlgInformeStock):
    u"""Diálogo para control de stock de productos."""
    
    def __init__(self, modelo=None, parent=None):
        super(ControlStockDlg, self).__init__(parent)

        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.modelo = modelo
        self.tableViewStock.setModel(self.modelo)
        
        self.listData()
        
        
    def listData(self):
        ok, msg = self.modelo.listData()
        if ok:
            self.modelo.updateTable()
        else:
            _qg.QMessageBox.information(self, "Listar Datos", msg)