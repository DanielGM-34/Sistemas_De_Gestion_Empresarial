# Daniel García Méndez 2º DAM

# Aquí hago una instancia de varios array con 3 elementos en cada uno
ordenadores = ['Portátil', 'Sobremesa', 'Servidor']
perifericos = ['Ratón', 'Teclado', 'Monitor']
accesorios = ['Funda', 'Altavoces', 'Webcam']

# Creo una instancia de tupla y agrego 3 elementos
precios = (750,1200,2200)

# Imprimo la tupla de precios
print(precios)

# Creo un diccionario con un nombre como valor y una llave como array.
catalogo = {
    'Ordenadores': ordenadores,
    'Periféricos': perifericos,
    'Accesorios': accesorios,
}

# Imprimo las diferentes listas
print(ordenadores)
print(perifericos)
print(accesorios)

# Imprimo la tupla de precios y el diccionario de catálogo.
print(precios)
print(catalogo)

# Imprimo el elemento 2 de los periféricos
print("Segundo periférico:", perifericos[1])