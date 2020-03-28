'''
Created on 15/03/2015

@author: jorgesaw
'''

import sqlalchemy
import mate.model.mapper.mapeador

#from __future__ import absolute_import, unicode_literals, print_function

from mate.dao.DAOProducto import DAOProducto
from mate.model.models import Product, Category, Item, Bill
import unittest


class TestCreaFactura(unittest.TestCase):
    
    def setUp(self):
        print("Preparando el contexto")
        self.dao = DAOProducto(False)

    def tearDown(self):
        print("Deconstruyendo el contexto.")
        self.dao = None
        
    def testCrudProd(self):
        fo = Bill()
        yerba = self.dao.get(1, Product)
        
        item1 = Item(yerba, 3)
        
        print('{0}|{1}|{2:.2f}'.format(item1.product, item1.quantity, item1.calculate()))
        fo.addItem(item1)
        
        masita = self.dao.get(2, Product)
        item2 = Item(masita)
        print('{0}|{1}|{2:.2f}'.format(item2.product, item2.quantity, item2.calculate()))
        
        fo.addItem(item2)
        
        fo.calculate()
        fo.close()
        print('TOTAL: {:.2f}'.format(fo.total))
        
        id = self.dao.insert(fo)
        self.assertTrue(id > 0)
        
if __name__ == "__main__":
    unittest.main()