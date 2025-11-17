# Daniel García Méndez 2º DAM
# 1. Evaluar un número
# Pide un número entero y muestra:

# El número es positivo” si es mayor que 0.

# El número es negativo” si es menor que 0.

# “El número es cero” en cualquier otro caso.

n1 = int(input("Introduce un número entero:"))
if n1>0:
    print(n1,"El número es positivo")
elif n1 <0:
    print("El número es negativo", n1)
else:
    print("El número es cero", n1)

# Pide dos números enteros y muestra uno de estos tres mensajes:
n1 = int(input("Introduce el primer número entero:"))
n2 = int(input("Introduce el segundo número entero:"))

# Esta condición mira si n1 es mayor que n2
if n1 > n2:
    print(n1, " es mayor que el segundo ", n2)

# Esta condición mira si n2 es mayor que n1
elif n2 > n1:
    print(n2, " es mayor que el primero ", n1)

# Mira si ambos son iguales.
else:
    print("Ambos son iguales", n1, n2)

# Pide una frase y después pide una palabara que será buscada en la frase.
frase = input("Introduce una frase o palabra: ")
palabra = input("Introduce una palabra para ver si está en la frase: ")

# Usamos 'in' para verificar si la palabra está en la frase
if palabra in frase:
    print("La palabra está en la frase")
else:
    print("La palabra no se encuentra")

# Pedimos un texto y verificamos si empieza por mayúscula, termina con . o no cumple ningún requisito.
texto = input("Introduce una frase o palabra: ")
if texto[0].isupper():
    print("Empieza por minúscula")
elif texto[-1] == ".":
    print("Finaliza el punto")
else:
    print("no empieza con mayúscula ni termina en punto.")



# Se pide una nota que será clasificada en las siguientes clasificaciones

# De 0 a 4 → Insuficiente

# Igual a 5 → Suficiente

# Igual a 6 → Bien

# De 7 a 8 → Notable

# De 9 a 10 → Sobresaliente

nota = int(input("Introduce un número entero: "))
if nota >= 0 and nota <= 4:
    print("Insuficiente")
elif nota == 5:
    print("Suficiente")
elif nota == 6:
    print("Bien")
elif nota >= 7 and nota <= 8:
    print("Notable")
elif nota >= 9 and nota <= 10:
    print("Sobresaliente")
else:
    print("Nota no válida.")

print("\n")