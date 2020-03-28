#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 13/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals

from mate.core.gui.Actions import addActions, createAction
from mate.vista import factoria

BCK_IMAGE = ':/fondo_abstracto.png'

MENUS = [u"&Archivo", u"&Productos", u"&Rubros", "&Informes", "&Ventas", "P&unto de venta"]

actSalir = ["&Salir", "Alt+F4", "quit.png", u"Salir de la aplicación", "triggered()"]

MATRIZ_ACTIONS_POR_MENU = [
            [
                ["&Exit", "Alt+F4", "quit.png", u"Exit the app", "triggered()"],  
        
            ], 
            [
                ["&Nuevo...", "", "article.png", u"Nuevo producto", "triggered()"], 
                ["&Mostrar", "", "", u"Mostrar productos", "triggered()"], 
                #["&Limits", "", "", u"Limits", "triggered()"]
            ],
            [
                ["&Nuevo...", "", "article.png", u"Nuevo rubro", "triggered()"], 
                ["&Mostrar", "", "", u"Mostrar rubros", "triggered()"]
            ], 
            [
                ["&Control de stock", "", "", u"Control de stock", "triggered()"],  
        
            ], 
            [
                ["&Informe de Ventas", "", "", u"Informe de Ventas", "triggered()"],  
        
            ], 
            [
                ["&Mostrar...", "", "", u"Mostrar TPV", "triggered()"],  
        
            ], 
        ]


def getActions(window, lst_var_actions, lstSlot, matriz=MATRIZ_ACTIONS_POR_MENU):
    #uAgrega las acciones definidas en factoria.
    matriz_actions = []
    i = factoria.APP_EXIT # Inicia con 0
    
    for menu in matriz:
        lstActions = []
        
        #print('LST_ACTIONS:', len(lstSlot))
        
        for action in menu:
            #print('I:', i)
            lst_var_actions[i] = createAction (window, window.tr(action[0]), 
                                    slot=lstSlot[i], 
                                    shortcut=action[1], icon=action[2], 
                                    tip=window.tr(action[3]), 
                                    signal=action[4]
                                    )
            lst_var_actions[i].setData(i)
            
            lstActions.append(lst_var_actions[i])
            i +=1
            
        matriz_actions.append(lstActions)
    
    return matriz_actions
    
def getMenus(window, lstMenus, matrizActions, menus=MENUS):
    for menu_string, menu_var, lstActions in zip(menus, lstMenus, matrizActions):
        menu_var = window.menuBar().addMenu(window.tr(menu_string))
        
        addActions(window, menu_var, lstActions)