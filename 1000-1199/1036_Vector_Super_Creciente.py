# 1036
# Vector super creciente
# https://jv.umsa.bo/oj/problem.php?id=1036
# listas series matematicas medio bucles condicionales

# description
# Un *vector creaciente* es aquel que cumple con la siguiente propiedad:
#
# $$
# A[i] > A[1] + A[2] + \ldots + A[i-1]
# $$
#
# Es decir, **el elemento `i`-ésimo es mayor a la suma de los `i-1` anteriores**. Por ejemplo, el vector `[1, 2, 4]` es un vector creciente porque $4 > 1 + 2$.
#
# El problema ahora se simplifica mucho viendo un vector creciente como una serie geométrica.
# Pensemos en un _ejemplo base_, es decir, un vector sencillo que cumpla, este es
# `[1, 2, 4, 8, 16, 32]` (Puedes comprobarlo). Fijandose en los elementos,
# notar que son los valores de son potencias de 2, es decir, $2^i$. Entonces,
# el vector creciente se puede definir como:
#
# $$
# A[i] = 2^i
# $$
#
# > [!NOTE] Cambio en código
# > En el código se vera que se usa `A_k = 2^(k-1)`, esto es porque las listas en Python empiezan en 0, por lo que el primer elemento es `A[0] = 2^0 = 1`.

# steps
# 1. Leer el número de casos de prueba `T`
# 2. Para cada caso de prueba, leer los valores `N`, `k` y `x`
# 3. Calcular el valor de `A_k = 2^(k-1)`
# 4. Si `x` es mayor o igual a `A_k`, imprimir "SI", en caso contrario, imprimir "NO"


T = int(input())
for _ in range(T):
    N, k, x = map(int, input().split())
    # A[k] = 2^(k-1)
    A_k = 2 ** (k - 1)
    if x >= A_k:
        print("SI")
    else:
        print("NO")
