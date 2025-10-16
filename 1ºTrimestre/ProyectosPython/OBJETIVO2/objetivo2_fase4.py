# Daniel García Méndez 2º DAM
# Pido números y hago comparaciones booleanas abajo
i = int(input("Introduce el primer número:"))
ii = int(input("Introduce el segundo número:"))
iii = int(input("Introduce el tercer número:"))



# Miro si i es menor a ii y si ii es menor que iii
print("(a < b ) and ( b < c):", (i<ii) and (ii<iii))

# Miro si i es igual a ii o si ii es igual que iii
print("(a == b ) or ( b == c):", (i==ii) or (ii==iii))

# Miro si i no es mayor a iii
print(" not (a > c ):", not (i>iii))

 