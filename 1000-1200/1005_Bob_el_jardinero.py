# 1005
# Bob el jardinero
# https://jv.umsa.bo/oj/problem.php?id=1005

"""
#pruebas #facil #matematicas #bucles #condicionales

! Solución incompleta - Solo para referencia

1. Obtener el número de casos de prueba T
2. Recibir un string para cada caso de prueba
3. Contar las vocales en cada string
4. Calcular el porcentaje de cada vocal (vocal * 100 / total)

! En el for se utiliza `k` para no tener un conflicto de variables entre el enumerador y la vocal `ì`

? Si se utiliza en el Juez para verificar, dará "Respuesta incorrecta", para la traducción c++ funciona correctamente
"""

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
    print(f"a= {(a * 100 / total, 2):.2f}")
    print(f"e= {(e * 100 / total, 2):.2f}")
    print(f"i= {(i * 100 / total, 2):.2f}")
    print(f"o= {(o * 100 / total, 2):.2f}")
    print(f"u= {(u * 100 / total, 2):.2f}")
