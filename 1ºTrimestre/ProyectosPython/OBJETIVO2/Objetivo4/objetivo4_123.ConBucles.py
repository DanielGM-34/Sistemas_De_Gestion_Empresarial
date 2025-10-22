# Daniel García Méndez - 2º DAM
# OBJETIVO 4 - FASES 1-2-3
# Este programa registra las notas de hasta 3 alumnos, calcula sus medias y clasifica su rendimiento.

cantidadAlumnos = int(input("¿Cuántos alumnos hay en el grupo? (1 a 3): "))
if cantidadAlumnos < 1 or cantidadAlumnos > 3:
    print("Número inválido. Debe ser entre 1 y 3.")
else:
    mediaTotal = 0
    numAprobados = 0
    numNotasAmejorar = 0
    alumnosSuspensos = 0

    contadorAlumnos = 1
    while contadorAlumnos <= cantidadAlumnos:
        nombre = input("Nombre del alumno " + str(contadorAlumnos) + ": ")
        num_notas = int(input("¿Cuántas notas tiene " + nombre + "? (1 a 3): "))
        if num_notas < 1 or num_notas > 3:
            print("Número de notas inválido.")
        else:
            suma = 0
            for i in range(1, num_notas + 1):
                nota = float(input("Nota " + str(i) + " de " + nombre + ": "))
                suma += nota
            media = suma / num_notas
            print("Media de", nombre, ":", round(media, 2))
            mediaTotal += media

            if media >= 5:
                print("Aprobado")
                numAprobados += 1
            elif media >= 4:
                print("Necesita mejorar")
                numNotasAmejorar += 1
            else:
                print("Suspenso")
                alumnosSuspensos += 1

        contadorAlumnos += 1

    media_grupo = mediaTotal / cantidadAlumnos
    print("\nResumen final:")
    print("Media del grupo:", round(media_grupo, 2))
    print("Aprobados:", numAprobados)
    print("Necesitan mejorar:", numNotasAmejorar)
    print("Suspensos:", alumnosSuspensos)
