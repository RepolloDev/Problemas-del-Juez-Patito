# 1008
# Ordenando mi directorio
# https://jv.umsa.bo/oj/problem.php?id=1008
# busqueda ordenamiento listas cadenas bucles facil

"""description
El problema consiste en busqueda y ordenamiento de elementos en una lista de archivos,
donde es solo hay que buscar los elementos "." y ".." y colocarlos al final de la lista.

> [!note] Nota
> Al intercambiar el elemento "." o ".." con el último elemento de la lista,
> se debe decrementar el índice del último elemento de la lista para no volver
> a intercambiar el mismo elemento.
"""

"""steps
1. Obtener los casos de prueba `T``
2. Por cada caso de prueba obtener el número de archivos `N`
3. Por cada caso de prueba leer y guardar los nombres de los archivos
4. Buscar "." o ".." en la lista de archivos
5. Verificar si "." y ".." son los últimos elementos de la lista (en cualquier orden)
    - Si es así mostrar "Caso [i]" y listar los archivos
    - Si no, buscar "." o ".." e intercambiarlos con el último elemento de la lista
    - Repetir el paso 5, pero ahora con el penúltimo elemento de la lista
"""


def verifyFiles(fileList):
    if fileList[-1] == "." and fileList[-2] == "..":
        return True
    elif fileList[-1] == ".." and fileList[-2] == ".":
        return True
    else:
        return False


def findDotsIndex(fileList):
    for i in range(len(fileList)):
        if fileList[i] == "." or fileList[i] == "..":
            return i
    return -1


def swapFiles(fileList, index_a, index_b):
    temp = fileList[index_a]
    fileList[index_a] = fileList[index_b]
    fileList[index_b] = temp


T = int(input())
for i in range(T):
    N = int(input())
    files_list = []
    for j in range(N):
        file = input()
        files_list.append(file)

    last_index = len(files_list) - 1
    while not verifyFiles(files_list):
        dot_index = findDotsIndex(files_list)
        swapFiles(files_list, dot_index, last_index)
        last_index -= 1

    print(f"Caso {i + 1}:")
    for file in files_list:
        print(file)
    print()
