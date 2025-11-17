class Punto:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    
    def mostrarPunto(self):
        print("El punto es: ", self.X, ", ", self.Y)

class Triangulo:
    def __init__(self, v1, v2, v3):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
    
    def mostrarVer(self):
        self.V1.mostrarPunto()
        self.V2.mostrarPunto()
        self.V3.mostrarPunto()

p1 = Punto(4, 6)
p2 = Punto(4, 6)

p1.X = 6
p2 = p1
p2.mostrarPunto()
p1.mostrarPunto()

p3 = Punto(3, 4)
p4 = Punto(6, 9)
p5 = Punto(9, 2)

trian = Triangulo(p3, p4, p5)
print("Imprimo a continuación los vértices del triángulo: ")
trian.mostrarVer()
