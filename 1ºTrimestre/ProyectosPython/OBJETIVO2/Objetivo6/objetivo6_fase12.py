class Autor:
    def __init__(self, nombre, apellidos):
        self.Nombre = nombre
        self.Apellidos = apellidos

    def MostrarAutor(self):
        print("El autor es:", self.Nombre, self.Apellidos)

class Libro:
    def __init__(self, titulo, isbn, autor):
        self.Titulo = titulo
        self.ISBN = isbn
        self.Autor = autor

    def MostrarLibro(self):
        print("Título:", self.Titulo)
        print("ISBN:", self.ISBN)
        self.Autor.MostrarAutor()
    
    def asociarAutorLibro(self, autorAsocio):
        self.Autor = autorAsocio

class Biblioteca:
    def __init__(self):
        self.ListaLibros = []  # Lista vacía para almacenar objetos de tipo Libro

    def agregar_libro(self, libro):
        self.ListaLibros.append(libro)

    def mostrar_libros(self):
        if not self.ListaLibros:
            print("La biblioteca no tiene libros.")
        else:
            for libro in self.ListaLibros:
                libro.MostrarLibro()



def MostrarMenu():
    continuar=True
    biblio = Biblioteca()
    while(continuar):  
        print("1) Agregar libro: ")
        print("2) Mostrar biblioteca: ")
        print("3) Borrar libro de biblioteca: ")
        print("4) Mostrar menú de libros: ")
        print("5) Salir")

        op = input(int("Elige una opcion: "))
        if op ==1:
            tituloLibro = input("Introduce el título del libro: ")
            isbn= input("Introduce el ISBN del libro: ")
            autor= input("Introduce  autor del libro: ")
            apllAutor= input("Introduce apellido del autor del libro: ")
            autor1 = Autor(autor,apllAutor)
            libro1 = Libro(tituloLibro,isbn,autor1)
            



