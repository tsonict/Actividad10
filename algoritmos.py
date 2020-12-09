import math

def distancia_euclidiana(x_1:int, y_1:int, x_2:int, y_2:int):
    resultado = math.sqrt((pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2)))
    return resultado


def busquedaProfundidad(grafo, origen):
    if origen is None or origen not in grafo:
        return "Entrada no valida."

    recorrido = []
    pila = []

    pila.append(origen)

    while pila:
        vertice = pila.pop()

        if vertice not in recorrido:
            recorrido.append(vertice)

        if vertice not in grafo:
            continue

        for vertice in grafo[vertice]:
            pila.append(vertice)

    return recorrido

def busquedaAmplitud(grafo, origen):
    if origen is None or origen not in grafo:
        return "Entrada no valida."

    recorrido = []
    cola = []

    cola.append(origen)

    while cola:
        v = cola.pop(0)

        if v not in recorrido:
            recorrido.append(v)

        if v not in grafo:
            continue

        for vertice in grafo[v]:
            cola.append(vertice)

    return recorrido