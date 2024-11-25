from scipy.stats import norm
import numpy as np
from scipy.stats import chi2
from scipy.stats import kstest
from collections import Counter

class RandomGenerator:
    def __init__(self, k, c, g, n):
        # Inicializamos los parámetros en el constructor
        self.k = k
        self.c = c
        self.g = g
        self.n = n

    def congruencial_lineal(self, semilla):
        x = semilla  # Inicializa la semilla.
        a = 1 + 2 * self.k  # Calcula el multiplicador.
        m = 2**self.g  # Calcula el módulo.
        resultXi = []  # Lista para almacenar los Xi generados.
        resultRi = []  # Lista para almacenar los Ri generados.
        
        for _ in range(self.n):  # Repite el proceso n veces.
            x = (a * x + self.c) % m  # Calcula el siguiente valor de x.
            Ri = x / (m - 1)  # Normaliza el número para que esté en [0, 1].   
            if Ri != 0 and Ri != 1:   
                resultXi.append(x) 
                resultRi.append(Ri)
        
        return resultXi, resultRi  # Retorna el último Ri y la lista de resultados.

    def numero_dis_unirfome(self, RiGenerados, min_val=0, max_val=1):
        totalNumeros = len(RiGenerados)
        result = []  # Lista para almacenar los resultados generados.
        for i in range(totalNumeros):
            Ni = min_val + (max_val - min_val) * RiGenerados[i]  # Escala al rango [min_val, max_val].
            result.append(Ni)  # Agrega el número generado a la lista de resultados.
        return result

    def numero_dis_normal(self, RiGenerados,media=0, desviacion=1, min_val=0, max_val=1):
        # Asegurarse de que RiGenerados esté en el rango (0, 1)
        RiGenerados = np.clip(RiGenerados, 1e-10, 1 - 1e-10)  # Ajuste de rango
        
        # Transformar R_i a N_i usando la función inversa de la distribución normal
        N_i = norm.ppf(RiGenerados, loc=self.media, scale=self.desviacion)
        
        return N_i

    def prueba_de_medias(self, datos):
        n = len(datos)
        media_observada = np.mean(datos)
        z0 = 1.96  # Valor crítico para un nivel de confianza del 95%
        
        # Cálculo de los límites inferior y superior del intervalo de confianza
        LI = 0.5 - z0 * (1 / np.sqrt(12 * n))
        LS = 0.5 + z0 * (1 / np.sqrt(12 * n))
        
        cumple = LI <= media_observada <= LS  # Verificar si la media está dentro del intervalo
        
        return cumple

    def prueba_de_varianza(self, numeros): 
        n = len(numeros)
        varianza_observada = np.var(numeros, ddof=1)  # Varianza muestral (ddof=1)
        
        alfa = 0.05
        chi_a2 = chi2.ppf(alfa / 2, n - 1)  # Valor crítico para alfa/2
        chi_1_a2 = chi2.ppf(1 - alfa / 2, n - 1)  # Valor crítico para 1 - alfa/2
        
        # Cálculo de los límites inferior y superior del intervalo de confianza para la varianza
        LI = (n - 1) * varianza_observada / chi_1_a2
        LS = (n - 1) * varianza_observada / chi_a2
        
        cumple = LI <= 1/12 <= LS  # Verificar si la varianza teórica (1/12) está dentro del intervalo
        
        return cumple

    # Función para calcular el número de intervalos usando la regla de Sturges
    def calcular_numero_intervalos(self, n):
        return int(1 + 3.322 * np.log10(n))

    def prueba_ks(self, numeros_generados):
        n_intervalos = self.calcular_numero_intervalos(len(numeros_generados))
        # Realizar la prueba KS con la distribución uniforme [0, 1]
        estadistico_ks, p_valor = kstest(numeros_generados, 'uniform')

        # Valor crítico Dcrit para un nivel de significancia del 5%
        Dcrit = 1.36 / np.sqrt(len(numeros_generados))

        # Verificar si Dmax cumple con la prueba
        if estadistico_ks < Dcrit:
            return True
        else:
            return False

    def prueba_chi_cuadrado(self, numeros_generados, alpha=0.05):
        """Realiza la prueba de Chi-cuadrado y retorna el valor calculado y el resultado de la prueba."""
        num_intervals = self.calcular_numero_intervalos(len(numeros_generados))

        # Calcular la frecuencia observada
        intervalos = np.linspace(0, 1, num_intervals + 1)
        frecuencias_observadas, _ = np.histogram(numeros_generados, bins=intervalos)

        # Calcular la frecuencia esperada
        n = sum(frecuencias_observadas)
        frecuencia_esperada = n / num_intervals  # Asumiendo distribución uniforme

        # Calcular Chi-cuadrado
        chi_cuadrado = sum((fo - frecuencia_esperada) ** 2 / frecuencia_esperada for fo in frecuencias_observadas)

        # Determinar los grados de libertad
        grados_de_libertad = num_intervals - 1

        # Calcular el valor crítico
        valor_critico = chi2.ppf(1 - alpha, grados_de_libertad)

        # Verificar si se cumple la prueba de Chi-cuadrado
        if chi_cuadrado < valor_critico:
            return True
        else:
            return False

    def prueba_poker(self, datos, alpha=0.05):
        # Convertir los números a 4 dígitos significativos
        digitos = [str(x).replace('.', '')[:5] for x in datos]

        # Contar las frecuencias de cada patrón (par, trio, etc.)
        patrones = []
        for digito in digitos:
            cuenta_digitos = Counter(digito)
            if len(cuenta_digitos) == 1:  # Todos los dígitos son iguales
                patrones.append("Quintilla")
            elif len(cuenta_digitos) == 2:  # 4 iguales o 3 iguales + 2 iguales
                patrones.append("Poker" if 4 in cuenta_digitos.values() else "Full")
            elif len(cuenta_digitos) == 3:  # 3 iguales o 2 pares
                patrones.append("Trio" if 3 in cuenta_digitos.values() else "Doble Par")
            elif len(cuenta_digitos) == 4:  # Un par
                patrones.append("Un Par")
            else:
                patrones.append("Diferentes")
        
        # Frecuencia observada de los patrones
        frec_obs = Counter(patrones)

        # Probabilidades teóricas para una distribución uniforme
        n = len(datos)
        probabilidades_esperadas = {
            "Quintilla": 0.0001,
            "Poker": 0.0012,
            "Full": 0.0090,
            "Trio": 0.0720,
            "Doble Par": 0.1080,
            "Un Par" : 0.5040,
            "Diferentes": 0.3024
        }

        # Frecuencias esperadas para cada patrón
        frec_esp = {patron: prob * n for patron, prob in probabilidades_esperadas.items()}

        # Asegurarnos de que las claves de los observados tengan valor 0 si no aparecen
        for patron in frec_esp.keys():
            if patron not in frec_obs:
                frec_obs[patron] = 0

        # Calcular Chi-cuadrado
        chi_cuadrado = sum(
            (frec_obs[patron] - frec_esp[patron]) ** 2 / frec_esp[patron]
            for patron in frec_esp
        )

        # Grados de libertad (número de categorías - 1)
        grados_de_libertad = len(frec_esp) - 1

        # Valor crítico de Chi-cuadrado para el nivel de significancia alpha
        valor_critico = chi2.ppf(1 - alpha, grados_de_libertad)

        # Determinar si la prueba se cumple
        return chi_cuadrado < valor_critico
