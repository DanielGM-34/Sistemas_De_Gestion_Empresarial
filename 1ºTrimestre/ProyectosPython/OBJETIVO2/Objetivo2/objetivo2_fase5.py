# Daniel García Méndez 2º DAM

# Pido al usuario una frase y uso \n para el salto de línea
frase = input("Introduce una frase o palabra:")
print("\n")

print("--- FORMATO DEL TEXTO ---")
# Muestra la frase en diferentes formatos: capitalizada, mayúsculas, minúsculas e invertida
print("Capitalizada:", frase.capitalize())
print("Mayúsculas:", frase.upper())
print("Minúsculas:", frase.lower())
print("Invertida:", frase.swapcase())
print("\n")

# Analiza el contenido de la frase: si contiene solo letras, números, si está en mayúsculas o minúsculas
print("--- ANÁLISIS DEL CONTENIDO ---")
print("¿Solo letras?:", frase.isalpha())
print("¿Solo números?:", frase.isdigit())
print("¿Está en minúsculas?:", frase.islower())
print("¿Está en mayúsculas?:", frase.isupper())
print("\n")

# Calcula la longitud total y la cantidad de caracteres reales sin contar espacios
print("--- LONGITUD ---")
print("Número total de caracteres:", len(frase))
fraseSinEsp=frase.replace(" ","")
print("Caracteres reales (sin espacios)", len((fraseSinEsp)))
print("\n")

# Elimina espacios al inicio, al final y en ambos extremos
print("--- LIMPIEZA ---"),
print("Sin espacios al principio: Python 3.11 / Lenguaje de Programación",frase.lstrip())
print("Sin espacios al final: Python 3.11 / Lenguaje de Programación",frase.rsplit())
print("Sin espacios en ambos lados: Python 3.11 / Lenguaje de Programación", frase.split())
print("\n")

# Permite reemplazar una palabra por otra en la frase
fraseAbuscar = input("Palabra a buscar:")
fraseNueva = input("Palabra nueva:")
fraseNuevaa = frase.replace(fraseAbuscar,fraseNueva)
print("Frase modificada:", fraseNuevaa)
print("\n")

# Muestra el carácter con mayor y menor valor Unicode en la frase modificada
print("--- CARACTERES ---")
print("Carácter mayor", max(fraseNuevaa))
print("Carácter menor", min(fraseNuevaa))
print("\n")

# Divide la frase modificada en una lista de palabras
print("--- LISTA DE PALABRAS ---")
print("Lista:",fraseNuevaa.split())

print("\n")

# Divide la frase modificada por '/' para mostrar la frase sin '/'
print("--- DIVISIÓN POR '/' ---")
print("Resultado del split('/'): ", fraseNuevaa.split("/"))
print("\n")

print("--- ANÁLISIS COMPLETO FINALIZADO ---")