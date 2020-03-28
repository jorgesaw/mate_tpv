#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

NAME, CODE, EXT_CODE, PRICE, BUY_PRICE, STOCK, PACK_UNITS, CATEGORY, \
MIN_STOCK, IDEAL_STOCK, DESCRIPTION = range(11)

lstHeader = [NAME, CODE, EXT_CODE, PRICE, BUY_PRICE, STOCK, PACK_UNITS, CATEGORY, \
MIN_STOCK, IDEAL_STOCK, DESCRIPTION]

lstTitHeader = ['Nombre', u'Código', u'Código externo', 'Precio', 'Precio compra', 'Stock',  
             'Und x pack', 'Rubro', 'Stock min.', 'Stock ideal', u'Descripción']

class ModeloDatosTablaProduct(object):
    u""""""

    def __init__(self):
        pass
    
    def columnCount(self, index=_qc.QModelIndex()):
        return 11

    def data(self, index, dato, role=_qc.Qt.DisplayRole):
        column = index.column()
        if role == _qc.Qt.DisplayRole:
            if column == NAME:
                return _qc.QVariant(dato.name)
            elif column == CODE:
                return _qc.QVariant(dato.code)
            elif column == EXT_CODE:
                return _qc.QVariant(dato.external_code)
            elif column == PRICE:
                return _qc.QVariant(dato.price)
            elif column == BUY_PRICE:
                return _qc.QVariant(dato.buy_price)
            elif column == STOCK:
                return _qc.QVariant(dato.stock)
            elif column == PACK_UNITS:
                return _qc.QVariant(dato.pack_units)
            elif column == CATEGORY:
                return _qc.QVariant(dato.category.name)
            elif column == MIN_STOCK:
                return _qc.QVariant(dato.min_stock)
            elif column == IDEAL_STOCK:
                return _qc.QVariant(dato.ideal_stock)
            elif column == DESCRIPTION:
                return _qc.QVariant(dato.description)
        elif role == _qc.Qt.TextAlignmentRole:
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        elif role == _qc.Qt.BackgroundColorRole:
            row = index.row()
            if row % 2 == 0: # Si es par.
                return _qc.QVariant(_qg.QColor(_qc.Qt.darkGray))
            #else:
            #return QVariant(QColor(Qt.darkBlue))
        elif role == _qc.Qt.ToolTipRole:
            if column == NAME:
                return _qc.QVariant("<font color='#FF0000'>" + dato.name + "</font>")
            elif column == CODE:
                return _qc.QVariant(dato.code)
        return _qc.QVariant()

    def headerData(self, section, orientation, role=_qc.Qt.DisplayRole):
        if role == _qc.Qt.TextAlignmentRole:
            if orientation == _qc.Qt.Horizontal:
                return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
        if role != _qc.Qt.DisplayRole:
            return _qc.QVariant()
        if orientation == _qc.Qt.Horizontal:
            if section in lstHeader:
                return _qc.QVariant(lstTitHeader[section])
        return _qc.QVariant(int(section + 1))