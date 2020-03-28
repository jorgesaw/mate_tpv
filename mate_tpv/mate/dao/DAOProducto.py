#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from mate.core.dao.DAOAlchemy import DAOAlchemy
from mate.model.models import Product
import sqlalchemy

class DAOProducto(DAOAlchemy):

    def __init__(self, cerrarSesion=True):
        super(DAOProducto, self).__init__(cerrarSesion)
        
    def getAllByStockIdealMin(self):
        """Busca todos los productos cuyo stock sea menor que el stock ideal.
        
        :return: Devuelve una tupla con objetos Product.
        :rtype: tuple[tipo]"""
        objects = []
        try:
            objects = self.session.query(Product).filter(\
                            Product.stock < Product.ideal_stock).\
                            order_by(Product.stock).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects
        
    def get(self, code, tipo):
        u"""Busca un objeto en la base de datos con el código ingresado.

        :param code: Representa el identificador del objeto.
        :param tipo: No es necesario porque el tipo es Product. Se mantiene
            por cuestiones de compatibilidad con el código ya existente.
        
        :return: Devuelve un producto con el parámetro code, sino devuelve None."""
        prod = None
        try:
            prod = self.session.query(Product).filter(Product.code == code).one()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return prod