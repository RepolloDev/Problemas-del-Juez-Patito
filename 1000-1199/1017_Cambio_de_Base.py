# 1017
# Cambio de Base
# https://jv.umsa.bo/oj/problem.php?id=1017
# matematicas facil bucles condicionales

"""description
Para este problema es necesario conocer el concepto de cambio de base. Este
proceso se logra mediante la división sucesiva del número original entre la base
a la que se quiere cambiar. El residuo de cada división se convierte en un dígito
del nuevo número en la base deseada. El proceso se repite hasta que el número
original sea menor que la base.

![ejemplo](https://rea.ceibal.edu.uy/elp/unidad-a-que-hora/cambio_base3.gif)

> [!note] Nota
> En el código, se pone un limite en el for desde 2 hasta 10 en la iteración,
> ya que el problema indica que el número `n` es igual a `a` en alguna base
> entre 2 y 9.
"""

"""steps
1. Recibir el número de casos de prueba `N`
2. Por cada caso, recibir los números `n` y `a`
3. Cambiar de base al número n desde 2 hasta 9
4. Si el número en la nueva base es igual a `a`, imprimir la base (`i`)
"""

def change_base(n, base):
    new_n = 0
    exponent = 0
    while n > 0:
        digit = n % base
        new_n += digit * (10 ** exponent)
        exponent += 1
        n = n // base

    return new_n

N = int(input())
for _ in range(N):
    n, a = map(int, input().split())
    # i = 2; i < 10; i++
    for i in range(2, 10, 1):
        new_n = change_base(n, i)
        if new_n == a:
            print(i)
            break