class PuntoPublico:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    
    def mostrarPunto(self):
        print("El punto es: ", self.X, ", ", self.Y)

class PuntoPrivado:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

publico = PuntoPublico(4, 8)
privado = PuntoPrivado(4, 4)

print("valores publicos: ", publico.X, publico.Y)
print("valores privados: ", privado.getX(), ",", privado.getY())
privado.setX(9)
print("valores privados: ", privado.getX(), ",", privado.getY())
