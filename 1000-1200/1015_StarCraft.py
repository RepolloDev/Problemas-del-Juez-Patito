# 1015
# StarCraft
# https://jv.umsa.bo/oj/problem.php?id=1015

"""
#matematicas #bucles #condicionales #facil

1. Recibir los casos de prueba `T`
2. Por cada caso de prueba, recibir un entero `N` que es la cantidad de coordenadas
3. Recibir `N` lineas, dos enteros `x`, `y` que representan las coordenadas de una estructura
4. Recibir la coordenadas `x`, `y` donde cae la bomba y el radio `r` que cubre la bomba
5. Calcular la distancia entre la coordenada de la bomba y cada una de las coordenadas de las estructuras
6. Verificar si la distancia es menor o igual al radio de la bomba
"""

def distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


T = int(input())
for i in range(T):
    N = int(input())
    structures = []
    for j in range(N):
        x, y = map(int, input().split())
        structures.append((x, y))

    X, Y, r = map(int, input().split())
    coord_bomb = (X, Y)
    
    affected = 0
    for structure_coord in structures:
        if distance(coord_bomb, structure_coord) <= r:
            affected += 1
    
    print(affected)