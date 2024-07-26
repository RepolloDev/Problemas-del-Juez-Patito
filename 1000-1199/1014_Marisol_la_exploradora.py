# 1014
# Marisol la exploradora
# https://jv.umsa.bo/oj/problem.php?id=1014
# grafos recorrido bucles condicionales dificil

# description
# Este problema se basa en el recorrido de nodos de un grafo, se tiene un grafo dirigido y se debe verificar si se puede llegar a todos los nodos desde un nodo inicial.
#
# > [!WARNING] Solución no aceptada
# > La solución no es aceptada por el juez en línea por temas de límites de tiempo, se debe optimizar el código para que pueda ser aceptado.
# TODO: Optimizar el código para que pueda ser aceptado por el juez en línea

# steps
# 1. Recibir los enteros `N` y `M` hasta una condición de parada
# 2. Verficar si `N` y `M` son diferentes a 0 (si lo es terminar de leer datos)
# 3. Recibir `M` lineas, dos enteros `X`, `Y` que representa que desde el lugar `X` se puede llegar a `Y`
# 4. Guardar el valor de `Y` en una lista de adyacencia de `X`
# 5. Recorrer el grafo mediante bfs desde cualquier nodo (para el caso desde el nodo 0)
# 6. Si todos los nodos fueron visitados imprimir "SI" en caso contrario "NO"
# 7. Verificar que desde cualquier nodo se pueda llegar a todos los nodos

from queue import Queue
from sys import stdin, stdout


def bfs(grafo, nodo=0):
    visitados = [False] * len(grafo)
    q = Queue()
    q.put(nodo)
    visitados[nodo] = True

    while not q.empty():
        nodo = q.get()
        for adyacente in grafo[nodo]:
            if not visitados[adyacente]:
                q.put(adyacente)
                visitados[adyacente] = True

    # Verificar si todos en la lista de visitados son True
    return all(visitados)


for line in stdin:
    N, M = map(int, line.split())
    if N == 0 and M == 0:
        break

    relaciones = [[] for _ in range(N)]
    for i in range(M):
        X, Y = map(int, input().split())
        # Se lo guarda con X-1 y Y-1 para normalizar los indices
        # ya que en el problema se empieza a contar desde 1
        # y en python se empieza a contar desde 0
        relaciones[X - 1].append(Y - 1)

    results = [bfs(relaciones, i) for i in range(N)]
    if all(results):
        stdout.write("SI\n")
    else:
        stdout.write("NO\n")
