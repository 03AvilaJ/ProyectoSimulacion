import numpy as np
import matplotlib.pyplot as plt

# Supongamos que `consumo` y `generacion_energia` son las listas de consumo y generación previas

# Calcular la cantidad de energía que debe ser provista por la red
energia_provista_por_red = []
energia_satisfecha_por_panel = []

for consumo_hora, generacion_hora in zip(consumo, generacion_energia):
    if generacion_hora >= consumo_hora:
        energia_satisfecha_por_panel.append(consumo_hora)
        energia_provista_por_red.append(0)  # Todo el consumo es cubierto por el panel
    else:
        energia_satisfecha_por_panel.append(generacion_hora)
        energia_provista_por_red.append(consumo_hora - generacion_hora)  # Diferencia que cubre la red

# Graficar el resultado
plt.figure(figsize=(14, 7))
plt.plot(consumo, marker='o', label='Consumo de la casa (kWh)', color='green')
plt.plot(generacion_energia, marker='o', label='Generación del panel solar (kWh)', color='orange')
plt.plot(energia_provista_por_red, marker='o', label='Energía provista por la red (kWh)', color='red')
plt.plot(energia_satisfecha_por_panel, marker='o', label='Energía satisfecha por el panel (kWh)', color='blue')

plt.title('Comparación de Consumo y Generación de Energía')
plt.xlabel('Hora del Día')
plt.ylabel('Energía (kWh)')
plt.xticks(range(24), labels=[f'{h}:00' for h in range(24)])
plt.grid(True)
plt.legend()
plt.show()
# Supongamos que `consumo` y `generacion_energia` son las listas de consumo y generación previas

# Calcular la cantidad de energía que debe ser provista por la red
energia_provista_por_red = []
energia_satisfecha_por_panel = []

for consumo_hora, generacion_hora in zip(consumo, generacion_energia):
    if generacion_hora >= consumo_hora:
        energia_satisfecha_por_panel.append(consumo_hora)
        energia_provista_por_red.append(0)  # Todo el consumo es cubierto por el panel
    else:
        energia_satisfecha_por_panel.append(generacion_hora)
        energia_provista_por_red.append(consumo_hora - generacion_hora)  # Diferencia que cubre la red

# Graficar el resultado
plt.figure(figsize=(14, 7))
plt.plot(consumo, marker='o', label='Consumo de la casa (kWh)', color='green')
plt.plot(generacion_energia, marker='o', label='Generación del panel solar (kWh)', color='orange')
plt.plot(energia_provista_por_red, marker='o', label='Energía provista por la red (kWh)', color='red')
plt.plot(energia_satisfecha_por_panel, marker='o', label='Energía satisfecha por el panel (kWh)', color='blue')

plt.title('Comparación de Consumo y Generación de Energía')
plt.xlabel('Hora del Día')
plt.ylabel('Energía (kWh)')
plt.xticks(range(24), labels=[f'{h}:00' for h in range(24)])
plt.grid(True)
plt.legend()
plt.show()
