#####Minimax#####
def evaluar_heuristica(pilas):
    xor_sum = 0
    for pila in pilas:
        xor_sum ^= pila
    return xor_sum

def terminado(pilas):
    return all(pila == 0 for pila in pilas)

def movimientos_posibles(pilas):
    movimientos = []
    for i, pila in enumerate(pilas):
        for j in range(1, pila + 1):
            nuevas_pilas = pilas[:i] + [pila - j] + pilas[i+1:]
            movimientos.append(nuevas_pilas)
    return movimientos

def minimax(pilas, profundidad, jugador_max):
    if profundidad == 0 or terminado(pilas):
        return evaluar_heuristica(pilas)

    if jugador_max:
        max_eval = float('-inf')
        for m in movimientos_posibles(pilas):
            evaluacion = minimax(m, profundidad - 1, False)
            max_eval = max(max_eval, evaluacion)
            mejores_movimientos_max.append(max_eval)
        return max_eval
    else:
        min_eval = float('inf')
        for m in movimientos_posibles(pilas):
            evaluacion = minimax(m, profundidad - 1, True)
            min_eval = min(min_eval, evaluacion)
            mejores_movimientos_min.append(min_eval)
        return min_eval

estado_inicial = [1, 4, 5]
mejor_movimiento = None
mejor_puntaje = float('-inf')
mejores_movimientos_min = []
mejores_movimientos_max = []


for m in movimientos_posibles(estado_inicial):
    puntaje = minimax(m, profundidad=3, jugador_max=True)

    if puntaje > mejor_puntaje:
        mejor_puntaje = puntaje
        mejor_movimiento = m

print("El mejor movimiento es retirar de los montones:", mejor_movimiento)
print("Puntuación asociada:", mejor_puntaje)

###A* Profesor###

import heapq

L = [
    [0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

movimientos = [(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1),(0,1),(0,-1)]

class Nodo:
    def __init__(self, x, y, padre=None):
        self.x = x
        self.y = y
        self.padre = padre
        self.g = 0
        self.h = 0
        self.f = 0
    
    def __lt__(self, otro):
        return self.f < otro.f
    
def movimientos_posibles(nodo):
    candidatos = []
    for m in movimientos:
        candidatos.append((nodo.x+m[0],nodo.y+m[1]))
    return candidatos
    
def heuristica(nodo, destino):
    return abs(nodo.x - destino.x) + abs(nodo.y - destino.y)

def es_valido(L,x,y):
    return 0 <= x < len(L) and 0 <= y < len(L[0])

def es_viable(L,x,y):
    return L[x][y] == 0

def astar(L, inicio, final):
    filas, columnas = len(L), len(L[0])
    lst_abiertos = []
    lst_cerrados = set()
    nodo_inicio = Nodo(inicio[0], inicio[1])
    nodo_destino = Nodo(final[0], final[1])
    heapq.heappush(lst_abiertos, nodo_inicio)
    
    while lst_abiertos:
        nodo_actual = heapq.heappop(lst_abiertos)
        lst_cerrados.add((nodo_actual.x, nodo_actual.y))
        
        if nodo_actual.x == nodo_destino.x and nodo_actual.y == nodo_destino.y:
            camino = []
            while nodo_actual:
                camino.append((nodo_actual.x, nodo_actual.y))
                nodo_actual = nodo_actual.padre
            return camino[::-1]
        
        candidatos = movimientos_posibles(nodo_actual)
        for c in candidatos:
            x, y = c
            if es_valido(L,x,y) and es_viable(L,x,y) and (x, y) not in lst_cerrados:
                nodo_candidato = Nodo(x, y, nodo_actual)
                nodo_candidato.g = nodo_actual.g + 1
                nodo_candidato.h = heuristica(nodo_candidato, nodo_destino)
                nodo_candidato.f = nodo_candidato.g + nodo_candidato.h
                heapq.heappush(lst_abiertos, nodo_candidato)
                lst_cerrados.add((x, y))
    
    return None

inicio = (0, 0)
destino = (4, 4)
camino = astar(L, inicio, destino)
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino.")



###Dijkstra###

import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    min_heap = [(0, start)]  # (cost, (row, col))
    visited = set()
    
    while min_heap:
        cost, (row, col) = heapq.heappop(min_heap)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if (row, col) == end:
            return cost
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                next_cost = cost + matrix[r][c]
                heapq.heappush(min_heap, (next_cost, (r, c)))
    return float("inf")

# Example usage:
matrix = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
start = (0, 0)  # Starting node
end = (2, 2)  # Destination node
print(dijkstra(matrix, start, end))



###A*###

def a_estrella(inicio, objetivo, heuristica):
    frontera = PriorityQueue()
    frontera.put(inicio, 0)
    costo = {inicio: 0}
    camino = {inicio: None}

    while not frontera.empty():
        actual = frontera.get()

        if actual == objetivo:
            break

        for siguiente in grafo[actual]:
            nuevo_costo = costo[actual] + grafo[actual][siguiente]

            if siguiente not in costo or nuevo_costo < costo[siguiente]:
                costo[siguiente] = nuevo_costo
                prioridad = nuevo_costo + heuristica(siguiente, objetivo)
                frontera.put(siguiente, prioridad)
                camino[siguiente] = actual

    return camino, costo

def heuristica(nodo, objetivo):
    return abs(nodo[0] - objetivo[0]) + abs(nodo[1] - objetivo[1])
