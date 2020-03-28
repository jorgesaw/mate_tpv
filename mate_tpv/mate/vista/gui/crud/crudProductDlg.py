'''
Created on 19/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
import PyQt4.QtCore as _qc
from mate.core.vista.crud.CRUD import CRUD
from mate.vista.gui.dlg.NewProductDlg import NewProductDlg
from mate.vista.gui.dlg.EditProductDlg import EditProductDlg

class CrudProductDlg(CRUD):
    u"""Dialogo CRUD de productos."""

    def __init__(self, modelo, parent=None):
        super(CrudProductDlg, self).__init__(modelo, parent)

        #self.datosTableView.setItemDelegate(CiudadesDelegate())
        self.updateUi()
        self.datosTableView.setStyleSheet('background-color: rgb(156, 156, 156);')
        #CRUD.resizeColumns(self, (ModeloDatosCiudad.NOMBRE, ModeloDatosCiudad.COD_POSTAL,
        #ModeloDatosCiudad.DDN, ModeloDatosCiudad.PROVINCIA))
        self.setWindowTitle("CRUD Productos")

    @_qc.pyqtSlot()
    def on_newPushButton_clicked(self):
        addDlg = NewProductDlg()
        CRUD.addData(self, addDlg)

    @_qc.pyqtSlot()
    def on_editPushButton_clicked(self):
        editDlg = EditProductDlg()
        CRUD.editData(self, editDlg)

    @_qc.pyqtSlot()
    def on_listPushButton_clicked(self):
        CRUD.listData(self)

    @_qc.pyqtSlot()
    def on_searchPushButton_clicked(self):
        pass#CRUD.searchData(self, BusquedaGui.INSTIT)

    def updateUi(self):
        CRUD.updateUi(self)