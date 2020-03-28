'''
Created on 14/03/2015

@author: jorgesaw
'''

class Producto():
    def __init__(self, cod, nombre):
        self.cod = cod
        self.nombre = nombre
        
    def __str__(self):
        return '{0}-{1}'.format(self.cod, self.nombre)
        
    @staticmethod
    def data2Object(lstDatos):
        prod = Producto(lstDatos[0], lstDatos[1])
        return prod
    
    @staticmethod
    def object2Data(prod):
        return [prod.cod, prod.nombre]
    
    @staticmethod
    def editObject(prod, lstDatos):
        prod.cod = lstDatos[0]
        prod.nombre = lstDatos[1]
    
clase_prod = Producto
p1 = clase_prod.data2Object([1, "Yerba Amanda"])

print p1.__str__()
print Producto.object2Data(p1)