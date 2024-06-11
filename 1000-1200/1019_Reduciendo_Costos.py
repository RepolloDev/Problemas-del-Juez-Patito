# 1019
# Reduciendo Costos
# https://jv.umsa.bo/oj/problem.php?id=1019

"""
#facil #matematicas #condicionales

Este problema es muy simple, pues hay que obtener el valor
medio de entre tres números, pero para hacerlo de forma
más sencilla se utiliza una lista.

1. Recibir el número de casos de prueba `T`
2. Por cada caso, recibir los números `a`, `b` y `c` en la lista `salaries`
"""

T = int(input())
for i in range(T):
    salaries = list(map(int, input().split()))
    salaries.sort()
    print(f"Case {i+1}: {salaries[1]}")