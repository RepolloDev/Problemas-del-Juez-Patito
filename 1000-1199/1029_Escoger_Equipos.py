# 1029
# Escoger Equipos
# https://jv.umsa.bo/oj/problem.php?id=1029
# facil listas matematicas bucles condicionales

# description
# El problema nos dara una lista de números que representa la capacidad de jugadores de algún juego, la idea es formar **dos equipos** tomando por capitanes a los dos jugadores con mayor capacidad, luego **se alternara la elección de jugadores entre los dos capitanes**, esto se resuelve utilizando una *bandera* para saber a que equipo le toca elegir.

# steps
# 1. Recibir datos indeterminadamente hasta que no haya más datos, es decir hasta que se presione enter.
# 2. Ordenar la lista de jugadores de mayor a menor.
# 3. Crear dos variables para almacenar la suma de las capacidades de los jugadores de cada equipo.
# 4. Crear una variable booleana para alternar la elección de jugadores entre los dos equipos.
# 5. Iterar sobre la lista de jugadores y sumar la capacidad de los jugadores a los equipos.
# 6. Imprimir la diferencia de las capacidades de los equipos.

from sys import stdin

for line in stdin:
    if line == "\n":
        break

    players = list(map(int, line.split()))
    # Se puede usar sort() o algun metodo de ordenamiento como el burbuja o seleccion
    players.sort(reverse=True)

    swap = False
    sum_1 = sum_2 = 0
    for player in players:
        if swap:
            sum_1 += player
        else:
            sum_2 += player

        swap = not swap

    result = abs(sum_1 - sum_2)
    print(result)
