# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mate/ui/ui_dlgInformeDiarioVentas.ui'
#
# Created: Fri Mar 27 03:38:38 2015
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

class Ui_DlgInformeDiarioVentas(object):
    def setupUi(self, DlgInformeDiarioVentas):
        DlgInformeDiarioVentas.setObjectName(_fromUtf8("DlgInformeDiarioVentas"))
        DlgInformeDiarioVentas.resize(400, 175)
        self.verticalLayout = QtGui.QVBoxLayout(DlgInformeDiarioVentas)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelSelFecha = QtGui.QLabel(DlgInformeDiarioVentas)
        self.labelSelFecha.setObjectName(_fromUtf8("labelSelFecha"))
        self.horizontalLayout.addWidget(self.labelSelFecha)
        self.dateEditVentas = QtGui.QDateEdit(DlgInformeDiarioVentas)
        self.dateEditVentas.setCalendarPopup(True)
        self.dateEditVentas.setObjectName(_fromUtf8("dateEditVentas"))
        self.horizontalLayout.addWidget(self.dateEditVentas)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(DlgInformeDiarioVentas)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditVentas = QtGui.QLineEdit(DlgInformeDiarioVentas)
        self.lineEditVentas.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditVentas.setReadOnly(True)
        self.lineEditVentas.setObjectName(_fromUtf8("lineEditVentas"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditVentas)
        self.lineEditVentTel = QtGui.QLineEdit(DlgInformeDiarioVentas)
        self.lineEditVentTel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditVentTel.setReadOnly(True)
        self.lineEditVentTel.setObjectName(_fromUtf8("lineEditVentTel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditVentTel)
        self.label_3 = QtGui.QLabel(DlgInformeDiarioVentas)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditVentCol = QtGui.QLineEdit(DlgInformeDiarioVentas)
        self.lineEditVentCol.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditVentCol.setReadOnly(True)
        self.lineEditVentCol.setObjectName(_fromUtf8("lineEditVentCol"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditVentCol)
        self.label_4 = QtGui.QLabel(DlgInformeDiarioVentas)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditTotVentas = QtGui.QLineEdit(DlgInformeDiarioVentas)
        self.lineEditTotVentas.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditTotVentas.setReadOnly(True)
        self.lineEditTotVentas.setObjectName(_fromUtf8("lineEditTotVentas"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditTotVentas)
        self.label_2 = QtGui.QLabel(DlgInformeDiarioVentas)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(DlgInformeDiarioVentas)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DlgInformeDiarioVentas)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DlgInformeDiarioVentas.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgInformeDiarioVentas.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgInformeDiarioVentas)
        DlgInformeDiarioVentas.setTabOrder(self.dateEditVentas, self.lineEditVentas)
        DlgInformeDiarioVentas.setTabOrder(self.lineEditVentas, self.lineEditVentTel)
        DlgInformeDiarioVentas.setTabOrder(self.lineEditVentTel, self.lineEditVentCol)
        DlgInformeDiarioVentas.setTabOrder(self.lineEditVentCol, self.lineEditTotVentas)
        DlgInformeDiarioVentas.setTabOrder(self.lineEditTotVentas, self.buttonBox)

    def retranslateUi(self, DlgInformeDiarioVentas):
        DlgInformeDiarioVentas.setWindowTitle(_translate("DlgInformeDiarioVentas", "Informe de ventas diario", None))
        self.labelSelFecha.setText(_translate("DlgInformeDiarioVentas", "Seleccionar fecha:", None))
        self.dateEditVentas.setDisplayFormat(_translate("DlgInformeDiarioVentas", "dd-MM-yyyy", None))
        self.label.setText(_translate("DlgInformeDiarioVentas", "Ventas:", None))
        self.label_3.setText(_translate("DlgInformeDiarioVentas", "Tarjetas colectivo:", None))
        self.label_4.setText(_translate("DlgInformeDiarioVentas", "Total ventas:", None))
        self.label_2.setText(_translate("DlgInformeDiarioVentas", "Tarjetas telefónicas:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgInformeDiarioVentas = QtGui.QDialog()
    ui = Ui_DlgInformeDiarioVentas()
    ui.setupUi(DlgInformeDiarioVentas)
    DlgInformeDiarioVentas.show()
    sys.exit(app.exec_())

