# 1005
# Bob el jardinero
# https://jv.umsa.bo/oj/problem.php?id=1005
# facil matematicas bucles condicionales

# description
# La solución de este problema es bastante sencilla, se debe
# contar la cantidad de vocales en un string y calcular el porcentaje de cada vocal.
#
# El problema aquí radica en como redondear los valores sin utilizar la función `round` de python.
# Entonces, creamos una función `round_fix` que redondea un número a dos decimales, esto
# multiplicando el número por 100, sumando 0.5 y convirtiendo el resultado a entero, luego
# se divide entre 100 para obtener el número redondeado a dos decimales.

# steps
# 1. Obtener el número de casos de prueba `T`
# 2. Recibir un string para cada caso de prueba
# 3. Contar las vocales en cada string
# 4. Calcular el porcentaje de cada vocal `(vocal * 100 / total)`
# 5. Redondear el porcentaje a dos decimales
# 6. Imprimir el porcentaje de cada vocal en el formato `a= 0.00`


def round_fix(number):
    # recorrer dos decimales
    # Ej. 12.34 -> 12.34 * 100 -> 1234.00
    rounded = number * 100
    # redondear al entero más cercano
    # Ej. 12.2 -> 12.2 + 0.5 -> 12.7 -> 13
    rounded = int(rounded + 0.5)
    # dividir entre 100 para obtener dos decimales
    # Ej. 13 -> 13 / 100 -> 0.13
    return rounded / 100


T = int(input())
for k in range(1, T + 1):
    text = input()
    total = len(text)
    a, e, i, o, u = 0, 0, 0, 0, 0
    for char in text:
        if char == "a":
            a += 1
        elif char == "e":
            e += 1
        elif char == "i":
            i += 1
        elif char == "o":
            o += 1
        elif char == "u":
            u += 1

    print(f"Caso {k}:")
    print(f"a= {round_fix(a * 100 / total):.2f}")
    print(f"e= {round_fix(e * 100 / total):.2f}")
    print(f"i= {round_fix(i * 100 / total):.2f}")
    print(f"o= {round_fix(o * 100 / total):.2f}")
    print(f"u= {round_fix(u * 100 / total):.2f}")
