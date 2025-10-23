# Daniel García Méndez 2ºDAM

# Validación del número de alumnos con while
numAlumnosTotales = int(input("¿Cuántos alumnos hay? (1 a 3): "))
while numAlumnosTotales < 1 or numAlumnosTotales > 3:
    print("MÁXIMO DEBE HABER 3 ALUMNOS")
    numAlumnosTotales = int(input("¿Cuántos alumnos hay? (1 a 3): "))

# Inicialización de varibales, nos harán falta más adelante.
mediaTotal = 0
aprobadosTotales = 0
notasAmejorar = 0
alumnosSuspensos = 0

contadorAlumnos = 1
while contadorAlumnos <= numAlumnosTotales:
    nombre = input("Nombre del alumno " + str(contadorAlumnos) + ": ")
    
    # Validación del número de notas con while
    num_notas = int(input("¿Cuántas notas tiene " + nombre + "? (1 a 3): "))
    while num_notas < 1 or num_notas > 3:
        print("Número de notas inválido.")
        num_notas = int(input("¿Cuántas notas tiene " + nombre + "? (1 a 3): "))

    suma = 0
    for i in range(1, num_notas + 1):
        nota = float(input("Nota " + str(i) + " de " + nombre + ": "))
        suma += nota

    media = suma / num_notas
    print("Media de", nombre, ":", round(media, 2))
    mediaTotal += media

    if media >= 5:
        print("Aprobado")
        aprobadosTotales += 1
    elif media >= 4:
        print("Necesita mejorar")
        notasAmejorar += 1
    else:
        print("Suspenso")
        alumnosSuspensos += 1

    contadorAlumnos += 1

# Cálculo de la media de grupo, media, aprobados, mejoras y suspensos.
media_grupo = mediaTotal / numAlumnosTotales
print("\nResumen final:")
print("Media del grupo:", round(media_grupo, 2))
print("Aprobados:", aprobadosTotales)
print("Necesitan mejorar:", notasAmejorar)
print("Suspensos:", alumnosSuspensos)
