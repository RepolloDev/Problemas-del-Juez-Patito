# 1009
# Mi música Favorita
# https://jv.umsa.bo/oj/problem.php?id=1009
# matematicas listas medio

# description
# El problema se trata de la obtención de subconjuntos de una lista que representan la duración de las canciones de una lista de reproducción. El objetivo es obtener el subconjunto de canciones que sumen la mayor cantidad de tiempo posible, pero que no sobrepasen el tiempo máximo de reproducción del casete.
#
# !TODO: Utilizar operadores binarios

# steps
# 1. Obtener el número de casos de prueba `TC`
# 2. Por cada caso de prueba, obtener el siguiente string "N T ...T_i"
#     - `N`: Minutos soportados por el casete
#     - `T`: Número de canciones en la lista
#     - `T_i`: Duración de la i-ésima canción (se maneja como time_list)
# 3. Obtener el número máximo de canciones que entran en `N` minutos
# 4. Imprimir el resultado con espacios


def get_max_songs(N, time_list):
    pass


TC = int(input())
for i in range(TC):
    # * time_list es el resto de la lista de tiempos
    N, T, *times_list = input().split()
    result = get_max_songs(N, times_list)
    # Imprimir el resultado con espacios
    print(result.join(" "))
