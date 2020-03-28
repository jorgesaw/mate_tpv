'''
Created on 15/03/2015

@author: jorgesaw
'''

import sqlalchemy
import mate.model.mapper.mapeador

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
        
        prods = [['Yerba Playadito 1kg.', '29226623', None, 43.72, 
             131.37, 10,  10, rubroYerba, 4, 8, 'Yerba Playadito 1kg.'
             ], ['Masitas Quacker', '29226637', None, 22.12, 
             11.2337, 10,  10, rubroMasitas, 4, 8, 'Masitas Quacker'
             ]]
        
        lstProductos = []
        for lstDatos in prods:
            prod = Product.data2Object(lstDatos)
            lstProductos.append(prod)

        for prod in lstProductos:
            id = self.dao.insert(prod)
            self.assertTrue(id > 0)
        
if __name__ == "__main__":
    unittest.main()