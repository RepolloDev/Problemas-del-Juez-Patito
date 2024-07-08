# 1030
# Collares
# https://jv.umsa.bo/oj/problem.php?id=1030
# strings bucles

# description
# TODO: Revisar la descripcion del problema

# steps
#

from sys import stdin

for line in stdin:
    if line == "\n":
        break

    # ordenar la cadena alfabeticamente
    line = sorted(line.strip())
    print(line)
