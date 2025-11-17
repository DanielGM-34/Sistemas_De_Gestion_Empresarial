# Daniel García Méndez 2ºDAM

# Clase Autor: el autor tendrá un nombre y apellidos.
class Autor:
    def __init__(self, nombre, apellidos):
        self.Nombre = nombre
        self.Apellidos = apellidos

    def MostrarAutor(self):
        print("El autor es:", self.Nombre, self.Apellidos)

# Clase Libro: tendrá un título, ISBN y autor
class Libro:
    def __init__(self, titulo, isbn, autor):
        self.Titulo = titulo
        self.ISBN = isbn
        self.Autor = autor

    def muestraTitulo(self):
        return self.Titulo

    def MostrarLibro(self):
        print("Título:", self.Titulo)
        print("ISBN:", self.ISBN)
        self.Autor.MostrarAutor()

    def asociarAutorLibro(self, autorAsocio):
        self.Autor = autorAsocio

# Clase Biblioteca: puse una colección de libros vacía inicializada en el constructor, no le paso ningún parámetro a la biblioteca.
class Biblioteca:
    def __init__(self):
        self.ListaLibros = []

    def agregar_libro(self, libro):
        self.ListaLibros.append(libro)

    def mostrar_libros(self):
        if len(self.ListaLibros) == 0:
            print("La biblioteca no tiene libros.")
        else:
            for libro in self.ListaLibros:
                print("\n------ Libro ------")
                libro.MostrarLibro()
                print("\n-------------------")

    def BorrarLibro(self, titulo):
        indice = -1
        contador = 0
        longitudListaLibros=len(self.ListaLibros)
        while contador < longitudListaLibros:
            if self.ListaLibros[contador].muestraTitulo().lower() == titulo.lower():
                indice = contador
            contador = contador + 1
        if indice != -1:
            del self.ListaLibros[indice]
            print("Libro", titulo, "eliminado. \n")
        else:
            print("No se encontró el libro con título:", titulo,"\n")

# Muestra el número de libros
    def NumeroLibros(self):
        return len(self.ListaLibros)

# Función para mostrar las opciones del menú 
def muestraOpcionesMenu():
    print("Menu")
    print("1) Añadir libro a la biblioteca")
    print("2) Mostrar biblioteca")
    print("3) Borrar libro")
    print("4) ¿Número de libros?")
    print("5) Salir")

# Función para que el usuario elija la opción.
def eligeOpcionesMenu():
    bibliotecaLibrillos = Biblioteca()
    salir = True
    while salir:
        muestraOpcionesMenu()
        op = input("Seleccione opción: ")
        if op.isdigit():
            op = int(op)
            if op == 1:
                tituloLibro = input("Introduzca el título del libro: ")
                isbn = input("Introduzca el ISBN del libro: ")
                nombreAutor = input("Introduzca el nombre del autor: ")
                apellidoAutor = input("Introduzca el apellido del autor: ")
                autor = Autor(nombreAutor, apellidoAutor)
                libro = Libro(tituloLibro, isbn, autor)
                bibliotecaLibrillos.agregar_libro(libro)
                print("Libro añadido correctamente.")
            elif op == 2:
                bibliotecaLibrillos.mostrar_libros()
            elif op == 3:
                tituloAEliminar = input("Introduce el nombre del libro a eliminar: ")
                bibliotecaLibrillos.BorrarLibro(tituloAEliminar)
            elif op == 4:
                print("El número de libros en la biblioteca es:", bibliotecaLibrillos.NumeroLibros())
            elif op == 5:
                print("Saliendo del programa...")
                salir = False
            else:
                print("Opción no válida. Intenta de nuevo.")
        else:
            print("Por favor, introduce un número válido.")

# Ejecutar todo el menú.
eligeOpcionesMenu()
