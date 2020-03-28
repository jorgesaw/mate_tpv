#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 06/07/2014

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from mate.core.model.genericmodel.genericModel import Model
from mate.core.model.modelotable.modeloTabla import ModeloTabla
from mate.core.util import util
from mate.dao.DAOBill import DAOBill
from mate.dao.DAOCategory import DAOCategory
from mate.dao.DAOProducto import DAOProducto
from mate.model.modelControlStock import ModelControlStock
from mate.model.modelInfDiarioVentas import ModelInfDiarioVentas
from mate.model.modelTPV import ModelTPV
from mate.model.models import Product, Category, Item, Bill
from mate.model.modeltable.modelTableTPV import ModelTableTPV
from mate.model.modeltable.modeldatatable.mdtCategory import \
    ModeloDatosTablaCategory
from mate.model.modeltable.modeldatatable.mdtInformeStock import MdtInformeStock
from mate.model.modeltable.modeldatatable.mdtMateTPVGui import MDTMateTPVGui
from mate.model.modeltable.modeldatatable.mdtProduct import \
    ModeloDatosTablaProduct
from mate.vista.gui.crud.crudCategoryDlg import CrudCategoryDlg
from mate.vista.gui.crud.crudProductDlg import CrudProductDlg
from mate.vista.gui.dlg.ControlStockDlg import ControlStockDlg
from mate.vista.gui.dlg.InformeDiarioVentasDlg import InformeDiarioVentasDlg
from mate.vista.gui.dlg.NewCategoryDlg import NewCategoryDlg
from mate.vista.gui.dlg.NewProductDlg import NewProductDlg
from mate.vista.main.MainWindowMateTPV import MainWindowMateTPV

#LIMITS_SHOW, \
APP_EXIT, ARTICLE_NEW, ARTICLE_SHOW, \
    ITEMS_NEW, ITEMS_SHOW, STOCK_CONTROL, VENTAS_INFORME_DIARIO, \
    GUI_MATE_TPV = range(8)

LST_GENERIC_WINDOW = [APP_EXIT, 
                      ARTICLE_NEW, ARTICLE_SHOW, #LIMITS_SHOW, 
                      ITEMS_NEW, ITEMS_SHOW, 
                      STOCK_CONTROL, VENTAS_INFORME_DIARIO, 
                      GUI_MATE_TPV]


def getClaseModelo(path, clase):
    import importlib
    cl = path + clase
    return getattr(importlib.import_module(cl[:- (len(cl.split('.')[-1])+1)]), 
                   cl.split('.')[-1])
    #return util.import_class(path + clase)

PATH_CRUD = 'mate.vista.gui.crud.'
PATH_DLG = 'mate.vista.gui.dlg.'
PATH_MODELS = 'mate.model.models.'
PATH_DAO = 'mate.dao.'
PATH_CRUD_MODELO = 'mate.core.model.genericmodel.genericModel.'
PATH_CRUD_MODELO_TABLA = 'mate.core.model.modelotable.modeloTabla.'
PATH_CRUD_MODELO_DATOS_TABLA = 'mate.model.modeltable.modeldatatable.'

PATH_CRUD_MODELO_ESPECIF = 'mate.model.'
PATH_CRUD_MODELO_TABLE_ESPECIF = 'mate.model.modeltable.'
PATH_GUI_TPV = 'mate.vista.main.'

GUI_NAME = {ARTICLE_SHOW: 'CrudProductDlg',}
MODEL_NAMES = {ARTICLE_NEW: 'Product', 
               ARTICLE_SHOW: 'Product'}

DIC_LIST_CLASES = {
    ARTICLE_NEW: {'clase_modelo': Product,#getClaseModelo(PATH_MODELS, 'Product'), 
                   'dao': DAOProducto,#getClaseModelo(PATH_DAO + 'DAOProducto.', 'DAOProducto'), 
                   'modelo': Model,#getClaseModelo(PATH_CRUD_MODELO, 'Model'),
                   'modelo_datos_tabla': None,
                   'modelo_tabla': None,
                   'ventana': NewProductDlg,#getClaseModelo(PATH_DLG + 'NewProductDlg.', 'NewProductDlg')
    }, 
    ARTICLE_SHOW: {'clase_modelo': Product,#getClaseModelo(PATH_MODELS, 'Product'), 
                   'dao': DAOProducto,#getClaseModelo(PATH_DAO + 'DAOProducto.', 'DAOProducto'), 
                   'modelo': Model,#getClaseModelo(PATH_CRUD_MODELO, 'Model'),
                   'modelo_datos_tabla': ModeloDatosTablaProduct, #getClaseModelo(PATH_CRUD_MODELO_DATOS_TABLA + 'mdtProduct.', 
                                                        #'ModeloDatosTablaProduct'),
                   'modelo_tabla': ModeloTabla,#getClaseModelo(PATH_CRUD_MODELO_TABLA, 'ModeloTabla'),
                   'ventana': CrudProductDlg,#getClaseModelo(PATH_CRUD + 'crudProductDlg.', 'CrudProductDlg')
    }, 
    ITEMS_NEW: {'clase_modelo': Category,#getClaseModelo(PATH_MODELS, 'Category'), 
                   'dao': DAOCategory,#getClaseModelo(PATH_DAO + 'DAOCategory.', 'DAOCategory'), 
                   'modelo': Model,#getClaseModelo(PATH_CRUD_MODELO, 'Model'),
                   'modelo_datos_tabla': None,
                   'modelo_tabla': None,
                   'ventana': NewCategoryDlg,#getClaseModelo(PATH_DLG + 'NewCategoryDlg.', 'NewCategoryDlg')
    }, 
    ITEMS_SHOW: {'clase_modelo': Category,#getClaseModelo(PATH_MODELS, 'Category'), 
                   'dao': DAOCategory,#getClaseModelo(PATH_DAO + 'DAOCategory.', 'DAOCategory'), 
                   'modelo': Model,#getClaseModelo(PATH_CRUD_MODELO, 'Model'),
                   'modelo_datos_tabla': ModeloDatosTablaCategory,#getClaseModelo(PATH_CRUD_MODELO_DATOS_TABLA + 'mdtCategory.', 
                                                        #'ModeloDatosTablaCategory'),
                   'modelo_tabla': ModeloTabla,#getClaseModelo(PATH_CRUD_MODELO_TABLA, 'ModeloTabla'),
                   'ventana': CrudCategoryDlg,#getClaseModelo(PATH_CRUD + 'crudCategoryDlg.', 'CrudCategoryDlg')
    },
    STOCK_CONTROL: {'clase_modelo': Product,#getClaseModelo(PATH_MODELS, 'Product'), 
                   'dao': DAOProducto,#getClaseModelo(PATH_DAO + 'DAOProducto.', 'DAOProducto'), 
                   'modelo': ModelControlStock,#getClaseModelo(PATH_CRUD_MODELO_ESPECIF + 'modelControlStock.', 
                                                        #'ModelControlStock'),
                   'modelo_datos_tabla': MdtInformeStock,#getClaseModelo(PATH_CRUD_MODELO_DATOS_TABLA + 'mdtInformeStock.', 
                                                        #'MdtInformeStock'),
                   'modelo_tabla': ModeloTabla,#getClaseModelo(PATH_CRUD_MODELO_TABLA, 'ModeloTabla'),
                   'ventana': ControlStockDlg,#getClaseModelo(PATH_DLG + 'ControlStockDlg.', 'ControlStockDlg')
    },
    GUI_MATE_TPV: {'clase_modelo': Item,#getClaseModelo(PATH_MODELS, 'Item'), 
                   'dao': DAOProducto,#getClaseModelo(PATH_DAO + 'DAOProducto.', 'DAOProducto'), 
                   'modelo': ModelTPV,#getClaseModelo(PATH_CRUD_MODELO_ESPECIF + 'modelTPV.', 'ModelTPV'),
                   'modelo_datos_tabla': MDTMateTPVGui,#getClaseModelo(PATH_CRUD_MODELO_DATOS_TABLA + 'mdtMateTPVGui.', 
                                                        #'MDTMateTPVGui'),
                   'modelo_tabla': ModelTableTPV,#getClaseModelo(PATH_CRUD_MODELO_TABLE_ESPECIF + 'modelTableTPV.', 'ModelTableTPV'),
                   'ventana': MainWindowMateTPV,#getClaseModelo(PATH_GUI_TPV + 'MainWindowMateTPV.', 'MainWindowMateTPV')
    },
    VENTAS_INFORME_DIARIO: {'clase_modelo': Bill,#getClaseModelo(PATH_MODELS, 'Bill'), 
                   'dao': DAOBill,#getClaseModelo(PATH_DAO + 'DAOBill.', 'DAOBill'), 
                   'modelo': ModelInfDiarioVentas,#getClaseModelo(PATH_CRUD_MODELO_ESPECIF + 'modelInfDiarioVentas.', 'ModelInfDiarioVentas'),
                   'modelo_datos_tabla': None,
                   'modelo_tabla': None,
                   'ventana': InformeDiarioVentasDlg,#getClaseModelo(PATH_DLG + 'InformeDiarioVentasDlg.', 'InformeDiarioVentasDlg')
    },
    }

def getDicConfigClases(tipo):
    return DIC_LIST_CLASES.get(tipo)