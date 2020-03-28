'''
Created on 15/03/2015

@author: jorgesaw
'''

import sqlalchemy

#from __future__ import absolute_import, unicode_literals, print_function

from mate.dao.DAOProducto import DAOProducto
from mate.model.models import Product, Category
import unittest


class TestCrudProd(unittest.TestCase):
    
    def setUp(self):
        print("Preparando el contexto")
        self.dao = DAOProducto(False)

    def tearDown(self):
        print("Deconstruyendo el contexto.")
        self.dao = None
        
    def testCrudProd(self):
        rubroYerba = Category.data2Object(['Yerba Mate',])
        rubroMasitas = Category.data2Object(['Masitas',])

        for rubro in (rubroYerba, rubroMasitas):
            id = self.dao.insert(rubro)
            self.assertTrue(id > 0)
        
if __name__ == "__main__":
    unittest.main()