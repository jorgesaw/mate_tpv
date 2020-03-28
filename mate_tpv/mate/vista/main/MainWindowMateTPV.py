#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 23/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from mate.core.gui.MsgBox import MsgBox
from mate.vista.main.ui_mainWindowMateTPV import Ui_MainWindowMateTPV
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import logging
logger = logging.getLogger(__name__)

class MainWindowMateTPV(_qg.QMainWindow, 
                      Ui_MainWindowMateTPV):
    
    VENTA_CERRADA = 'background-color: rgb(156, 156, 156);'
    VENTA_ABIERTA = 'background-color: rgb(79, 136, 63);'
        
    def __init__(self, modelo=None, parent=None):
        super(MainWindowMateTPV, self).__init__(parent)
        
        #uCrea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.pBNuevaVenta.setFocusPolicy(_qc.Qt.NoFocus)
        self.pBCerrarVenta.setFocusPolicy(_qc.Qt.NoFocus)
        self.pBBuscarProd.setFocusPolicy(_qc.Qt.NoFocus)
        self.pBCerrar.setFocusPolicy(_qc.Qt.NoFocus)
        self.lineEditTotalNum.setFocusPolicy(_qc.Qt.NoFocus)
        self.lineCode.setFocus()
        self.statusbar.setVisible(False)
        self.move(0, 0)
        #self.setWindowFlags(Qt.FramelessWindowHint)#uQuitar barra de título en ventana.
        self.setWindowFlags(_qc.Qt.CustomizeWindowHint) #Deja un marco.
        
        self.modelo = modelo
        self.tableViewItems.setModel(modelo)
        self.modelo.nuevaVenta()
        
        self.cant = 1
        self.venta = False
        self.lineCode.setEnabled(self.venta)
        
        self.resetLabels()
        
        self.connect(self.lineCode, _qc.SIGNAL("returnPressed()"), 
                     self.addProduct)
        
        key = _qg.QShortcut(_qg.QKeySequence(_qc.Qt.Key_F8), self) 
        self.connect(key, _qc.SIGNAL("activated()"), self.nuevaVenta)
        
        key = _qg.QShortcut(_qg.QKeySequence(_qc.Qt.Key_F10), self) 
        self.connect(key, _qc.SIGNAL("activated()"), self.cerrarVenta)
        
        self.pBNuevaVenta.clicked.connect(self.nuevaVenta)
        self.pBCerrarVenta.clicked.connect(self.cerrarVenta)
        
    @_qc.pyqtSlot("QString")
    def on_lineCode_textEdited(self, text):
        if not self.venta:
            _qg.QMessageBox.warning(self, "Crear venta", 
                    u'Por favor cree una venta para agregar ítems vendidos.')
            self.clearLineCode()
            
    def closeEvent(self, event):
        if self.venta:
            _qg.QMessageBox.warning(self, "Cerrar Mate TPV", 
                    u'Imposible cerrar la aplicación\n' + 
                    u'Tiene una venta activa.')
            event.ignore()
        else:    
            if MsgBox.okToContinue(self):
                logging.info(u'Cerrando TPV...')
                event.accept()
            else:
                event.ignore()
                
    def cambiarBkTabla(self, venta=True):
        if venta:
            self.tableViewItems.setStyleSheet(MainWindowMateTPV.VENTA_ABIERTA)
        else:
            self.tableViewItems.setStyleSheet(MainWindowMateTPV.VENTA_CERRADA)
            
    
    def nuevaVenta(self):
        if not self.venta:
            self.resetLabels()
            self.venta = True
            self.modelo.nuevaVenta()
            self.cambiarBkTabla()
        else:
            _qg.QMessageBox.information(self, "Agregar producto", 
                    u'Tiene una venta sin cerrar. Por favor cierre\n' + 
                    u'la venta para iniciar una nueva.')
        
        self.lineCode.setEnabled(self.venta)
        self.lineCode.setFocus()
    
    def cerrarVenta(self):
        value = 0.0
        vuelto = 0.0
        
        if not self.modelo.isDatos(): #uSi no se gregaron ítems a la venta.
            if not MsgBox.okToContinue(self, 'Cerrar venta', 
                                   u'La venta no tiene ítems.\n' + 
                                   u'¿Está seguro que desea cerrarla?'):
                return
        else:
            value, ok = _qg.QInputDialog.getDouble(self, 
                            'Pago', 'Ingresar pago:', 0, 0, 999999.99, 2)
            if not ok:
                return
            
            totVenta = self.modelo.totalVenta()
            vuelto = value - totVenta
            
            if vuelto < 0:
                _qg.QMessageBox.warning(self, "Vuelto venta", 
                        u'Imposible cerrar la venta. Recuerde que el pago\n' + 
                        u'no puede ser menor que el valor de la venta.')
        
        ok, msg = self.modelo.cerrarVenta()
        if not ok:
            _qg.QMessageBox.information(self, "Cerrar venta", msg)
        else:
            self.venta = not ok
            self.modelo.clear()
            self.cambiarBkTabla(False)
            
            self.labelPag.setText('$ {:.2f}'.format(value))
            self.labelVue.setText('$ {:.2f}'.format(vuelto))
        
        self.lineCode.setEnabled(self.venta)
    
    def addProduct(self):
        if len(self.lineCode.text()) < 4:
            if int(self.lineCode.text()) == 0:
                _qg.QMessageBox.information(self, "Agregar producto", 
                                u'Ingrese una cantidad mayor a 0.')
                return
            self.cant = int(self.lineCode.text())
            self.clearLineCode()
            return
        ok, msg = self.modelo.insertRows(self.modelo.rowCount(), self.data())
        if not ok:
            _qg.QMessageBox.information(self, "Agregar producto", msg)
        self.cant = 1
        self.clearLineCode()
        self.mostrarTotal()
        
    def mostrarTotal(self):
        totVenta = '$ {:.2f}'.format(
                        self.modelo.totalVenta())
        self.lineEditTotalNum.setText(totVenta)
        self.labelTot.setText(totVenta)
            
    def resetValues(self):
        self.clearLineCode()
        self.clearLinePrecioTotal()
        
    def resetLabels(self):
        self.labelTot.setText('$ {:.2f}'.format(0.0))
        self.labelPag.setText('$ {:.2f}'.format(0.0))
        self.labelVue.setText('$ {:.2f}'.format(0.0))
                
    def data(self):
        return [self.cant, unicode(self.lineCode.text())]
        
    def clearLineCode(self):
        self.lineCode.clear()
        
    def clearLinePrecioTotal(self):
        self.lineEditTotalNum.clear()