# Daniel García Méndez 2º DAM

# Pido al usuario una frase y uso \n para el salto de línea
frase = input("Introduce una frase o palabra:")
print("\n")

print("--- FORMATO DEL TEXTO ---")
# Uso capitalize para 
print("Capitalizada:", frase.capitalize())
print("Mayúsculas:", frase.upper())
print("Minúsculas:", frase.lower())
print("Invertida:", frase.swapcase())
print("\n")
print("--- ANÁLISIS DEL CONTENIDO ---")
print("¿Solo letras?:", frase.isalpha())
print("¿Solo números?:", frase.isdigit())
print("¿Está en minúsculas?:", frase.islower())
print("¿Está en mayúsculas?:", frase.isupper())

print("--- LONGITUD ---")
print("Número total de caracteres:", len(frase))