# Daniel García Méndez 2º DAM

# Pide dos enteros y muestra suma, resta, multiplicación y división.
n1 = int(input("Introduce el primer número:"))
n2 = int(input("Introduce el segundo número:"))
print("Suma:", n1 + n2)
print("Resta:", n1 - n2)
print("Multiplicación:", n1 * n2)
print("División:", n1 / n2)
print("- 2 -")


# Pide tres reales (float), calcula el promedio y muéstralo redondeado a 2 decimales.
real1 = float(input("Introduce el primer número:"))
real2 = float(input("Introduce el segundo número:"))
real3 = float(input("Introduce el tercer número:"))
promedio = round((real1+real2+real3)/3,2)

print("El promedio es:",promedio)
print("- 3 -")

# Pide dos enteros y muestra:
# si el primero es mayor que el segundo,
# si son iguales,
# si el segundo es distinto de 0.

ent1 = int(input("Introduce el primer número:"))
ent2 = int(input("Introduce el segundo número:"))

print("¿El primero es mayor?", ent1>ent2)
print("¿Son iguales?", ent1==ent2)
print("¿El segundo es distinto de cero?", ent2!=0)
print("- 4 -")
# Pide dos valores lógicos escritos como True o False y muestra:
logico1 = eval(input("Introduce el primer valor lógico (True/False):"))
logico2 = eval(input("Introduce el primer valor lógico (True/False):"))
print("Resultado de and", logico1==logico2)
print("Resultado de or:", (logico1==logico2) or (logico1!=logico2) or (logico2!=logico1))
print("Resultado de not primer valor:", logico1==False)
print("Resultado de not segundo valor:", logico2==False)

print("- 5 -")
# Pide dos edades como texto, convierte a entero y muestra suma y promedio (1 decimal).
edad1 = int(input("Edad de la primera persona:"))
edad2 = int(input("Edad de la segunda persona:"))
suma =  edad1+edad2
print("Suma total:", suma)
promedio = round(suma/3,1)
print("Promedio:", promedio)

print("- 6 -")
# Pide dos números (pueden ser reales) y muestra:
i = int(input("Introduce el primer número:"))
ii = int(input("Introduce el segundo número:"))
print("(a > 10) and (b<5):", (i>10) and (ii<5))
print("(a ==b) or (b<5):", (i==ii) or (ii>0))
print("not (a < b)", (i<i))

print("- 7 -")
# Pide dos reales, divide y muestra el resultado redondeado a 1 decimal.
nn1 = int(input("Introduce el dividendo:"))
nn2 = int(input("Introduce el divisor:"))
divisi = round(nn1/nn2,1)
print("Resultado redondeado:", divisi)