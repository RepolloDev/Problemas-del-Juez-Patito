# 1040
# El libro y la torre humana
# https://jv.umsa.bo/oj/problem.php?id=1040
# facil matematicas listas

# description
# Contextualizando, hay un libro a una altura `a`, hay `n` amigos
# que harán una torre humana para alcanzar el libro.
# Cada amigo tiene una altura `h`, si la suma de las alturas de los amigos
# es mayor o igual a la altura del libro, entonces los amigos podrán alcanzar
# el libro, de lo contrario, no podrán.
#
# > [!WARNING] Solución directa
# > Una de las condiciones del problema indica que se puede alcanzar el libro si la altura del libro está dentro del intervalo de altura del último amigo, es decir, si el libro está entre los pies y la cabeza del último amigo, entonces se puede alcanzar el libro.
# > Para este caso, solo es necesario saber si llegan a alcanzar o superar la altura del libro, no es necesario saber cuántos amigos se necesitan para alcanzarlo.
# > Vease el problema **[1041]**

# steps
# 1. Leer el número de casos de prueba
# 2. Por cada caso de prueba, leer:
#    - `a`: altura del libro y número flotante
#    - `n`: cantidad de amigos
# 3. Leer la altura de cada amigo y guardarla en una lista
# 4. Sumar las alturas de los amigos y compararla con la altura del libro
# 5. Si la suma es mayor o igual a la altura del libro, imprimir `:)`, de lo contrario, imprimir `:(`


c = int(input())
for _ in range(c):
    a = float(input())
    n = int(input())
    friends = []
    for __ in range(n):
        friends.append(float(input()))
    if sum(friends) >= a:
        print(":)")
    else:
        print(":(")
