import random

# Definir la matriz de transición
transition_matrix = {
    "Soleado": ["Soleado", "Nublado", "Lluvia Ligera", "Lluvia Fuerte", "Tormenta"],
    "Nublado": ["Soleado", "Nublado", "Lluvia Ligera", "Lluvia Fuerte", "Tormenta"],
    "Lluvia Ligera": [
        "Soleado",
        "Nublado",
        "Lluvia Ligera",
        "Lluvia Fuerte",
        "Tormenta",
    ],
    "Lluvia Fuerte": [
        "Soleado",
        "Nublado",
        "Lluvia Ligera",
        "Lluvia Fuerte",
        "Tormenta",
    ],
    "Tormenta": ["Soleado", "Nublado", "Lluvia Ligera", "Lluvia Fuerte", "Tormenta"],
}

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
    "Soleado": 600,
    "Nublado": 400,
    "Lluvia Ligera": 100,
    "Lluvia Fuerte": 0,
    "Tormenta": 0,
}


# Función para simular el clima para N días
def simulate_weather(days, initial_state="Soleado"):
    current_state = initial_state
    weather_log = []
    radiation_log = []

    for _ in range(days):
        weather_log.append(
            {"Estado": current_state, "Radiación": radiation[current_state]}
        )

        radiation_log.append(radiation[current_state])

        # Seleccionar el siguiente estado basado en las probabilidades
        next_state = random.choices(
            transition_matrix[current_state], probabilities[current_state]
        )[0]
        current_state = next_state

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
