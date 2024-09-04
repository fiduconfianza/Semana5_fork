def diccionario_alumnos():
    alumnos = {}
    while True:
        nombre = input("Ingrese el nombre del alumno o escriba (salir) para finalizar: ")
        if nombre.lower() == 'salir':
            break
        nota = float(input("Ingrese la nota del alumno: "))
        alumnos[nombre] = nota
    return alumnos

def promedio_notas(alumnos):
    if not alumnos: 
        return 0
    suma_notas = 0
    for nota in alumnos.values():
        suma_notas += nota
    promedio = suma_notas / len(alumnos)
    return promedio

def alumno_con_mejor_nota(alumnos):
    if not alumnos:  
        return None
    
    mejor_alumno = None
    mejor_nota = float('-inf')  
    
    for alumno, nota in alumnos.items():
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = alumno
    
    return mejor_alumno


alumnos = diccionario_alumnos()
promedio = promedio_notas(alumnos)
mejor_alumno = alumno_con_mejor_nota(alumnos)

"""Respuestas puntos 1 al 3"""
print ("Alumnos registrados y sus notas:", alumnos)
print(f"El promedio de las notas del equipo es: {promedio:.2f}")
print(f"El alumno con la mejor nota es: {mejor_alumno}")


