# 1031
# Mediana
# https://jv.umsa.bo/oj/problem.php?id=1031
# matematicas facil ordenamiento listas bucles condicionales

# description
# La lógica de este problema es obtener la *mediana* de una lista de números dados, inicialmente
# las condiciones que se toman en cuenta son:
#
# - La lista de números es de tamaño impar.
# - La lista de números está ordenada.
#
# Si se cumple con esto, entonces pasamos a obtener la mediana de la lista con la siguiente fórmula:
#
# $$
# M = \\frac{n}{2}
# $$
#
# Donde `M` es `median_index` (la posición de la mediana en la lista). Por otro lado, la otra condición es que tanto a la izquierda como a la derecha de la mediana no existan números iguales a la mediana, si se cumple esta condición, entonces la mediana es correcta, de lo contrario, la mediana no es correcta.

# steps
# 1. Recibir casos de prueba hasta que se reciba una línea en blanco `\n`.
# 2. Por cada caso, recibir la cantidad de números `n`, seguido de la lista de números.
# 3. Ordenar la lista de números.
# 4. Si `n` es par, imprimir `-1` y continuar con el siguiente caso.
# 5. Calcular la posición de la mediana `median_index = (n) // 2`.
# 6. Inicializar dos variables `i` y `j` con los valores `median_index - 1` y `median_index + 1` respectivamente.
# 7. Inicializar una variable `is_median` en `True` para saber si la mediana es correcta.
# 8. Recorrer la lista de números hacia la izquierda y derecha desde la posición de la mediana para verificar si la mediana es correcta.
# 9. Si la mediana es correcta, imprimir el valor de la mediana, de lo contrario imprimir `-1`.

from sys import stdin


for line in stdin:
    if line == "\n":
        break

    n = int(line)
    numbers = list(map(int, input().split()))
    numbers.sort()

    if n % 2 == 0:
        print(-1)
        continue

    median_index = (n) // 2
    i, j = median_index - 1, median_index + 1
    is_median = True
    while i >= 0 and j < n:
        if numbers[i] == numbers[median_index]:
            is_median = False
            break
        if numbers[j] == numbers[median_index]:
            is_median = False
            break
        i -= 1
        j += 1

    if is_median:
        print(numbers[median_index])
    else:
        print(-1)
