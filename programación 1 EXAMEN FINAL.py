#PRIMERA PARTE
# >>>>>> EJERCICIO 1
# par_impar.py

def determinar_par_impar(numero):
    if numero % 2 == 0:
        return "El número ingresado es par."
    else:
        return "El número ingresado es impar."

# Solicitar al usuario que ingrese un número
numero_ingresado = int(input("Ingrese un número: "))

# Llamar a la función e imprimir el resultado
resultado = determinar_par_impar(numero_ingresado)
print(resultado)

# >>>>>> EJERCICIO 2

# par_impar.py

def determinar_par_impar(numero):
    if numero % 2 == 0:
        return "El número ingresado es par."
    else:
        return "El número ingresado es impar."

def generar_serie_fibonacci(n):
    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[i-1] + serie[i-2])
    return serie

# Solicitar al usuario que ingrese un número
numero_ingresado = int(input("Ingrese un número: "))

# Llamar a la función y mostrar el resultado
resultado_par_impar = determinar_par_impar(numero_ingresado)
print(resultado_par_impar)

# Solicitar al usuario que ingrese la cantidad de términos de la serie Fibonacci
n_fibonacci = int(input("Ingrese la cantidad de términos de la serie de Fibonacci: "))

# Llamar a la función e imprimir la serie de Fibonacci
serie_fibonacci = generar_serie_fibonacci(n_fibonacci)
print(f"Los primeros {n_fibonacci} términos de la serie de Fibonacci son: {serie_fibonacci}")


# >>>>>> EJERCICIO 3

# par_impar.py

def determinar_par_impar(numero):
    if numero % 2 == 0:
        return "El número ingresado es par."
    else:
        return "El número ingresado es impar."

def generar_serie_fibonacci(n):
    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[i-1] + serie[i-2])
    return serie

def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas para comparación
    cadena_sin_espacios = ''.join(cadena.split()).lower()
    
    # Verificar si la cadena es igual al revés
    return cadena_sin_espacios == cadena_sin_espacios[::-1]

# Solicitar al usuario que ingrese una cadena de texto
cadena_ingresada = input("Ingrese una cadena de texto: ")

# Llamar a la función y mostrar el resultado
resultado_par_impar = determinar_par_impar(len(cadena_ingresada))
print(resultado_par_impar)

# Llamar a la función y mostrar el resultado
if es_palindromo(cadena_ingresada):
    print("La cadena ingresada es un palíndromo.")
else:
    print("La cadena ingresada no es un palíndromo.")


# >>>>>> EJERCICIO 4
# par_impar.py

def determinar_par_impar(numero):
    if numero % 2 == 0:
        return "El número ingresado es par."
    else:
        return "El número ingresado es impar."

def generar_serie_fibonacci(n):
    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[i-1] + serie[i-2])
    return serie

def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas para comparación
    cadena_sin_espacios = ''.join(cadena.split()).lower()
    
    # Verificar si la cadena es igual al revés
    return cadena_sin_espacios == cadena_sin_espacios[::-1]

def encontrar_extremos(lista):
    if not lista:
        return None, None  # La lista está vacía
    
    minimo = maximo = lista[0]
    
    for numero in lista:
        if numero < minimo:
            minimo = numero
        elif numero > maximo:
            maximo = numero
    
    return minimo, maximo

# Solicitar al usuario que ingrese una lista de números
lista_numeros_ingresada = input("Ingrese una lista de números separados por espacios: ")

# Convertir la cadena de entrada a una lista de números
lista_numeros = [float(numero) for numero in lista_numeros_ingresada.split()]

# Llamar a la función y mostrar el resultado
resultado_par_impar = determinar_par_impar(len(lista_numeros))
print(resultado_par_impar)

# Llamar a la función y mostrar el resultado
minimo, maximo = encontrar_extremos(lista_numeros)
print(f"El número más pequeño de la lista es: {minimo}")
print(f"El número más grande de la lista es: {maximo}")



# >>>>>> EJERCICIO 5

# par_impar.py

import math

def determinar_par_impar(numero):
    if numero % 2 == 0:
        return "El número ingresado es par."
    else:
        return "El número ingresado es impar."

def generar_serie_fibonacci(n):
    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[i-1] + serie[i-2])
    return serie

def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas para comparación
    cadena_sin_espacios = ''.join(cadena.split()).lower()
    
    # Verificar si la cadena es igual al revés
    return cadena_sin_espacios == cadena_sin_espacios[::-1]

def encontrar_extremos(lista):
    if not lista:
        return None, None  # La lista está vacía
    
    minimo = maximo = lista[0]
    
    for numero in lista:
        if numero < minimo:
            minimo = numero
        elif numero > maximo:
            maximo = numero
    
    return minimo, maximo

def calcular_area_perimetro_circulo(radio):
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    return area, perimetro

# Solicitar al usuario que ingrese el radio del círculo
radio_circulo = float(input("Ingrese el radio del círculo: "))

# Llamar a la función y mostrar el resultado
resultado_par_impar = determinar_par_impar(int(radio_circulo))
print(resultado_par_impar)

# Llamar a la función y mostrar el resultado
minimo, maximo = encontrar_extremos([radio_circulo])
print(f"El radio del círculo es: {radio_circulo}")
print(f"El número más pequeño (y el radio del círculo) es: {minimo}")
print(f"El número más grande (y el radio del círculo) es: {maximo}")

# Llamar a la función y mostrar el resultado
area, perimetro = calcular_area_perimetro_circulo(radio_circulo)
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")


# >>>>>> EJERCICIO 6

# par_impar.py

import math

def determinar_par_impar(numero):
    if numero % 2 == 0:
        return "El número ingresado es par."
    else:
        return "El número ingresado es impar."

def generar_serie_fibonacci(n):
    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[i-1] + serie[i-2])
    return serie

def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas para comparación
    cadena_sin_espacios = ''.join(cadena.split()).lower()
    
    # Verificar si la cadena es igual al revés
    return cadena_sin_espacios == cadena_sin_espacios[::-1]

def encontrar_extremos(lista):
    if not lista:
        return None, None  # La lista está vacía
    
    minimo = maximo = lista[0]
    
    for numero in lista:
        if numero < minimo:
            minimo = numero
        elif numero > maximo:
            maximo = numero
    
    return minimo, maximo

def calcular_area_perimetro_circulo(radio):
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    return area, perimetro

def encontrar_mayor(num1, num2, num3):
    return max(num1, num2, num3)

# Solicitar al usuario que ingrese tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Llamar a la función y mostrar el resultado
mayor = encontrar_mayor(num1, num2, num3)
print(f"El mayor de los tres números es: {mayor}")


