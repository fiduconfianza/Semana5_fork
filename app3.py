"""Respuestas puntos 1 al 3"""

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


print ("Alumnos registrados y sus notas:", alumnos)
print(f"El promedio de las notas del equipo es: {promedio:.2f}")
print(f"El alumno con la mejor nota es: {mejor_alumno}")
"""

"""Punto 4"""
"""
def ingresar_palabras():
    diccionario = {}
    while True:
        palabra = input("Ingrese una palabra (o 'salir' para terminar): ")
        if palabra.lower() == 'salir':
            break
        definicion = input("Ingrese la definición de la palabra: ")
        diccionario[palabra] = definicion
    return diccionario

def mostrar_diccionario_palabras(diccionario):
    print("\nDiccionario de palabras y sus definiciones:")
    for palabra, definicion in diccionario.items():
        print(f"{palabra}: {definicion}")

diccionario_palabras = ingresar_palabras()
mostrar_diccionario_palabras(diccionario_palabras)


"""Punton 4 y 5"""

def ingresar_palabras():
    diccionario = {}
    while True:
        palabra = input("Ingrese una palabra (o 'salir' para terminar): ")
        if palabra.lower() == 'salir':
            break
        definicion = input("Ingrese la definición de la palabra: ")
        diccionario[palabra] = definicion
    return diccionario

def mostrar_diccionario_palabras(diccionario):
    print("\nDiccionario de palabras y sus definiciones:")
    for palabra, definicion in diccionario.items():
        print(f"{palabra}: {definicion}")

def buscar_palabra(diccionario, palabra):
    definicion = diccionario.get(palabra)
    if definicion:
        print(f"Definición de '{palabra}': {definicion}")
    else:
        print(f"La palabra '{palabra}' no se encuentra en el diccionario.")

diccionario_palabras = ingresar_palabras()
mostrar_diccionario_palabras(diccionario_palabras)

while True:
    palabra_a_buscar = input("\nIngrese una palabra para buscar (o 'salir' para terminar): ")
    if palabra_a_buscar.lower() == 'salir':
        break
    buscar_palabra(diccionario_palabras, palabra_a_buscar)
