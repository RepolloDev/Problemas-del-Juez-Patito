# 1020
# Planificando un viaje
# https://jv.umsa.bo/oj/problem.php?id=1020

"""
#facil #listas #bucles #condicionales

1. Recibir los casos de prueba hasta que ya no haya datos
2. Recibir una linea con los siguientes datos:
    - `N`: número de participantes
    - `P`: presupuesto
    - `H`: número de hoteles
    - `S`: número de semanas
3. Por cada hotel, recibir dos lineas
    - `p`: precio por persona
    - `camas`: linea de camas disponibles por semana (`S` datos)
4. Verificar si hay camas disponibles para todos los participantes
5. Si hay camas disponibles, calcular el precio total si esta dentro del presupuesto
6. Si hay precios válidos, imprimir el menor precio, sino, imprimir "quedarse en casa"
"""

import sys

for line in sys.stdin:
    if line == "\n":
        break
    
    N, P, H, S = map(int, line.split())
    prices = []
    for i in range(H):
        p = int(input())
        camas = list(map(int, input().split()))
        # Retorna True si hay un valor mayor o igual a N
        any_camas = any([c >= N for c in camas])
        if any_camas and p * N <= P:
            prices.append(p * N)
    
    if prices:
        print(min(prices))
    else:
        print("quedarse en casa")