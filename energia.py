import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FuenteEnergia:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

    def generar_energia(self):
        # Energía variable si es solar, constante si es convencional
        return random.uniform(0.5, 1.0) * self.capacidad if self.tipo == "solar" else self.capacidad

class Almacenamiento:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.energia_actual = 0

    def almacenar_energia(self, cantidad):
        self.energia_actual = min(self.capacidad, self.energia_actual + cantidad)

    def consumir_energia(self, demanda):
        energia_disponible = min(demanda, self.energia_actual)
        self.energia_actual -= energia_disponible
        return energia_disponible

class Casa:
    def __init__(self, id_casa, consumo_base):
        self.id_casa = id_casa
        self.consumo_base = consumo_base

    def consumo(self):
        return random.uniform(0.8, 1.2) * self.consumo_base

class Sector:
    def __init__(self, id_sector, casas):
        self.id_sector = id_sector
        self.casas = casas

    def consumo_total(self):
        return sum(casa.consumo() for casa in self.casas)
