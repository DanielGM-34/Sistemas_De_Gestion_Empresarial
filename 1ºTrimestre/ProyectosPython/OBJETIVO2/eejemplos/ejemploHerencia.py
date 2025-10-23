class Persona():
    def __init__(self,nombre="Anonimo", edad=0):
        self.nombre=nombre
        self.edad=edad


p1 = Persona()  #Nombre anónimo con edad 0
p2=Persona("Lucia") #Nombre Lucía con edad 0
p3=Persona("Pepe",20) #Nombre Pepe con edad 20
print(p1.nombre)
print(p2.nombre)
print(p2.edad)
print(p3.edad)