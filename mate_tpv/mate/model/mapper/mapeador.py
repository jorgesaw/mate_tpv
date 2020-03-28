#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 14/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from mate.model.models import Bill, Category, Item, Product, Licencia, TypePay
from sqlalchemy import Column, Integer, String, Float, Date, Boolean, Time, \
    ForeignKey, Table, MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship, backref

    


meta = MetaData()

categoriaTabla = Table('CATEGORIES', meta,
    Column('id_category', Integer, primary_key=True),
    Column('name', String(50), nullable=False),
    mysql_engine='InnoDB'
)

mapper(Category, categoriaTabla, properties={
    'id': categoriaTabla.c.id_category,
    'name': categoriaTabla.c.name,
    'products': relationship(Product, 
                             lazy="dynamic",
                             cascade="all, delete-orphan")
})

productoTabla = Table("PRODUCTS", meta,
    Column('id_product', Integer, primary_key=True),
    Column('code', String(13), unique=True),
    Column('name', String(50), nullable=False),
    Column('external_code', String(25), nullable=True, unique=True),
    Column('price', Float, nullable=False),
    Column('buy_price', Float, nullable=False),
    Column('stock', Integer, nullable=False),
    Column('min_stock', Integer, nullable=False),
    Column('ideal_stock', Integer, nullable=False),
    Column('description', String(50), nullable=True),
    Column('id_category', Integer, 
           ForeignKey('CATEGORIES.id_category', ondelete="CASCADE", onupdate="CASCADE")), 
    mysql_engine='InnoDB'
)
mapper(Product, productoTabla, properties={
    'id': productoTabla.c.id_product,
    'code': productoTabla.c.code,
    'name': productoTabla.c.name,
    'external_code': productoTabla.c.external_code, 
    'price': productoTabla.c.price,
    'buy_price': productoTabla.c.buy_price,
    'stock': productoTabla.c.stock,
    'min_stock': productoTabla.c.min_stock,
    'ideal_stock': productoTabla.c.ideal_stock, 
    'description': productoTabla.c.description, 
    'category': relationship(Category,
                         backref='CATEGORIES',
                         lazy="joined")
})

itemTabla = Table("ITEMS", meta,
    Column('id', Integer, primary_key=True),
    Column('price', Float, nullable=False),
    Column('unit_price', Float, nullable=False),
    Column('quantity', Integer, nullable=False),
    Column('code_prod', Integer, ForeignKey('PRODUCTS.code')), 
    Column('number', Integer, ForeignKey('BILLS.number')),
    mysql_engine='InnoDB'
)
mapper(Item, itemTabla, properties={
    'id': itemTabla.c.id,
    'price': itemTabla.c.price, 
    'unit_price': itemTabla.c.unit_price, 
    'quantity': itemTabla.c.quantity,
    'product': relationship(Product,
                         uselist=False),
    'bill': relationship(Bill,
                         backref='BILLS',
                         lazy="joined"), 
})

billTabla = Table("BILLS", meta, 
    #Column('id', Integer, primary_key=True),              
    #Column('number', Integer, unique=True),
    Column('number', Integer, primary_key=True),
    Column('date', Date, nullable=False),
    Column('subtotal', Float),
    Column('total', Float),
    mysql_engine='InnoDB'
)

mapper(Bill, billTabla, properties={
    #'id': billTabla.c.id,
    'id': billTabla.c.number,
    #'number': billTabla.c.number,
    'date': billTabla.c.date,
    'subtotal': billTabla.c.subtotal,
    'total': billTabla.c.total,
    'items': relationship(Item, 
                lazy="dynamic",
                cascade="all, delete-orphan")
})

licenciaTabla = Table("LICENCIAS", meta, 
    Column('id', Integer, primary_key=True),              
    Column('cant', Integer, nullable=False),
    mysql_engine='InnoDB'
)

mapper(Licencia, licenciaTabla, properties={
    'id': licenciaTabla.c.id,
    'cant': licenciaTabla.c.cant,
})

def main():
    import mate.core.dao.config as config
    
    engine = create_engine(config.cargarConfig())
    meta.drop_all(engine)
    meta.create_all(engine)
    
    print(u"Se crearon las tablas con éxito")

if __name__ == '__main__':
    main()