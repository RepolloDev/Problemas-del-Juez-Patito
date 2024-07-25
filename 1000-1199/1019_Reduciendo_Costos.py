# 1019
# Reduciendo Costos
# https://jv.umsa.bo/oj/problem.php?id=1019
# facil matematicas condicionales

# description
# Este problema es muy simple, pues hay que obtener el valor
# medio de entre tres números, lo cual se puede hacer ordenando
# la lista y obteniendo el valor en la posición 1.

# steps
# 1. Recibir el número de casos de prueba `T`
# 2. Por cada caso, recibir los números `a`, `b` y `c` en la lista `salaries`
# 3. Obtener el valor medio de la lista

T = int(input())
for i in range(T):
    salaries = list(map(int, input().split()))
    salaries.sort()
    print(f"Case {i+1}: {salaries[1]}")
