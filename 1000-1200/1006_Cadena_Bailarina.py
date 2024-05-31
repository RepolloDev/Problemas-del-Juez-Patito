# 1006 - Cadena Bailarina
# https://jv.umsa.bo/oj/problem.php?id=1006

# 1. Obtener el número de casos de prueba T
# 2. Por cada caso, recibir un string
# 3. Iterar por cada letra del string
# 4. Cambiar la secuencia por MAYÚSCULA - minúscula - MAYÚSCULA - minúscula ...

# ! Si es una oración, se debe considerar los espacios. Es decir, saltar a la siguiente letra si es un espacio
# ? Se utiliza código ASCII para cambiar de mayúscula a minúscula y viceversa, pero para Python se puede utilizar `str.upper()` y `str.lower()`


T = int(input())
for _ in range(T):
    text = input()
    result = ""
    upper = True
    for char in text:
        if char == " ":
            result += " "
            continue
        if upper:
            result += char.upper()
            upper = False
        else:
            result += char.lower()
            upper = True
    print(result)
