import numpy as np
import matplotlib.pyplot as plt

# Definición de la matriz de transición de Markov
matriz_transicion = np.array([
    [0.6, 0.3, 0.1],  # Soleado
    [0.4, 0.4, 0.2],  # Nublado
    [0.2, 0.5, 0.3]   # Lluvioso
])

# Estados y energía generada (en kWh) para cada estado
estados = ['Soleado', 'Nublado', 'Lluvioso']
energia_por_estado = {
    'Soleado': (5, 7),  # Rango de generación de energía
    'Nublado': (2, 4),
    'Lluvioso': (0, 2)
}

# Simulación de 24 horas
n_horas = 24
estado_actual = 0  # Iniciar con estado 'Soleado'
generacion_energia = []

for _ in range(n_horas):
    # Generar la energía según el estado actual
    energia_min, energia_max = energia_por_estado[estados[estado_actual]]
    energia_generada = np.random.uniform(energia_min, energia_max)
    generacion_energia.append(energia_generada)
    
    # Determinar el próximo estado
    estado_actual = np.random.choice([0, 1, 2], p=matriz_transicion[estado_actual])

# Graficar la energía generada
plt.figure(figsize=(12, 6))
plt.plot(generacion_energia, marker='o', color='orange', label='Energía generada (kWh)')
plt.title('Simulación de Energía Generada por un Panel Solar en 24 Horas')
plt.xlabel('Hora del Día')
plt.ylabel('Energía Generada (kWh)')
plt.xticks(range(24), labels=[f'{h}:00' for h in range(24)])
plt.grid(True)
plt.legend()
plt.show()

