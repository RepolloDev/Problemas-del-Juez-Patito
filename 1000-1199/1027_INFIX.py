# 1027
# INFIX
# https://jv.umsa.bo/oj/problem.php?id=1027
# medio matematicas colas bucles condicionales

# description
# > [!note] Operaciones
# > Para este caso se representa los operadores como:
# > - `S` para la suma `+`
# > - `R` para la resta `-`
# > - `M` para la multiplicación `*`
# > - `D` para la división `/`
# > - `C` para elevar al cuadrado `**2`
#
# Para este problema es necesario tomar en cuenta ciertas condiciones:
#
# - Si solo hay un número, se imprime el mismo número
# - Si hay más de un operador, se define el resultado del primero con el segundo y así sucesivamente
# - Si el numero es menor a 1, se utiliza el siguiente digito (0.9 -> 9)
#
# Para la tercera condición puede parecer confuso, pero como tal es algo necesario
# para que pueda ser aceptado por el juez en línea. Sin embargo, el proceso para que
# sea aceptado está comentado en el código porque no tiene lógica y uso más que para
# el juez en línea.

# steps
# 1. Recibir el número de casos de prueba `T`
# 2. Por cada caso, recibir la siguiente sucesión formada por:
#     - numeros enteros
#     - operadores aritméticos
# 3. Mostrar el resultado de la operación aritmética

# funciones lambda para las operaciones
operators = {
    "S": lambda x, y: x + y,
    "R": lambda x, y: x - y,
    "M": lambda x, y: x * y,
    "D": lambda x, y: x / y,
    "C": lambda x: x**2,
}

T = int(input())
for i in range(T):
    line = list(input().split())
    queue = []
    for item in line:
        if item not in operators:
            queue.append(int(item))
            continue

        if item == "C":
            element = queue.pop()
            # result = operators[item](element)
            # queue.append(round(result * 10 ,0) if result < 1 else result)
            queue.append(operators[item](element))
        else:
            element1 = queue.pop()
            element2 = queue.pop()
            # result = operators[item](element2, element1)
            # queue.append(round(result * 10 ,0) if result < 1 else result)
            queue.append(operators[item](element2, element1))

    print(int(queue[0]))
