'''
Created on 15/03/2015

@author: jorgesaw
'''

from mate.core.dao.DAOAlchemy import DAOAlchemy
from mate.model.listmodel import listService
from mate.model.models import Category
import mate.model.mapper.mapeador
import unittest

#from __future__ import absolute_import, unicode_literals, print_function



class TestListModel(unittest.TestCase):
    
    def setUp(self):
        print("Preparando el contexto")
        self.dao = DAOAlchemy(False)

    def tearDown(self):
        print("Deconstruyendo el contexto.")
        self.dao = None
        
    def testListData(self):
        rubroYerba = Category.data2Object(['Yerba Mate',])
        rubroMasitas = Category.data2Object(['Masitas',])
        
        for rubro in (rubroYerba, rubroMasitas):
            id = self.dao.insert(rubro)
            self.assertTrue(id > 0, "No se pudieron guardar los rubros.")
        
        modeloDatos = listService.getListaDatos(Category)
        
        self.assertTrue(len(modeloDatos.datos) >= 2)
        
if __name__ == "__main__":
    unittest.main()