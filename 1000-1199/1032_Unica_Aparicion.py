# 1032
# Unica Aparicion
# https://jv.umsa.bo/oj/problem.php?id=1032
# medio listas operadores-binarios bucles

# description
# El problema se basa en que tenemos una lista de números donde existen pares de ellos, es decir
# que se repiten dos veces, excepto uno que se repite una sola vez. Debemos encontrar ese número.
#
# La forma más sencilla de hacerlo es mediante **el operador XOR**, que se basa en la siguiente tabla:
#
# | A | B | A XOR B |
# |---|---|---------|
# | 0 | 0 |   0     |
# | 0 | 1 |   1     |
# | 1 | 0 |   1     |
# | 1 | 1 |   0     |
#
# Es decir, si A y B son iguales, entonces el resultado es 0, de lo contrario es 1. Por lo tanto, aplicando esto a números es casi lo mismo, utilizaremos la propiedad:
#
# $$
# A \oplus 0 = A
# $$
#
# Que nos dice que **si un número se compara con 0, el resultado es el mismo número**. Por lo tanto, si tenemos una lista de números y los comparamos con el operador XOR, los números que se repiten dos veces se cancelarán y el único número que se repite una vez quedará.
#
# $$
# A_1 \oplus A_2 \oplus A_3 \oplus \ldots \oplus A_n) = A_{\text{único}}
# $$
#
# > [!IMPORTANT]
# > Para este problema, se utiliza el módulo `sys` con las funciones `stdin` y `stdout` para leer y escribir datos, respectivamente. Esto se hace para mejorar la eficiencia del programa, ya que la función `input()` y `print()` son más lentas lo que causa un error en el juez.

# steps
# 1. Leer el número de elementos de la lista.
# 2. Inicializar una variable `result` en 0.
# 3. Iterar sobre la lista de números.
# 4. Por cada número, aplicar el operador XOR con la variable `result`.
# 5. Al finalizar, imprimir el valor de `result`.

from sys import stdin, stdout

n = int(stdin.readline())
result = 0
for x_i in range(n):
    result ^= int(stdin.readline())
stdout.write(f"{result}\n")
