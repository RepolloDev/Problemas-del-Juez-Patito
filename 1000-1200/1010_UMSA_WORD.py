# 1010
# UMSA WORD
# https://jv.umsa.bo/oj/problem.php?id=1010

"""
#cadenas #diccionarios #búsqueda #bucles #condicionales #medio

Dado la variable `word` que contiene una cadena sin espacios de la palabra
a buscar, para el caso es `"UMSAICPC"`.

1. Obtener el número de casos de prueba `N`
2. Por cada caso, obtener la cadena de caracteres
3. Obtener un diccionario de la cantidad de caracteres de la cadena
4. De la cadena de la palabra a buscar, verificar si la cantidad de caracteres de la cadena de entrada es mayor o igual a la cantidad de caracteres de la palabra a buscar
5. Si es así, imprimir "ES POSIBLE", caso contrario "NO ES POSIBLE"

* La solución es para casos genéricos, no solo para la palabra "UMSAICPC"
"""


def count_chars(word):
    result = dict()  # Alternamente se puede usar {}
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


word = "UMSAICPC"
chars_word = count_chars(word)

N = int(input())
for i in range(N):
    input_text = input()
    chars_input = count_chars(input_text)
    is_possible = True
    for char in chars_word:
        if char not in chars_input:
            is_possible = False
            break
        if chars_word[char] >= chars_input[char]:
            is_possible = False
            break

    if is_possible:
        print("ES POSIBLE")
    else:
        print("NO ES POSIBLE")
