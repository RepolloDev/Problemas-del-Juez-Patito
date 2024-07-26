# 1023
# Defense Of The Ancients
# https://jv.umsa.bo/oj/problem.php?id=1023
# grafos cadenas bucles condicionales

# description
# El problema tiene una temática con el juego DOTA, donde estudiamos
# los siguientes aspectos:
# - Hay dos equipos con máximo 6 jugadores cada uno
# - Cada jugador tiene cuatro habilidades
# - Dos jugadores tienen una batalla si **tienen al menos una habilidad en común**
#
# > [!IMPORTANT] No completado
# TODO: Obtener los subgrafos

# steps
# 1. Recibir una variable `T` que representa la cantidad de casos de prueba
# 2. Por cada caso, Recibir una variable `N` que representa la cantidad de jugadores
# 3. Por cada equipo (solo dos), recibir el string de cuatro caracteres que representa las habilidades de cada jugador


def sub_string(s1, s2):
    for c in s1:
        if c in s2:
            return True
    return False


def gen_subgraphs(graph):
    # subgraph with two nodes
    subgraphs = []
    disabled = [False] * len(graph)
    for i in range(len(graph)):
        if len(graph[i]) == 0 or disabled[i]:
            continue
        if len(graph[i]) == 1:
            disabled[graph[i][0]] = True
            disabled[i] = True
            subgraphs.append([i, graph[i][0]])
            continue


T = int(input())
for _ in range(T):
    # N <= 6 porque es la cantidad de un equipo DOTA
    N = int(input())
    teamA = input().split()
    teamB = input().split()

    graph = [[] for _ in range(2 * N)]
    # 36 iteraciones
    for i in range(N):
        for j in range(N):
            if sub_string(teamA[i], teamB[j]):
                graph[i].append(j + N)
                graph[j + N].append(i)

    subgraphs = gen_subgraphs(graph)
    print(subgraphs)