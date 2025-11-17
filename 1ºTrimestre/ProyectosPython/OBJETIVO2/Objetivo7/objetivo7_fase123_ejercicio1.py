# Daniel García Méndez

# Creo una clase vehículo con los sus atributos
class Vehiculo():
    def __init__(self, marcaVehiculo, velocidadInicial):
        self.marcaVehiculo = marcaVehiculo
        self.velocidadInicial = velocidadInicial


# Las funciones acelerar, desacelerar, asignan un nuevo valor a la velocidad.
    def acelerar(self,velocidad):
        self.velocidadInicial=velocidad

    def desacelerar(self,velocidad):
        self.velocidadInicial=velocidad


# Muestra la velocidad del vehículo.
    def mostrar_velocidad(self):
        print("Velocidad actual: ",self.velocidadInicial)

# Se inicia una herencia y se inicializan los atributos de vehículo y luego coche.
class Coche(Vehiculo):
    def __init__(self, marcaVehiculo, velocidadInicial, bocina="¡tuuut!"):
        super().__init__(marcaVehiculo, velocidadInicial)

        self.bocina = bocina


# Imprime la cadena del claxon.
    def tocar_claxon(self):
        print(self.bocina)

coche1 = Coche("Toyota", 0,"ppp")
coche1.acelerar(80)
coche1.mostrar_velocidad()     # Salida: 80
coche1.desacelerar(30)
coche1.mostrar_velocidad()     # Salida: 30
coche1.tocar_claxon()          # Salida: ¡tuuut!
print(coche1.marcaVehiculo)