# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mate/ui/ui_dlgControlStock.ui'
#
# Created: Mon Mar 23 02:17:47 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DlgInformeStock(object):
    def setupUi(self, DlgInformeStock):
        DlgInformeStock.setObjectName(_fromUtf8("DlgInformeStock"))
        DlgInformeStock.resize(540, 359)
        self.verticalLayout = QtGui.QVBoxLayout(DlgInformeStock)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableViewStock = QtGui.QTableView(DlgInformeStock)
        self.tableViewStock.setObjectName(_fromUtf8("tableViewStock"))
        self.verticalLayout.addWidget(self.tableViewStock)

        self.retranslateUi(DlgInformeStock)
        QtCore.QMetaObject.connectSlotsByName(DlgInformeStock)

    def retranslateUi(self, DlgInformeStock):
        DlgInformeStock.setWindowTitle(_translate("DlgInformeStock", "Control de stock", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgInformeStock = QtGui.QDialog()
    ui = Ui_DlgInformeStock()
    ui.setupUi(DlgInformeStock)
    DlgInformeStock.show()
    sys.exit(app.exec_())

