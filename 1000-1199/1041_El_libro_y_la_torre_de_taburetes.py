# 1041
# El libro y la torre de taburetes
# https://jv.umsa.bo/oj/problem.php?id=1041
# facil matematicas

# description
# Este problema es similar al **[1040]**, pero en lugar de amigos, se tienen taburetes.
# Recibimos una cantidad de tabuerees `n`, la altura de los taburetes `x`, la altura del libro `h`,
# y las alturas de tres amigos `a`, `b`, `c`.
#
# El fin es determinar cuántos taburetes se necesitan para alcanzar el libro.
# Para esto, obtenemos al amigo más alto y calculamos la altura que alcanzaría si se subiera sobre `i` taburetes considerando que la altura del libro debe estar entre los pies y la cabeza del amigo.
#
# $$
# x * i \leq h \leq \max(a, b, c) + x * i
# $$

# steps
# 1. Recibir el número de casos de prueba `T`
# 2. Por cada caso de prueba, leer:
#   - `n`: cantidad de taburetes
#   - `x`: altura de todos los taburetes
#   - `h`: altura del libro
#   - `a`, `b`, `c`: alturas de los amigos
# 3. Obtener al amigo más alto
# 4. Por cada taburete `i` desde 0 hasta `n`, calcular la altura que alcanzaría el amigo más alto
# 5. Si la altura del libro está entre los pies y la cabeza del amigo, imprimir `i`, de lo contrario, imprimir `:(`


T = int(input())
for _ in range(T):
    n, x, h = map(float, input().split())
    a, b, c = map(float, input().split())
    tall_friend = max(a, b, c)

    nrof_taburets = -1
    for i in range(int(n) + 1):
        value = tall_friend + x * i
        if x * i <= h and h <= value:
            nrof_taburets = i
            break
    if nrof_taburets == -1:
        print(":(")
    else:
        print(nrof_taburets)
