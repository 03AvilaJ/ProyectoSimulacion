from energia import FuenteEnergia, Almacenamiento, Casa, Sector  # Importa las clases necesarias
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SimulacionRedInteligente:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulación de Consumo y Eficiencia Energética en Redes Inteligentes")
        self.dias_simulacion = 30
        self.dia_actual = 0  # Contador de días
        self.resultados_dia = []

        # Inicializar componentes de energía
        self.fuente_convencional = FuenteEnergia("convencional", 1000)
        self.fuente_solar = FuenteEnergia("solar", 500)
        self.almacenamiento = Almacenamiento(500)

        # Crear casas y sectores
        casas_sector1 = [Casa(f"Casa_{i+1}", 5) for i in range(10)]
        casas_sector2 = [Casa(f"Casa_{i+1}", 8) for i in range(15)]
        self.sectores = [Sector("Sector 1", casas_sector1), Sector("Sector 2", casas_sector2)]

        # Botón de simulación
        self.btn_simular = ttk.Button(master, text="Iniciar Simulación", command=self.simular)
        self.btn_simular.pack(pady=10)

        # Canvas para gráficos
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master)
        self.canvas.get_tk_widget().pack()

    def simular(self):
        self.dia_actual = 0  # Reiniciar contador de días
        self.resultados_dia.clear()
        self.simular_dia()

    def simular_dia(self):
        if self.dia_actual < self.dias_simulacion:
            self.dia_actual += 1
            consumo_total_red = sum(sector.consumo_total() for sector in self.sectores)
            energia_convencional = self.fuente_convencional.generar_energia()
            energia_solar = self.fuente_solar.generar_energia()
            energia_total_generada = energia_convencional + energia_solar

            if energia_total_generada >= consumo_total_red:
                self.almacenamiento.almacenar_energia(energia_total_generada - consumo_total_red)
                energia_utilizada = consumo_total_red
            else:
                energia_faltante = consumo_total_red - energia_total_generada
                energia_desde_almacenamiento = self.almacenamiento.consumir_energia(energia_faltante)
                energia_utilizada = energia_total_generada + energia_desde_almacenamiento

            self.resultados_dia.append({
                'dia': self.dia_actual,
                'consumo': consumo_total_red,
                'energia_convencional': energia_convencional,
                'energia_solar': energia_solar,
                'energia_utilizada': energia_utilizada,
                'almacenamiento': self.almacenamiento.energia_actual
            })

            self.graficar_resultados()

            # Llamar a la función `simular_dia` después de 1000 ms (1 segundo)
            self.master.after(1000, self.simular_dia)

    def graficar_resultados(self):
        dias = [resultado['dia'] for resultado in self.resultados_dia]
        consumo = [resultado['consumo'] for resultado in self.resultados_dia]
        energia_convencional = [resultado['energia_convencional'] for resultado in self.resultados_dia]
        energia_solar = [resultado['energia_solar'] for resultado in self.resultados_dia]
        almacenamiento = [resultado['almacenamiento'] for resultado in self.resultados_dia]

        self.ax.clear()
        self.ax.plot(dias, consumo, label="Consumo Total (kWh)", color="blue")
        self.ax.plot(dias, energia_convencional, label="Energía Convencional (kWh)", color="orange")
        self.ax.plot(dias, energia_solar, label="Energía Solar (kWh)", color="green")
        self.ax.plot(dias, almacenamiento, label="Almacenamiento (kWh)", color="purple", linestyle="--")

        self.ax.set_title("Consumo y Generación de Energía en la Red Inteligente")
        self.ax.set_xlabel("Día")
        self.ax.set_ylabel("Energía (kWh)")
        self.ax.legend()
        self.ax.grid()
        
        self.canvas.draw()
