# 1037
# Jackub
# https://jv.umsa.bo/oj/problem.php?id=1037
# cadenas listas bucles condicionales búsqueda

# description
# Este problema se basa en el manejo de _strings_ y algo de comportamiento de listas,
# pues utilizaremos _cursores_. La idea es que nos dan:
# - un teclado con un orden específico de letras (Ej: `"qwertyuiop"`)
# - una cadena de texto (Ej: `"potato"`)
# El objetivo es encontrar la distancia mínima entre cada letra de la cadena
# de texto en el teclado, esto para todas las letras y sumarlas en total.
#
# ![teclado](https://thumbs4.imagebam.com/4a/86/3e/MEUXB4N_t.png)
#
# Para obtener la distancia mínima a la siguiente letra, nos desplazamos
# a la izquierda y derecha de la última letra encontrada.
#
# > [!INFO] Todo está controlado
# > Resaltar que en el juez, todas las entradas están controladas, es decir, la entrada de teclado y el texto a evaluar siempre serán válidos por lo que no es necesario hacer validaciones adicionales.


# steps
# 1. Leer el número de casos `T`
# 2. Para cada caso, recibir el teclado `keyboard` y la cadena de texto `text`
# 3. Inicializar la variable `total_distance` en 0
# 4. Buscar la primera letra de la cadena de texto en el teclado para comenzar
# 5. Para cada letra de la cadena de texto, buscar la distancia mínima a la siguiente letra
# 6. Sumar la distancia mínima a `total_distance`
# 7. Imprimir `total_distance`


def min_distance(keyboard, index, char):
    """
    La función retorna dos valores en una tupla (int, int):
    - la distancia entre el cursor y la letra encontrada
    - la posición de la letra encontrada
    Sin validar si la letra se encuentra en el teclado porque
    esto se garantiza en el enunciado.
    """
    cursor_left = index
    cursor_right = index

    for _ in range(len(keyboard)):
        if cursor_left >= 0:
            if keyboard[cursor_left] == char:
                return (index - cursor_left, cursor_left)
            cursor_left -= 1
        if cursor_right < len(keyboard):
            if keyboard[cursor_right] == char:
                return (cursor_right - index, cursor_right)
            cursor_right += 1
    # return (0, index)  # No debería llegar a este punto


def search_first(keyboard, char):
    """
    Busca la primera letra de la cadena de texto en el teclado
    y retorna su posición.
    No se valida si la letra se encuentra en el teclado porque
    esto se garantiza en el enunciado.
    """
    for i in range(len(keyboard)):
        if keyboard[i] == char:
            return i
    # return -1  # No debería llegar a este punto


T = int(input())
for _ in range(T):
    keyboard = input()
    text = input()
    total_distance = 0
    index = search_first(keyboard, text[0])
    for char in text[1:]:
        distance, index = min_distance(keyboard, index, char)
        total_distance += distance
    print(total_distance)
