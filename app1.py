#SUMAR ELEMENTOS: 

def suma_elementos(lista):
    suma = 0  # Variable acumuladora
    for numero in lista:  # Recorre cada número en la lista
        suma = suma + numero  # Suma cada número a la variable acumuladora
    return suma  # Devuelve la suma total

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
print(suma_elementos(numeros))


#CONTAR ELEMENTOS: 

def contar_pares(lista):
    contador = 0  # Contador de números pares
    for numero in lista:  # Recorre cada número en la lista
        if numero % 2 == 0:  # Verifica si el número es divisible por 2
            contador = contador + 1  # Incrementa el contador si es par
    return contador  # Devuelve la cantidad de números pares

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5, 6]
print(contar_pares(numeros))

#ELEMENTO MAS GRANDE: 

def elemento_mas_grande(lista):
    if len(lista) == 0:  # Verificación de lista vacía
        return None  # Devuelve None si la lista está vacía
    maximo = lista[0]  # Asume que el primer elemento es el más grande
    for numero in lista:  # Recorre cada número en la lista
        if numero > maximo:  # Compara cada número con el actual más grande
            maximo = numero  # Actualiza el número más grande
    return maximo  # Devuelve el número más grande

# Ejemplo de uso
numeros = [3, 5, 7, 2, 8]
print(elemento_mas_grande(numeros))

#NUEVA LISTA CON ELEMENTOS x2: 

def multiplicar_elementos(lista):
    nueva_lista = []  # Nueva lista vacía
    for numero in lista:  # Recorre cada número en la lista
        nueva_lista.append(numero * 2)  # Multiplica el número por 2 y lo agrega a la nueva lista
    return nueva_lista  # Devuelve la nueva lista

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
print(multiplicar_elementos(numeros))

#INVERTIR LISTA: 

def invertir_lista(lista):
    lista_invertida = []  # Nueva lista vacía
    for i in range(len(lista) - 1, -1, -1):  # Recorre la lista original desde el final al principio
        lista_invertida.append(lista[i])  # Agrega cada elemento en orden inverso
    return lista_invertida  # Devuelve la lista invertida

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
print(invertir_lista(numeros)) 



