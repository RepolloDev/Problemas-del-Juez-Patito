# 1004
# Salir del laberinto
# https://jv.umsa.bo/oj/problem.php?id=1004
# listas medio matrices

# description
# TODO: Revisar la descripción del problema

# steps
# 1. Recibir el número de casos de prueba `T`
# 2. Recibir el tamaño de la matriz `N` y `M`
# 3. Recibir `N` lineas con `M` caracteres que representan la matriz
# 4. Recibir las coordenadas de `X1` y `Y1` de pepito
# 5. Recibir las coordenadas de `X2` y `Y2` de la salida

T = int(input())
way = "."
wall = "#"
for _ in range(T):
    N, M = map(int, input().split())
    matrix = [[char for char in input()] for _ in range(N)]
    X1, Y1 = map(int, input().split())
    X2, Y2 = map(int, input().split())
