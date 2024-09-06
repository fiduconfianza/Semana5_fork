#Adivinar un número con intentos limitados
import random
 
numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 7
adivinado = False
 
print("Estoy pensando en un número entre 1 y 100.")
while intentos < max_intentos and not adivinado:
    intento = int(input("Intenta adivinar el número: "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número en", intentos, "intentos.")
        adivinado = True
    elif intento < numero_secreto:
        print("El número es mayor que", intento)
    else:
        print("El número es menor que", intento)
 
if not adivinado:
    print("Lo siento, no adivinaste el número en el número máximo de intentos.")
    print("El número secreto era", numero_secreto)





    #Eliminar duplicados de una listaa:
 
 
def eliminar_duplicados(lista):  
    elementos_unicos = set(lista)
   
    lista_sin_duplicados = list(elementos_unicos)
    return lista_sin_duplicados
 
 
numeros = [1, 2, 2, 3, 4, 4, 5]
resultado = eliminar_duplicados(numeros)
print(resultado)


#Contar vocales en una frase
cadena = input("Ingresa una cadena: ")
vocales = "aeiouAEIOU"
contador = 0

for caracter in cadena:
    if caracter in vocales:
        contador += 1

print("La cadena tiene", contador, "vocales.")


#Calculadora básica

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

while True:
    print("\nCalculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1/2/3/4/5): ")
    
    if opcion == '5':
        print("Saliendo de la calculadora...")
        break
    
    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if opcion == '1':
            print("Resultado:", sumar(num1, num2))
        elif opcion == '2':
            print("Resultado:", restar(num1, num2))
        elif opcion == '3':
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == '4':
            print("Resultado:", dividir(num1, num2))
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")

    #Crear una lista de números pares


        pares = []
numero = 1

while numero <= 100:
    if numero % 2 == 0:
        pares.append(numero)
    numero += 1

print("Números pares entre 1 y 100:", pares)