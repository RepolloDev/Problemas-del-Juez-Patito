# 1022
# Mercado Magico
# https://jv.umsa.bo/oj/problem.php?id=1022
# medio listas bucles condicionales

# description
# > [!WARNING] Tiempo excedido
# > La solución del problema no es eficiente, por lo que en el juez se tendra el error de tiempo excedido.
# TODO: Mejorar la solución para que sea más eficiente

# steps
# 1. Recibir el número de casos de prueba `T`
# 2. Por cada caso, recibir el número de productos `N` y el número de consultas `Q`
# 3. Recibir la lista de precios de los productos, en total son `N` precios
# 4. Por cada consulta, recibir una de las siguientes opciones:
#     - `A i v`, implica cambiar el precio del producto `i` a `v`
#     - `P i j`, implica sumar el precio de los productos `i` a `j`
# 5. Mostrar la suma de los precios de los productos `i` a `j`

from sys import stdin, stdout

T = int(input())
for _ in range(T):
    N, Q = map(int, stdin.readline().split())
    prices = list(map(int, stdin.readline().split()))
    for __ in range(Q):
        query = stdin.readline().split()
        if query[0] == "A":
            i, v = map(int, query[1:])
            prices[i - 1] = v
        elif query[0] == "P":
            i, j = map(int, query[1:])
            stdout.write(f"{sum(prices[i - 1:j])}\n")
