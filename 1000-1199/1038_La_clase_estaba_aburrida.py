# 1038
# La clase estaba aburrida
# https://jv.umsa.bo/oj/problem.php?id=1038
# matematicas fácil bucles condicionales

# description
# Resumiendo el problema, nos dan un número entero positivo `a`
# el cual es el resultado de multiplicar dos números enteros positivos `x` e `y`.
#
# $$
# x \times y = a
# $$
#
# Inicialmente, debemos encontrar **la cantidad de productos que dan `a`**,
# lo que se puede obtener expresando la multiplicación como una función
#
# $$
# x(y) = \frac{a}{y}
# $$
#
# Entonces vamos probando con todos los valores de `y` desde 1 hasta `a`
# que den como resultado un número entero, ya solo contamos cuántos valores son.
#
# Finalmente, en el problema nos dan a entender que cada uno de los productos contados
# tiene una probabilidad de que sea el correcto, por probabilidad básica, se entiende
# que la probabilidad de un evento simple es de `1/n` donde `n` es la cantidad de eventos posibles,
# que en este caso es la cantidad de productos que dan `a`.

# steps
# 1. Leer la cantidad de casos de prueba `n`
# 2. Por cada caso, leer el valor de `a`
# 3. Contar la cantidad de productos que dan `a`
# 4. Imprimir la probabilidad de que sea el correcto


def x_range(y):
    count = 0
    for i in range(1, a + 1, 1):
        if a % i == 0:
            count += 1
    return count


n = int(input())
for _ in range(n):
    # x * y = a
    a = int(input())
    # x = a / y
    print(f"{1}/{x_range(a)}")
