# 1026
# Tuncuña
# https://jv.umsa.bo/oj/problem.php?id=1026
# facil matematicas bucles condicionales

# description
# > [!note] Sobre el input y print
# > La solución hace uso del modulo `sys` para leer y escribir datos por
# > temas de problemas con el juez patito, ya que las funciones `input()`
# > y `print()` no funcionan correctamente con este problema.

# steps
# 1. Recibir la cantidad de veces `T` que juega Bob
# 2. Por cada jugada, recibir un entero `N` que representa la casilla a la que quiere llegar
# 3. Seguir la serie sumando 1, 2, 3, ... hasta llegar a la casilla `N`
# 4. Si la suma da igual a `N`, entonces mostrar "Go On Bob" y la cantidad de pasos que se necesita, de lo contrario mostrar el el mensaje "Better Luck Next Time"

from sys import stdin, stdout

T = int(stdin.readline())
for i in range(1, T + 1, 1):
    N = int(stdin.readline())
    n = int(pow(0.25 + 2 * N, 0.5) - 0.5)
    sum = n * (n + 1) // 2
    if sum == N:
        stdout.write("Go On Bob " + str(n) + "\n")
    else:
        stdout.write("Better Luck Next Time" + "\n")
