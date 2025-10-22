# Daniel García Méndez - 2º DAM
# OBJETIVO 4 - FASES 1-2-3
# Este programa registra las notas de hasta 3 alumnos, calcula sus medias y clasifica su rendimiento.

# Solicita el número de alumnos (sin bucles, solo hasta 3)
cantidadAlumnos = int(input("¿Cuántos alumnos hay en el grupo? (1 a 3): "))
if cantidadAlumnos < 1 or cantidadAlumnos > 3:
    print("Número inválido. Debe ser entre 1 y 3.")
else:
    # Inicializa contadores
    mediaTotal = 0
    numAprobados = 0
    numNotasAmejorar = 0
    alumnosSuspensos = 0

    # Alumno 1
    if cantidadAlumnos >= 1:
        nombre1 = input("Nombre del alumno 1: ")
        num_notas1 = int(input("¿Cuántas notas tiene " + nombre1 + "? (1 a 3): "))
        if num_notas1 < 1 or num_notas1 > 3:
            print("Número de notas inválido.")
        else:
            suma1 = 0
            for i in range(1, num_notas1 + 1):
                suma1 += float(input("Nota " + str(i) + " de " + nombre1 + ": "))
            media1 = suma1 / num_notas1
            print("Media de", nombre1, ":", round(media1, 2))
            mediaTotal += media1
            if media1 >= 5:
                print("Aprobado")
                numAprobados += 1
            elif media1 >= 4:
                print("Necesita mejorar")
                numNotasAmejorar += 1
            else:
                print("Suspenso")
                alumnosSuspensos += 1

    # Alumno 2
    if cantidadAlumnos >= 2:
        nombre2 = input("Nombre del alumno 2: ")
        num_notas2 = int(input("¿Cuántas notas tiene " + nombre2 + "? (1 a 3): "))
        if num_notas2 < 1 or num_notas2 > 3:
            print("Número de notas inválido.")
        else:
            suma2 = 0
            for i in range(1, num_notas2 + 1):
                suma2 += float(input("Nota " + str(i) + " de " + nombre2 + ": "))
            media2 = suma2 / num_notas2
            print("Media de", nombre2, ":", round(media2, 2))
            mediaTotal += media2
            if media2 >= 5:
                print("Aprobado")
                numAprobados += 1
            elif media2 >= 4:
                print("Necesita mejorar")
                numNotasAmejorar += 1
            else:
                print("Suspenso")
                alumnosSuspensos += 1

    # Alumno 3
    if cantidadAlumnos == 3:
        nombre3 = input("Nombre del alumno 3: ")
        num_notas3 = int(input("¿Cuántas notas tiene " + nombre3 + "? (1 a 3): "))
        if num_notas3 < 1 or num_notas3 > 3:
            print("Número de notas inválido.")
        else:
            suma3 = 0
            for i in range(1, num_notas3 + 1):
                suma3 += float(input("Nota " + str(i) + " de " + nombre3 + ": "))
            media3 = suma3 / num_notas3
            print("Media de", nombre3, ":", round(media3, 2))
            mediaTotal += media3
            if media3 >= 5:
                print("Aprobado")
                numAprobados += 1
            elif media3 >= 4:
                print("Necesita mejorar")
                numNotasAmejorar += 1
            else:
                print("Suspenso")
                alumnosSuspensos += 1

    # Resumen final
    media_grupo = mediaTotal / cantidadAlumnos
    print("\nResumen final:")
    print("Media del grupo:", round(media_grupo, 2))
    print("Aprobados:", numAprobados)
    print("Necesitan mejorar:", numNotasAmejorar)
    print("Suspensos:", alumnosSuspensos)
