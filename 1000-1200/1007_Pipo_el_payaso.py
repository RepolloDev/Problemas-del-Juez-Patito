# 1007
# Pipo el payaso
# https://jv.umsa.bo/oj/problem.php?id=1007

"""
#facil #cadenas #bucles #condicionaless #medio

1. Obtener el número de casos de prueba T
2. Por cada caso, recibir el número de participantes N
3. Por cada participante, recibir un string (trabalenguas)
4. Convertir el string en una lista de palabras con `.split()`
5. Contar la cantidad de palabras que comienzan con la misma letra
6. Obtener el máximo de palabras que comienzan con la misma letra

* la variable `winner` solo cambia cuando letter_count es mayor a max_words, por lo que si hay un empate, el ganador será el que se haya registrado primero
"""


def max_prefix(words):
    """
    La función recibe una LISTA de palabras, crea un diccionario con la cantidad de palabras que comienzan con la misma letra y retorna el máximo valor de palabras que comienzan con la misma letra
    """
    prefix = {}
    for word in words:
        if word[0] in prefix:
            prefix[word[0]] += 1
        else:
            prefix[word[0]] = 1
    return max(prefix.values())


T = int(input())
for i in range(T):
    N = int(input())

    # Por defecto el ganador es el primer participante
    winner = 1
    max_words = 0

    for j in range(N):
        text = input()
        words = text.split()
        prefix_count = max_prefix(words)
        if prefix_count > max_words:
            max_words = prefix_count
            winner = j + 1
    print(f"El ganador es {winner}")
