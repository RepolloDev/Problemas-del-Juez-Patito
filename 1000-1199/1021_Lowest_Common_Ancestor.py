# 1021
# Lowest Common Ancestor
# https://jv.umsa.bo/oj/problem.php?id=1021
# grafos arboles recorrido medio bucles condicionales matematicas

# description
# Para este caso es necesario generar un árbol binario basado en lo siguiente:
#
# - La raíz del árbol es el nodo 1
# - Para cualquier nodo `x`, su hijo izquierdo es `2 * x` y su hijo derecho es `2 * x + 1`
#
# TODO: Agregar un ejemplo del árbol generado
#
# La solución es más matemática que nada, pues por la naturaleza del árbol,
# se puede obtener el nodo padre de cualquier nodo `x` con la fórmula `x // 2`.
# La idea es obtener los padres de ambos hasta que ambos tengan el mismo padre.

# steps
# 1. Recibir datos indefinidamente hasta que se reciba una línea en blanco
# 2. Por cada linea, se recibe dos números `v` y `w` que representan dos nodos del árbol
# 3. Obtener el nivel de los nodos `v` y `w` en el árbol
# 4. Mover el nodo de mayor nivel hacia arriba hasta que ambos nodos tengan el mismo nivel
# 5. Mover ambos nodos hacia arriba hasta que ambos nodos tengan el mismo padre
# 6. Imprimir el nodo padre común más bajo

import sys


def get_father(v):
    return v // 2


def get_level(a, b):
    level_a = 0
    level_b = 0
    while a != 1 or b != 1:
        if a != 1:
            a = get_father(a)
            level_a += 1
        if b != 1:
            b = get_father(b)
            level_b += 1
    return level_a, level_b


for line in sys.stdin:
    if line == "\n":
        break

    v, w = map(int, line.split())
    level_v, level_w = get_level(v, w)

    while level_v > level_w:
        v = get_father(v)
        level_v -= 1

    while level_w > level_v:
        w = get_father(w)
        level_w -= 1

    while v != w:
        v = get_father(v)
        w = get_father(w)

    print(v)
