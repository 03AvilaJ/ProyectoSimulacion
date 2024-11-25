import random

import numpy as np

from ..models import RandomGenerator
import random

# Definir la matriz de transición
states = ["Soleado", "Nublado", "Lluvia Ligera", "Lluvia Fuerte", "Tormenta"]

# Probabilidades de transición (simplificadas)
probabilities = {
    "Soleado": [0.6, 0.2, 0.1, 0.05, 0.05],
    "Nublado": [0.3, 0.4, 0.2, 0.05, 0.05],
    "Lluvia Ligera": [0.1, 0.3, 0.4, 0.15, 0.05],
    "Lluvia Fuerte": [0.05, 0.1, 0.3, 0.4, 0.15],
    "Tormenta": [0.05, 0.1, 0.2, 0.2, 0.45],
}

# Radiación por estado (en W/m²)
radiation = {
    "Soleado": 500,
    "Nublado": 300,
    "Lluvia Ligera": 100,
    "Lluvia Fuerte": 0,
    "Tormenta": 0,
}


# Función para simular el clima para N días
def simulate_weather(days, initial_state="Soleado"):
    semillas = [77,13,55,20,90,4434]
    randomP = RandomGenerator( 832262, 1013904223, 32, 500)
    Xi, num_aleatorio_arr = randomP.congruencial_lineal(random.choice(semillas))
    current_index = 0
    current_state = initial_state
    weather_log = []
    radiation_log = []

    for _ in range(days):
        weather_log.append({"Estado": current_state, "Radiación": radiation[current_state]})
        radiation_log.append(radiation[current_state])

        # Obtener las probabilidades de transición para el estado actual
        transition_probs = probabilities[current_state]
        
        # Calcular la distribución acumulada usando np.cumsum
        cumulative_probs = np.cumsum(transition_probs)

        # Obtener el siguiente número aleatorio y avanzar el índice
        rand_value = num_aleatorio_arr[current_index]  # Usar el número en la posición actual
        current_index += 1  # Avanzar al siguiente número aleatorio

        # Determinar el siguiente estado basándonos en la distribución acumulada
        for i, cumulative_prob in enumerate(cumulative_probs):
            if rand_value < cumulative_prob:
                next_state = states[i]
                break
        
        current_state = next_state  # Actualizamos el estado actual

    return weather_log


# # Simular el clima durante 30 días
simulated_weather = simulate_weather(1)
for day, weather in enumerate(simulated_weather, start=1):
    print(weather['Radiación'])

# # Mostrar los resultados
# for day, weather in enumerate(simulated_weather, start=1):
#     print(
#         f"Día {day}: Estado: {weather['Estado']}, Radiación: {weather['Radiación']} W/m²"
#     )
