#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from mate.core.dao.DAOAlchemy import DAOAlchemy
from mate.model.models import Bill
import sqlalchemy

class DAOBill(DAOAlchemy):

    def __init__(self, cerrarSesion=True):
        super(DAOBill, self).__init__(cerrarSesion)
        
    def getVentasPorFecha(self, fecha):
        ventas = None
        try:
            ventas = self.session.query(Bill).filter(Bill.date== fecha).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return ventas