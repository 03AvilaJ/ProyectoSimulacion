import numpy as np
import matplotlib.pyplot as plt

def congruencial_lineal(X0, k, c, g, n):
    """Genera números pseudoaleatorios usando el método congruencial lineal."""
    x = X0  # Inicializa la semilla.
    a = 1 + 2 * k  # Calcula el multiplicador.
    m = 2**g  # Calcula el módulo.
    resultXi = []  # Lista para almacenar los Xi generados.
    resultRi = []  # Lista para almacenar los Ri generados.
    
    for _ in range(n):  # Repite el proceso n veces.
        x = (a * x + c) % m  # Calcula el siguiente valor de x.
        Ri = x / (m - 1)  # Normaliza el número para que esté en [0, 1].
        if Ri != 0 and Ri != 1:
            resultXi.append(x)
            resultRi.append(Ri)
        
    return resultXi, resultRi  # Retorna la lista de Xi y Ri generados.

# Parámetros para la generación pseudoaleatoria
X0 = 7  # Semilla inicial
k = 3  # Constante para el cálculo de 'a'
c = 5  # Constante de desplazamiento
g = 16  # Número de bits (determina el módulo)
n = 24  # Número de datos para representar 24 horas (un día)

# Generar números pseudoaleatorios
_, Ri = congruencial_lineal(X0, k, c, g, n)

# Simulación de consumo eléctrico (en kWh) basada en los números generados
consumo_medio = 1.5  # Consumo promedio en kWh
desviacion = 0.5  # Desviación estándar

# Aplicar distribución normal a los números pseudoaleatorios generados
consumo = consumo_medio + desviacion * np.array(Ri)

# Simular picos de consumo en horas de más uso (ej. 7-9 am y 6-10 pm)
for i in range(n):
    hora_del_dia = i
    if 7 <= hora_del_dia <= 9 or 18 <= hora_del_dia <= 22:
        consumo[i] += np.random.uniform(1, 2)  # Picos adicionales de 1-2 kWh

# Graficar el consumo eléctrico en 24 horas
plt.figure(figsize=(12, 6))
plt.plot(consumo, marker='o', label='Consumo (kWh)', color='green')
plt.title('Simulación del Consumo Eléctrico de una Casa en 24 Horas')
plt.xlabel('Hora del Día')
plt.ylabel('Consumo (kWh)')
plt.xticks(range(24), labels=[f'{h}:00' for h in range(24)])  # Etiquetas de las horas
plt.grid(True)
plt.legend()
plt.show()
