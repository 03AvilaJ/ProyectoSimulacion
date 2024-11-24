import time

class RandomGenerator:
    def __init__(self, seed=None):
        self.seed = seed if seed is not None else int(time.time() * 1000)
        self.a = 1103515245  # Multiplicador grande
        self.c = 12345  # Incremento pequeño
        self.m = 2**31  # Módulo (valor grande para mayor variabilidad)

    def next(self):
        # Generar el siguiente número pseudoaleatorio
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def generate_in_range(self, min_val, max_val):
        # Mapear al rango deseado
        random_value = self.next() % (max_val - min_val + 1)
        return min_val + random_value

