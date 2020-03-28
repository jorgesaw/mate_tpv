#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 14/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function

from mate.core.util.cadenas import printable
import datetime

#This could be stored in the settings
TAX_MAX = 0.21
TAX_REDUCED = 0.105

NAME, CODE, EXT_CODE, PRICE, BUY_PRICE, STOCK, PACK_UNITS, CATEGORY, \
MIN_STOCK, IDEAL_STOCK, DESCRIPTION = range(11)

class Product(object):
    """Each of the product in the store.
    It can have stock, or not. It can be available or not.
    It just store the properties for each product (like a 'class' for real products)
    """
    name = ""
    code = ""
    #External/Provider code
    external_code = ""
    #sold price, SOLD price
    price = 0.0
    #Price at which is (usually) bought
    buy_price = 0.0
    #Available stock
    stock = 0
    #Units PER (bought) Package (box)
    pack_units = 1
    category = None
    #Minimum stock before warning
    min_stock = 0 
    #Ideal stock before warning
    ideal_stock = 0
    #Constants for type of product, it defines the tax it to be charged (depends on other crappy stuff)
    description = ""

    def __init__(self, code, name="", price=0.0, stock=0):
        self.code = code
        self.setName(name)
        self.price = price
        self.stock = stock

    def __str__(self):
        return "[{0}] ${1:.2f} {2}".format(self.code, self.price, self.name)

    def setName(self, name):
        self.name = printable(name)
        
    @staticmethod
    def data2Object(lstDatos):
        prod = Product(lstDatos[CODE], lstDatos[NAME], 
                       lstDatos[PRICE], lstDatos[STOCK])
        
        prod.external_code = lstDatos[EXT_CODE]
        prod.buy_price = lstDatos[BUY_PRICE]
        prod.pack_units = lstDatos[PACK_UNITS]
        prod.category = lstDatos[CATEGORY]
        prod.min_stock = lstDatos[MIN_STOCK]
        prod.ideal_stock = lstDatos[IDEAL_STOCK]
        prod.description = lstDatos[DESCRIPTION]
        
        return prod

    @staticmethod
    def object2Data(prod):
        return [prod.name, prod.code, prod.external_code, prod.price, 
                prod.buy_price, prod.stock, prod.pack_units, prod.category, 
                prod.min_stock, prod.ideal_stock, prod.description]
        
    @staticmethod
    def editObject(prod, lstDatos):
        prod.code = lstDatos[CODE]
        prod.name = lstDatos[NAME] 
        prod.price = lstDatos[PRICE]
        prod.stock = lstDatos[STOCK]
        
        prod.external_code = lstDatos[EXT_CODE]
        prod.buy_price = lstDatos[BUY_PRICE]
        prod.pack_units = lstDatos[PACK_UNITS]
        prod.category = lstDatos[CATEGORY]
        prod.min_stock = lstDatos[MIN_STOCK]
        prod.ideal_stock = lstDatos[IDEAL_STOCK]
        prod.description = lstDatos[DESCRIPTION]
        
    @staticmethod
    def type():
        return Product

QUANT, PRODUCT = range(2)

class Item(object):
    """Represents an item in a bill.
    it is related to a product, BUT for historical reasons (ask nande)
    the product data needed to form a bill, must be duplicated and stored SEPARATEDLY"""
    product = None
    #CALCULATED price per unit, including markup but without tax
    unit_price = 0.0
    #CALCULATED total price with tax (calculated with item.calculate())
    price = 0.0
    quantity = 1
    
    def __init__(self, product=None, quant=1):
        if product:
            self.setProduct(product)
        self.setQuantity(quant)

    def setProduct(self, product):
        self.product = product
        #this values need duplication because the client might want to change the default values
        #also to allow the use of generic products

        self.unit_price = round(product.price, 2)

    def setQuantity(self, quant):
            self.quantity = quant

    def calculate(self):
        """Calculates the total
        and other values.
        self.price is the total price of the item (including tax)
        self.tax_total is the total ammount of tax in the price (not a percentaje)
        self.net_price is the total price without tax
        """
        #round( ,2) rounds the item to 2 digits, is needed because printers dont process more then 4 digits
        #self.unit_price = round(self.base_price, 2)
        self.price = self.unit_price * self.quantity
        
        return self.price
    
    @staticmethod
    def data2Object(lstDatos):
        item = Item(lstDatos[PRODUCT], lstDatos[QUANT])
        return item
    
    @staticmethod
    def object2Data(item):
        return [item.product, item.quantity]
    
    @staticmethod
    def editObject(item, lstDatos):
        item.product = lstDatos[PRODUCT]
        item.quantity = lstDatos[QUANT]
        
    @staticmethod
    def type():
        return Item
    
NAME = range(1)   
ID_CATEGORY_TARJ_TEL = 1
ID_CATEGORY_TARJ_COL = 2
class Category(object):
    name = ""
    def __init__(self, name=""):
        self.name = name
        
    def __str__(self):
        return '{}'.format(self.name)
        
    @staticmethod
    def data2Object(lstDatos):
        category = Category(lstDatos[NAME])
        return category
    
    @staticmethod
    def object2Data(category):
        return [category.name]
    
    @staticmethod
    def editObject(category, lstDatos):
        category.name = lstDatos[NAME]
        
    @staticmethod
    def type():
        return Category

NAME, MARKUP = range(2)
class TypePay(object):
    name = ''
    markup = 0.0
    def __init__(self, name, markup=0.0):
        self.name = name
        self.markup = markup

    def __str__(self):
        return "{0} - {1}" % (self.name, self.markup*100)
    
    @staticmethod
    def data2Object(lstDatos):
        typePay = TypePay(lstDatos[NAME], lstDatos[MARKUP])
        return typePay
    
    @staticmethod
    def object2Data(typePay):
        return [typePay.name, typePay.markup]
    
    @staticmethod
    def editObject(typePay, lstDatos):
        typePay.name= lstDatos[NAME]
        typePay.markup = lstDatos[MARKUP]
        
    @staticmethod
    def type():
        return TypePay


class Bill(object):
    """Bill. Factura. Ticket.
    """
    #Constants for the bill type
    TYPE_A = 0
    TYPE_B = 1
    TYPE_C = 2
    TYPE_NOTA_CRED_A = 3
    TYPE_NOTA_CRED_B = 4
    TYPE_NOTA_DEB_A = 5
    TYPE_NOTA_DEB_B = 6
    TYPE_NAMES = (
            'A', 'B', 'C', 'Nota de Crédito A', 'Nota de Crédito B', 'Nota de Débito A', 'Nota de Débito B'
    )

    number = 0
    date = 0
    total = 0.0
    subtotal = 0.0
    btype = 0
    closed = False
    #used as a key
    time = 0
    def __init__(self):
        self.date = datetime.datetime.now()
        self.items = []
        self.setTypeBill(Bill.TYPE_A)

    def setTypeBill(self, tb):
        self.btype = tb

    def calculate(self):
        """Recalculate the values for the bill, and sets the values in each variable.
        It can be slow so call it only if it has changed"""
        self.subtotal = 0.0
        self.total = 0.0
        for i in self.items:
            i.calculate()
            self.total += i.price
        self.subtotal = self.total
    
    def copy(self):
        copy = Bill()
        #copy of the rest of bill class
        copy.btype = self.btype
        #copy.client = self.client
        #copy.markup = self.markup
        #copy.ptype = self.ptype
        #copy.user = self.user
        #copy.ptype = self.ptype
        #is easier to just copy this attributes than recalculating stuff
        copy.subtotal = self.subtotal
        copy.total = self.total
        #copy.tax = self.tax

        for i in self.items:
            item = Item()
            #copy ALL item properties! :D!
            #here is safer to copy attributes instead of recalculating, because a bill could have a modified price/description
            #that's the reason we have redundant attributes in the item after all
            #item.base_price = i.base_price
            #item.client_exempt = i.client_exempt
            #item.description = i.description
            #item.markup = i.markup
            #item.net_price = i.net_price
            item.price = i.price
            #copy the product to the new instance
            #product is an object that is safe to copy (that way we can do reports)
            item.product = i.product
            item.quantity = i.quantity
            #item.reducible = i.reducible
            #item.tax_type = i.tax_type
            #item.tax = i.tax
            #item.tax_total = i.tax_total
            item.unit_price = i.unit_price
            copy.items.append(item)
        return copy

    def close(self):
        """Closes the bill.
        ADDS THE BILL TO THE DATABASE
        Reduces the stock, sets the bill date
        and add it to the bill list
        if the bill is already closed, it does nothing.
        Notice this is pretty destructive and has side-effects, so be careful when using it
        """
        #TODO disable all functions if the bill is closed
        if self.closed:
            return False

        #import banta.db
        self.closed = True
        self.date = datetime.datetime.now()
        #we will be using time as a key
        #self.time = banta.utils.dateTimeToInt(self.date)
        #calculate if we will be adding or substracting the stock
        #this is a little trick to impact lowly on the code
        if self.btype in (self.TYPE_NOTA_CRED_A, self.TYPE_NOTA_CRED_B):
            sign = 1
        else :
            sign = -1
        #let's reduce the stock :D
        for item in self.items:
            prod = item.product
            prod.stock += sign* item.quantity
            #TODO ask the client if adding a "Move" for each returned item would be a good feature
        #check that there's not another bill with the same key (should not happen unless using several clients at once)
        #though that's not possible YET, let's be prepared (also if some stupid person changes the system date)

        #while (self.time in banta.db.DB.bills):
        #    self.time += 1

        #banta.db.DB.bills[self.time] = self
        return True

    def addItem(self, item):
        """Adds an item to the bill.
        Returns True if ok.
        If the item is already on the bill, or there's an error it returns False."""

        if item in self.items:
            return False

        self.items.append(item)
        return True
        #DB.commit() #DONT COMMIT UNTIL THE BILL IS PRINTED (important also if we ever make a network shared-db version)

    def delItem(self, i):
        del self.items[i]

    @staticmethod
    def data2Object(lstDatos):
        bill = Bill()
        return bill
    
    @staticmethod
    def object2Data(bill):
        return [bill.number, bill.date, bill.time, 
                bill.subtotal, bill.total, bill.items]
    
    @staticmethod
    def editObject(bill, lstDatos):
        pass
    
    @staticmethod
    def type():
        return Bill
    
class Licencia(object):
    def __init(self, cant=1):
        self.cant = cant
        