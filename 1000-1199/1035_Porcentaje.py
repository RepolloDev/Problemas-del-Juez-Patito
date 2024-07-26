# 1035
# Porcentaje
# https://jv.umsa.bo/oj/problem.php?id=1035
# cadenas facil ascii bucles condicionales

# description
# El problema se basas en remplazar los caracteres especiales por su valor en ASCII,
# simplemente iteramos en la entrada para remplazar por su valor en ASCII.
#
# > [!TIP] Solución rápida
# > Se puede resolver utilizando el método `str.maketrans` para crear una _traducción_, aplicando directamente a la cadena de entrada con el método `translate`.
# > Más información en [W3Schools](https://www.w3schools.com/python/ref_string_maketrans.asp)

# steps
# 1. Crear un diccionario con los caracteres especiales y su valor en ASCII
# 2. Recibir lineas de entrada hasta que se reciba un `#`
# 3. Iterar en cada caracter de la linea de entrada
# 4. Obtener el valor del caracter en el diccionario, si no existe el caracter se mantiene igual `get(llave, valor_por_defecto)`
# 5. Imprimir el resultado

from sys import stdin, stdout

# chars = str.maketrans({ ... })
chars = {
    " ": "%20",
    "!": "%21",
    "$": "%24",
    "%": "%25",
    "(": "%28",
    ")": "%29",
    "*": "%2a",
}

for line in stdin:
    if line == "#":
        break
    # stdout.write(line.translate(chars))
    result = ""
    for c in line:
        result += chars.get(c, c)
    stdout.write(result)
