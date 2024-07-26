# 1039
# Redundancia
# https://jv.umsa.bo/oj/problem.php?id=1039
# listas medio bucles

# description
# El problema consiste en leer una lista de números enteros
# y determinar cuántas veces se repite cada número en la lista.
# Esto se logra facilmente utilizando un diccionario o un _hashmap_
# donde la clave es el número y el valor es la cantidad de veces que se repite.
#
# > [!INFO] Todo ordenado
# > En el problema se pide utilizar algunas estructuras de datos para mantener el orden de los elementos, pero en Python los diccionarios se guardan en orden de inserción, entonces no es necesario ordenar los elementos.

# steps
# 1. Leer la lista de números enteros
# 2. Crear un diccionario para contar las repeticiones
# 3. Por cada número en la lista, si no está en el diccionario, agregarlo con valor 1, si ya está, incrementar el valor en 1
# 4. Imprimir el diccionario

from sys import stdin, stdout

counters = {}
my_list = list(map(int, stdin.readline().split()))
for number in my_list:
    if number in counters:
        counters[number] += 1
    else:
        counters[number] = 1

for key, value in counters.items():
    # key: número, value: cantidad de veces que se repite
    stdout.write(f"{key} {value}\n")
