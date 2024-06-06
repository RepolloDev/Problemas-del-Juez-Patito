# 1011
# Futbol
# https://jv.umsa.bo/oj/problem.php?id=1011

"""
#math #bucles #facil

Para este caso es necesario utilizar la fórmula de la distancia entre dos puntos en un plano cartesiano.

$$
Distancia = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}s
$$

1. Recibir el número (`N`) de jugadores del equipo
2. Por cada jugador, recibir las coordenadas `x`, `y`
3. Recibir el número de consultas `Q`
4. Por cada consulta, recibir los jugadores a operar
5. Calcular la distancia entre los jugadores
"""

N = int(input())

# Cada jugador tiene una tupla (x, y)
# ! Se comienza desde el 1 (porque los jugadores son de 1 a N)
players = [(0, 0)] * (N + 1)
for i in range(N):
    x, y = map(int, input().split())
    players[i + 1] = (x, y)

Q = int(input())

for i in range(Q):
    p1, p2 = map(int, input().split())
    distance = (
        (players[p1][0] - players[p2][0]) ** 2 + (players[p1][1] - players[p2][1]) ** 2
    ) ** 0.5
    print(f"{distance:.2f}")
