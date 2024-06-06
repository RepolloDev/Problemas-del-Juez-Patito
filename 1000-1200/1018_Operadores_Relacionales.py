# 1018
# Operadores Relacionales
# https://jv.umsa.bo/oj/problem.php?id=1018

"""
#facil #matematicas #condicionales #bucles

1. Recibir el número de casos de prueba `t`
2. Por cada caso, recibir los números `a` y `b`
3. Comparar `a` y `b`, imprimir su relación respectivas
"""

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a < b:
        print("<")
    elif a > b:
        print(">")
    else:
        print("=")