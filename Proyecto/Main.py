import numpy as np
import heapq

class Nodo:
    def __init__(self,id, vehiculo=False,  N=False, E=False, semaforo=False,  lugarTuristico=False, pasajero=False):
        
        self.id = id
        self.N = N #sentido norte sur else sur norte
        self.E=E #sentido este oeste else oeste este
        self.semaforo = semaforo #True si hay semaforo, False si no
        if (semaforo):
            self.tiempoSemaforo = 2 #tiempo de espera en semaforo 
        self.lugarTuristico = lugarTuristico #True si es lugar turistico, False si no
        self.pasajero = pasajero #True si hay pasajero, False si no
        self.vehiculo = vehiculo #True si hay vehiculo, False si no
        if(vehiculo):
            self.consumo = 1 #consumo de combustible por km
        self.g = 0
        self.h = 0
        self.f = 0

    def __str__(self):
        return f'Nodo {self.id}: {self.ubicacion} -> {self.sentido} -> {self.semaforo} -> {self.tiempoSemaforo} -> {self.lugarTuristico} -> {self.pasajero} -> {self.vehiculo}'
    
 

def interpretar_caracter(caracter):
    # Aquí definimos la lógica para interpretar un carácter y retornar las propiedades del nodo
    propiedades = {
        
        'V': {'vehiculo': True},
        'N': { 'N':True},
        'E': {'E':True},
        'S': {'semaforo': True},
        'L': {'es_lugarTuristico': True},
        'P': {'tiene_pasajero': True},
        # Añade más según sea necesario
    }
    return propiedades.get(caracter, {})

def cargar_ciudad_desde_archivo(nombre_archivo):
    ciudad = []  # Matriz que representa la ciudad
    with open("matriz.txt", 'r') as archivo:
        for fila_index, linea in enumerate(archivo):
            fila_nodos = []
            elementos = linea.strip().split(',')  # Divide por comas
            for col_index, elem in enumerate(elementos):
                propiedades = interpretar_caracter(elem)
                nodo_id = f"{fila_index}-{col_index}"  # Formar el ID del nodo
                propiedades['ubicacion'] = nodo_id  # Agregar el ID a las propiedades del nodo
                nodo = Nodo(**propiedades)
                fila_nodos.append(nodo)
            ciudad.append(fila_nodos)
    return ciudad


###Dijsktra###
def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    ###debe cambiarse por una funcion de movimientos posibles desde un nodo
    min_heap = [(0, start)]  # (cost, (row, col))
    visited = set()
    
    while min_heap:
        cost, (row, col) = heapq.heappop(min_heap)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if (row, col) == end: #end(row, col)
            return cost
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                next_cost = cost + matrix[r][c]
                heapq.heappush(min_heap, (next_cost, (r, c)))
    return float("inf")

##A*####

#movimientos = [(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1),(0,1),(0,-1)]

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

#inicio = (0, 0)
#destino = (4, 4)
#camino = astar(L, inicio, destino)
#if camino:
 #   print("Camino encontrado:", camino)
#else:
 #   print("No se encontró un camino.")


# Example usage:

start = (0, 0)  # Starting node
end = (2, 2)  # Destination node
print(dijkstra(matrix, start, end))




def recibir_matriz(n, m):
    """
    Funcion para crear una matriz de tamaño nxm.
    
    Parámetros:
    - n: Número de filas de la matriz.
    - m: Número de columnas de la matriz.
    
    Retorna:
    Una matriz de tamaño nxm con los elementos introducidos por el usuario.
    """
    
    
    matriz = []  # Inicializa una lista vacía para almacenar la matriz
    for i in range(n):
        fila = []  # Inicializa una lista vacía para la fila actual
        for j in range(m):
            # Solicita al usuario que ingrese el elemento para la posicion actual
            valor = float(input(f'Ingresa el elemento [{i}][{j}]: '))
            fila.append(valor)  # Añade el elemento a la fila actual
        matriz.append(fila)  # Añade la fila completa a la matriz
    return matriz

def leer_matriz_desde_archivo(nombre_archivo):
    """
    Funcion para leer una matriz de un archivo de texto y almacenarla en una variable.
    
    Parámetros:
    - nombre_archivo: El nombre o ruta del archivo de texto que contiene la matriz.
    
    Retorna:
    Una matriz almacenada como una lista de listas, donde cada sublista representa una fila de la matriz.
    """
    matriz = []  # Inicializa una lista vacía para almacenar la matriz
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = [str(elemento) for elemento in linea.split()]  # Convierte cada elemento a float y los añade a una lista
            matriz.append(fila)  # Añade la fila a la matriz
    return matriz


def EstadoInicial_IN():
    # Solicitar al usuario que ingrese los elementos del arreglo separados por espacios
    entrada = input("Ingresa los elementos del arreglo separados por espacios: ")

    # Convertir la entrada en una lista de enteros
    estado_inicial = list(map(int, entrada.split()))

    # Imprimir el arreglo ingresado por el usuario
    print("Arreglo ingresado:", estado_inicial)

if __name__ == "__main__":
    estado_inicial =EstadoInicial_IN();
    
    nombre_del_archivo = "matriz.txt"
    matriz = leer_matriz_desde_archivo(nombre_del_archivo)
    print(matriz)
