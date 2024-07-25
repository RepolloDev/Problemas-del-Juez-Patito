# 1025
# Habilidad Mental
# https://jv.umsa.bo/oj/problem.php?id=1025
# facil hashmap matematicas bucles condicionales

# description
# Para este ejercicio se hace uso del concepto de distancia
# entre puntos en un plano cartesiano.
#
# $$
# d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
# $$
#
# > [!note] Sobre el código
# > En el código se utiliza el valor `min_distance = maxsize` para inicializar la variable que guardará la distancia minima, inicialmente es el valor máximo posible para que puede ser reemplazado por cualquier valor menor.

# steps
# 1. Recibir la cantidad de puntos `N` en la pantalla
# 2. Recibir `N` lineas de entrada, donde cada linea tiene los valores `x` `y` `color`
# 3. Castear los valores `x` y `y` a enteros y el color a string
# 4. Guardar los valores en un diccionario, donde la clave es el color y el valor es una lista de tuplas con las coordenadas
# 5. Ordenar el diccionario por clave
# 6. Iterar sobre el diccionario
# 7. Por cada color, calcular la distancia minima entre la lista de coordenadas
# 8. Imprimir el color y la distancia minima

from sys import maxsize


def get_distance(coord_1: tuple[int], coord_2: tuple[int]):
    x1, y1 = coord_1
    x2, y2 = coord_2
    return pow(pow(x2 - x1, 2) + pow(y2 - y1, 2), 0.5)


def min_distance(values: list[int]):
    # Maximo valor posible en un sistema de 64 bits
    min_distance = maxsize
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            distance = get_distance(values[i], values[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance


N = int(input())
values = dict()

for i in range(N):
    params = input().split()
    coords = tuple(map(int, params[:2]))
    color = params[2]

    if color not in values:
        values[color] = [coords]
        continue
    values[color].append(coords)

values = dict(sorted(values.items()))
for key, value in values.items():
    print(f"{key} {min_distance(value):.2f}")
