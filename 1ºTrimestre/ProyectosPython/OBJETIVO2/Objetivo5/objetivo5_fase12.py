import math

def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def potencia(n1, n2):
    return n1 ** n2

def raiz_cuadrada(n1):
    return math.sqrt(n1)

def modulo(n1, n2):
    return n1 % n2

def menu():
    continuar = True
    while continuar:
        print("=========================")    
        print("CALCULADORA AVANZADA")
        print("=========================")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Operaciones avanzadas")
        print("6) Salir")
        
        opcion = int(input("Elige una opción: "))

        if opcion in [1, 2, 3, 4]:
                n1 = float(input("Introduce un numerín: "))
                n2 = float(input("Introduce el segundo numerín: "))
                if opcion == 1:
                     print("Resultado de la suma:", round(sumar(n1, n2), 2))
                
                elif opcion == 2:
                    print("Resultado de la resta:", round(restar(n1, n2), 2))
                
                elif opcion == 3:
                    print("Resultado de la multiplicación:", round(multiplicar(n1, n2), 2))
                
                elif opcion == 4:
                    if n2 == 0:
                        print("Error: No se puede dividir entre cero.")
                    else:
                        print("Resultado de la división:", round(divide(n1, n2), 2))

        elif opcion == 5:
            print("a) Potencia")
            print("b) Módulo")
            print("c) Raíz cuadrada")
            print("d) Volver")
            opcionAvan = input("Elige una opción avanzada: ").lower()
            if opcionAvan == "a":
                base = float(input("Base: "))
                exp = float(input("Exponente: "))
                print("Resultado:", round(potencia(base, exp), 2))
            elif opcionAvan == "b":
                n1 = float(input("Número: "))
                n2 = float(input("Divisor: "))
                print("Resultado:", round(modulo(n1, n2), 2))
            elif opcionAvan == "c":
                n1 = float(input("Número: "))
                if n1 < 0:
                    print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
                else:
                    print("Resultado:", round(raiz_cuadrada(n1), 2))
            elif opcionAvan=="d":
                print("Volviendooooo")
            else:
                print("Opción avanzada no válida.")

        elif opcion == 6:
            print("Bye bye hasta pronto")
            continuar = False
        else:
            print("Opción no válida. Intenta de nuevo.")
menu()
