#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./')

from PyQt4.QtCore import Qt, pyqtSignature
from PyQt4.QtGui import QDialog, QMessageBox, QIcon
import PyQt4

#from core.vista.factoria.FactoriaBusqueda import FactoriaBusqueda
import ui_dlgCrud

u"""Módulo que contiene la gui para interactuar con un CRUD de mascotas.
    :author: Jorge Adrián Gonzalez
    :version: 1.0.0"""

__docformat__ = "reestructuredtext"

__version__ = "1.0.0"

MAC = hasattr(PyQt4.QtGui, "qt_mac_set_native_menubar")

class CRUD(QDialog,
           ui_dlgCrud.Ui_DlgCrud):
    u"""Dialogo CRUD para CRUD de masoctas."""

    def __init__(self, modelo, parent=None):
        u"""Inicializador de la clase DAO.
            :param modelo: Modelo que maneja los datos de un tipo objeto"""
        super(CRUD, self).__init__(parent)

        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.searchPushButton.setText('')
        self.searchPushButton.setIcon(QIcon(":/find.png"))

        self.modelo = modelo
        self.datosTableView.setModel(self.modelo)
        #self.datosTableView.setAlternatingRowColors(True)
        
        if not MAC:
            self.listPushButton.setFocusPolicy(Qt.NoFocus)
            self.newPushButton.setFocusPolicy(Qt.NoFocus)
            self.delPushButton.setFocusPolicy(Qt.NoFocus)
            self.editPushButton.setFocusPolicy(Qt.NoFocus)
            self.quitPushButton.setFocusPolicy(Qt.NoFocus)
        
        self.on_buscarLineEdit_textEdited('')


    @pyqtSignature("")
    def on_delPushButton_clicked(self):
        self.delData()
        self.updateUi()

    @PyQt4.QtCore.pyqtSlot()
    def on_listPushButton_clicked(self):
        self.listData()

    @pyqtSignature("")
    def searchData(self, tipoBusqueda):
        #busqueda = FactoriaBusqueda.crearBusquedaGui(tipoBusqueda, 
            # {'texto': unicode(self.buscarLineEdit.text())})
        #dato = busqueda.datoBuscado()
        dato = None
        if dato:
            self.modelo.clear()
            self.modelo.insertRowsTabla(0, [dato,])
            self.updateUi()
        self.buscarLineEdit.clear()
        self.on_buscarLineEdit_textEdited('')
        
    @pyqtSignature("QString")
    def on_buscarLineEdit_textEdited(self, text):
        enable = not self.buscarLineEdit.text().isEmpty()
        self.searchPushButton.setEnabled(enable)

    def addData(self, addDlg):
        r = addDlg.exec_()
        if r: # Apretaron "Add"
            row = self.modelo.rowCount()
            ok, msg = self.modelo.insertRows(row, addDlg.data())
            if ok:
                QMessageBox.information(self, "Agregar datos", msg)
                self.updateUi()
            else:
                QMessageBox.information(self, "Agregar datos", msg)

    def delData(self):
        index = self.datosTableView.currentIndex()
        if not index.isValid():
            QMessageBox.information(self, "Eliminar Datos",
                               u"Por favor seleccione una fila de la tabla para eliminar.")
            return
        row = index.row()
        if QMessageBox.question(self, "Remove Datos",
                                u"¿Desea eliminar el dato seleccionado de \n" + 
                                "la base de datos?\n",
                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
            return
        ok, msg = self.modelo.removeRows(row)
        QMessageBox.information(self, "Eliminar datos", msg)
        
    def editData(self, editDlg):
        index = self.datosTableView.currentIndex()
        if not index.isValid():
            QMessageBox.information(self, "Editar Datos",
                               u"Por favor seleccione una fila de la tabla para editar.")
            return
        row = index.row()
        lstData = self.modelo.datosModelo(row)
        editDlg.setData(lstData)
        editDlg.updateUi()
        r = editDlg.exec_()
        if r:
            ok, msg = self.modelo.editRows(index, editDlg.data())
            QMessageBox.information(self, "Editar Datos", msg)

    def listData(self):
        #self.modelo.listData()
        ok, msg = self.modelo.listData(reverse=False)
        if ok:
            self.modelo.updateTable()
        else:
            QMessageBox.information(self, "Listar Datos",
                msg)
        self.updateUi()

    def resizeColumns(self, columns):
        for column in columns:
            self.datosTableView.resizeColumnToContents(column)
            
    def updateUi(self):
        enable = self.modelo.isDatos()
        for btn in (self.delPushButton, self.editPushButton):
            btn.setEnabled(enable)
