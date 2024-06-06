# 1003
# Rumores
# https://jv.umsa.bo/oj/problem.php?id=1003

"""
#grafos #búsqueda #bfs #recorrido #medio

! Existe un problema con el Juez en línea, por lo que no se puede verificar la solución. Sin embargo, el código es correcto.

Para este problema, se utiliza el concepto de grafos como listas de adyacencia para 
determinar si una persona puede llegar a otra, en simples palabras es verificar
si el elemento `graph[X]` contiene a `Y` o algún amigo de `Y`.

1. Obtener el número de casos de prueba `T`
2. Por cada caso, obtener el número de personas `N` y el número de relaciones `M`
3. Utilizando un grafo, obtener las relaciones entre las personas `a --> b`
4. Obtener las personas `X` e `Y`
5. Mediante un recorrido del grafo, verificar si `X` puede llegar a `Y`
6. Imprimir `"SI"` si puede llegar, `"NO"` en caso contrario
"""

from queue import Queue

def verify(graph, X, Y):
    visited = [False for _ in range(len(graph) + 1)]
    queue = Queue()
    queue.put(X)
    visited[X] = True
    while queue.qsize() > 0:
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)
    return visited[Y]

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    relations = [[] for _ in range(N + 1)]
    for j in range(M):
        u, v = map(int, input().split())
        relations[u].append(v)
    X, Y = map(int, input().split())
    result = verify(relations, X, Y)
    if result:
        print("SI")
    else:
        print("NO")