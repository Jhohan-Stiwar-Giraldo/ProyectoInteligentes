import pygame
import numpy as np
import tkinter as tk
from tkinter import filedialog
import tkinter

class Pasajero:
    def __init__(self, id, ubicaciónOrigen, destino):
        self.id = id
        self.origen = ubicaciónOrigen
        self.destino = destino

    def __str__(self):
        return f'Pasajero {self.id}: {self.origen} -> {self.destino}'

class vehiculo:
    def __init__(self, id, ubicación, estado, combustible):
        self.id = id
        self.ubicación = ubicación
        self.estado = estado
        self.combustible = combustible
        
    def __init__(self, id, ubicación, pasajero):
        self.id = id
        self.ubicación = ubicación
        self.pasajero = pasajero

    def __str__(self):
        return f'Vehículo {self.id}: {self.ubicación}'

class ReporteViaje:
    def __init__(self, id, vehiculo, pasajero, combustibleConsumido, costo, duracion, distancia):
        self.id = id
        self.vehiculo = vehiculo
        self.pasajero = pasajero
        self.combustibleConsumido = combustibleConsumido
        self.costo = costo
        self.duracion = duracion
        self.distancia = distancia

    def __str__(self):
        return f'Reporte de viaje {self.id}: {self.vehículo} -> {self.pasajero}'

class Ruta:
    def __init__(self, id, origen, destino, distanciaTotal, duracion, puntosIntermedios, consumoCombustible):
        self.id = id
        self.origen = origen
        self.destino = destino
        self.distanciaTotal = distanciaTotal
        self.duracion = duracion
        self.puntosIntermedios = puntosIntermedios
        self.consumoCombustible = consumoCombustible

    def __str__(self):
        return f'Ruta {self.id}: {self.origen} -> {self.destino}'

class Nodo:
    def __init__(self, id, ubicación, sentido, semaforo, tiempoSemaforo):
        self.id = id
        self.ubicación = ubicación
        self.sentido = sentido
        self.semaforo = semaforo
        self.tiempoSemaforo = tiempoSemaforo
        

    def __str__(self):
        return f'Nodo {self.id}: {self.ubicación}'
    
class sistemaSimulacion:
    vehiculosRegistrados = []
    semaforos = []
    nodos = []
    pasajeros = []
    
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

mejor_movimiento = None
mejor_puntaje = float('-inf')
mejores_movimientos_min = []
mejores_movimientos_max = []

def EstadoInicial_IN():
    # Solicitar al usuario que ingrese los elementos del arreglo separados por espacios
    entrada = input("Ingresa los elementos del arreglo separados por espacios: ")

    # Convertir la entrada en una lista de enteros
    estado_inicial = list(map(int, entrada.split()))

    # Imprimir el arreglo ingresado por el usuario
    print("Arreglo ingresado:", estado_inicial)

if __name__ == "__main__":
    estado_inicial =EstadoInicial_IN();