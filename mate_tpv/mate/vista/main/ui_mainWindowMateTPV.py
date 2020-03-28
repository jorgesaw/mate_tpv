# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mate/ui/ui_mainWindowMateTPV.ui'
#
# Created: Sat Mar 28 03:39:55 2015
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

class Ui_MainWindowMateTPV(object):
    def setupUi(self, MainWindowMateTPV):
        MainWindowMateTPV.setObjectName(_fromUtf8("MainWindowMateTPV"))
        MainWindowMateTPV.resize(800, 600)
        MainWindowMateTPV.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindowMateTPV)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineCode = QtGui.QLineEdit(self.centralwidget)
        self.lineCode.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(86, 158, 59);\n"
"font: 48pt \"Lucida Sans\";"))
        self.lineCode.setMaxLength(13)
        self.lineCode.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineCode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineCode.setObjectName(_fromUtf8("lineCode"))
        self.horizontalLayout.addWidget(self.lineCode)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelTotal = QtGui.QLabel(self.centralwidget)
        self.labelTotal.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(86, 158, 59);\n"
"font: 24pt \"Lucida Sans\";"))
        self.labelTotal.setObjectName(_fromUtf8("labelTotal"))
        self.horizontalLayout.addWidget(self.labelTotal)
        self.lineEditTotalNum = QtGui.QLineEdit(self.centralwidget)
        self.lineEditTotalNum.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(86, 158, 59);\n"
"font: 48pt \"Lucida Sans\";"))
        self.lineEditTotalNum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditTotalNum.setReadOnly(False)
        self.lineEditTotalNum.setObjectName(_fromUtf8("lineEditTotalNum"))
        self.horizontalLayout.addWidget(self.lineEditTotalNum)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.tableViewItems = QtGui.QTableView(self.centralwidget)
        self.tableViewItems.setStyleSheet(_fromUtf8("background-color: rgb(156, 156, 156);"))
        self.tableViewItems.setObjectName(_fromUtf8("tableViewItems"))
        self.horizontalLayout_7.addWidget(self.tableViewItems)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(86, 158, 59);\n"
"font: 14pt \"Lucida Sans\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(86, 158, 59);\n"
"font: 16pt \"Lucida Sans\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(86, 158, 59);\n"
"font: 14pt \"Lucida Sans\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.labelTot = QtGui.QLabel(self.centralwidget)
        self.labelTot.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(86, 158, 59);\n"
"font: 16pt \"Lucida Sans\";"))
        self.labelTot.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTot.setObjectName(_fromUtf8("labelTot"))
        self.horizontalLayout_4.addWidget(self.labelTot)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(86, 158, 59);\n"
"font: 14pt \"Lucida Sans\";"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.labelPag = QtGui.QLabel(self.centralwidget)
        self.labelPag.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(86, 158, 59);\n"
"font: 16pt \"Lucida Sans\";"))
        self.labelPag.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPag.setObjectName(_fromUtf8("labelPag"))
        self.horizontalLayout_5.addWidget(self.labelPag)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(86, 158, 59);\n"
"font: 14pt \"Lucida Sans\";"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_6.addWidget(self.label_11)
        self.labelVue = QtGui.QLabel(self.centralwidget)
        self.labelVue.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(86, 158, 59);\n"
"font: 16pt \"Lucida Sans\";"))
        self.labelVue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelVue.setObjectName(_fromUtf8("labelVue"))
        self.horizontalLayout_6.addWidget(self.labelVue)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pBNuevaVenta = QtGui.QPushButton(self.centralwidget)
        self.pBNuevaVenta.setStyleSheet(_fromUtf8(""))
        self.pBNuevaVenta.setObjectName(_fromUtf8("pBNuevaVenta"))
        self.horizontalLayout_2.addWidget(self.pBNuevaVenta)
        self.pBCerrarVenta = QtGui.QPushButton(self.centralwidget)
        self.pBCerrarVenta.setObjectName(_fromUtf8("pBCerrarVenta"))
        self.horizontalLayout_2.addWidget(self.pBCerrarVenta)
        self.pBBuscarProd = QtGui.QPushButton(self.centralwidget)
        self.pBBuscarProd.setObjectName(_fromUtf8("pBBuscarProd"))
        self.horizontalLayout_2.addWidget(self.pBBuscarProd)
        self.pBCerrar = QtGui.QPushButton(self.centralwidget)
        self.pBCerrar.setObjectName(_fromUtf8("pBCerrar"))
        self.horizontalLayout_2.addWidget(self.pBCerrar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindowMateTPV.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowMateTPV)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindowMateTPV.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowMateTPV)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowMateTPV.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowMateTPV)
        QtCore.QObject.connect(self.pBCerrar, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindowMateTPV.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindowMateTPV)

    def retranslateUi(self, MainWindowMateTPV):
        MainWindowMateTPV.setWindowTitle(_translate("MainWindowMateTPV", "MainWindow", None))
        self.labelTotal.setText(_translate("MainWindowMateTPV", "TOTAL:", None))
        self.lineEditTotalNum.setText(_translate("MainWindowMateTPV", "$ 0.00", None))
        self.label.setText(_translate("MainWindowMateTPV", "Forma de pago:", None))
        self.label_2.setText(_translate("MainWindowMateTPV", "Efectivo", None))
        self.label_7.setText(_translate("MainWindowMateTPV", "Total:", None))
        self.labelTot.setText(_translate("MainWindowMateTPV", "0.00", None))
        self.label_9.setText(_translate("MainWindowMateTPV", "Pago:", None))
        self.labelPag.setText(_translate("MainWindowMateTPV", "0.00", None))
        self.label_11.setText(_translate("MainWindowMateTPV", "Vuelto:", None))
        self.labelVue.setText(_translate("MainWindowMateTPV", "0.00", None))
        self.pBNuevaVenta.setText(_translate("MainWindowMateTPV", "Nueva venta (F8)", None))
        self.pBCerrarVenta.setText(_translate("MainWindowMateTPV", "Cerrar Venta (F10)", None))
        self.pBBuscarProd.setText(_translate("MainWindowMateTPV", "PushButton", None))
        self.pBCerrar.setText(_translate("MainWindowMateTPV", "Cerrar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindowMateTPV = QtGui.QMainWindow()
    ui = Ui_MainWindowMateTPV()
    ui.setupUi(MainWindowMateTPV)
    MainWindowMateTPV.show()
    sys.exit(app.exec_())

