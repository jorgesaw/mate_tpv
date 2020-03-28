#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 06/07/2014

@author: jorgesaw
'''

import sys
sys.path.append('./')

class ModeloDatos(object):
    
    MSG_SAVE, MSG_NOT_SAVE, \
    MSG_DELETE, MSG_NOT_DELETE, \
    MSG_EDIT, MSG_NOT_EDIT, \
    MSG_LIST_ERROR, MSG_NOT_LIST, MSG_LIST \
         = range(9) 

    CANT_MSG = 8
    
    def __init__(self):
        self.mensajes = [
            u'Datos guardados con éxito.',
            u'No se pudieron guardar los datos.', 
            u'Datos eliminados con éxito.',
            u'No se pudieron eliminar los datos.', 
            u'Datos actualizados con éxito.',
            u'No se pudieron actualizar los datos.',
            u'Ocurrió un error al listar los datos solicitados.',
            u'No hay datos para mostrar.', 
            u'Datos listados con éxito.'
        ]
        
    def msg(self, tipoMsg):
        return self.mensajes[tipoMsg]