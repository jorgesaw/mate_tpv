#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 13/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from PyQt4.QtCore import Qt
from mate.core.gui.Actions import createAction, addActions
from mate.core.gui.MsgBox import MsgBox
from mate.core.model.modelotable.modeloTabla import ModeloTabla
from mate.core.vista.crud.CRUD import CRUD
from mate.vista import config_main, factoria
from mate.vista.factoria.factoriaVentanas import FactoriaVentanas
from mate.vista.gui.crud.crudProductDlg import CrudProductDlg
from mate.vista.gui.dlg.NewProductDlg import NewProductDlg
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import logging
import tpv_gui_run
logger = logging.getLogger(__name__)

class MainWindow(_qg.QMainWindow):
    """Ventana principal de la aplicación."""
    
    def __init__(self, app, parent=None):
        super(MainWindow, self).__init__(parent)
        self.app = app
        #self.mdiArea = QMdiArea()
        #self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        #self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdi = _qg.QWorkspace()
        #bc = _qg.QPixmap(config_main.BCK_IMAGE)
        #bc = bc.scaled(700, 640, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        #br = _qg.QBrush(bc)
        
        #self.mdi.setBackground(br)
        self.mdi.setBackground(_qg.QColor(79, 136, 63))
        self.mdi.setAutoFillBackground(False)
        self.setCentralWidget(self.mdi)
        
    
        self.createActions()
        self.createMenus()
        
    def createActions(self):
        self.archivoSalirAction=None;self.artNuevoAction=None;\
        self.artMostrarAction=None;#self.artLimiteSalirAction=None;\
        self.rubroNuevoAction=None;self.rubroMostrarAction=None;\
        self.informeStock=None;self.ventasInformeAction=None;
        self.mateTPV=None
        #uEl orden de las aaciones son determina por las constantes del paquete factoria.
        #u factoria.APP_EXIT = 0
        lstActions = [self.archivoSalirAction, self.artNuevoAction, 
                      self.artMostrarAction, #self.artLimiteSalirAction, 
                      self.rubroNuevoAction, self.rubroMostrarAction, 
                      self.informeStock, self.ventasInformeAction, 
                      self.mateTPV]
        
        lstSlot = [self.close,]
        size = len(lstSlot)
        for i in range(len(lstActions) - size):
            lstSlot.append(self.searchWindow)
        
        self.matrizActions = config_main.getActions(self, lstActions, lstSlot)
        #print(self.matrizActions)
        
    def createMenus(self):
        self.archivoMenu=None; self.articulosMenu=None; self.rubroMenu=None
        self.informeMenu=None; self.ventasMenu=None; self.mate_tpvMenu=None
        lstMenus = [self.archivoMenu, self.articulosMenu, self.rubroMenu, 
                    self.informeMenu, self.ventasMenu, 
                    self.mate_tpvMenu]
        
        config_main.getMenus(self, lstMenus, self.matrizActions)
        
    def closeEvent(self, event):
        #uTambién guardamos la geometria(tamaño) de la ventana de la app.
        if MsgBox.okToContinue(self):
            settings = _qc.QSettings()
            settings.setValue("MainWindow/Size", _qc.QVariant(self.size()))
            settings.setValue("MainWindow/Position", _qc.QVariant(self.pos()))
            settings.setValue("MainWindow/State", _qc.QVariant(self.saveState()))
            #settings.setValue("Geometry", QVariant(self.saveGeometry()))
            logging.info(u'Cerrando la aplicación...')
            event.accept()
        else:
            event.ignore()
        
    def searchWindow(self):
        sender = self.sender().data().toInt()[0]
        maximized= False
        focus=False
        if sender == factoria.GUI_MATE_TPV:
            maximized = True
            focus = True
        self.loadWindow(sender, maximized, focus)
        
    def loadWindow(self, wnd, maximized=False, focus=False):
        gui = FactoriaVentanas.crearVentanaGui(wnd, parent=self.mdi)
        #if not self.app.isWindowActived(gui.tipo()):
        dlg = gui.prepararVentana()
        if dlg:
            if not self.app.isWindowActived(type(dlg)):
                self.app.showWindow(dlg)
                if focus:
                    dlg.setFocus()
                if maximized:
                    dlg.showMaximized()
                
    def m(self):
        modelo = ModeloTabla(None, None)
        ventana = CrudProductDlg(modelo)
        
        #ventana = NewProductDlg()
        ventana.move(0, 0)
        
        if len(self.mdi.windowList()) > 0:
            self.mdi.closeAllWindows()
        self.mdi.addWindow(ventana)
        ventana.show()