from matplotlib import pyplot as plt
from ..models import Device, Property, RandomGenerator, SolarPanel, simulate_weather
from ..views import Menu
import random


class EnergyConsumptionSimulation:
    def __init__(self):
        self.semillas = [77,13,55,20,90,4434]
        self.random_generator = RandomGenerator(832262, 1013904223, 32, 500)
        self.interface_menu = Menu()
        self.device_list = []
        self.consumption_list = []
        self.solar_generation_list = []

    def save_device(self):
        return self.device_list

    def generate_device(self, device_name, amount):
        
        Xi, num_aleatorio_nevera = self.random_generator.congruencial_lineal(random.choice(self.semillas))
        Xi, num_aleatorio_lavadora = self.random_generator.congruencial_lineal(random.choice(self.semillas))
        Xi, num_aleatorio_freidora = self.random_generator.congruencial_lineal(random.choice(self.semillas))
        Xi, num_aleatorio_televisor = self.random_generator.congruencial_lineal(random.choice(self.semillas))
        Xi, num_aleatorio_computador = self.random_generator.congruencial_lineal(random.choice(self.semillas))
        lower_name = device_name.lower()
        new_device = ""
        if lower_name == "nevera":
            random_consume_nevera = self.random_generator.numero_dis_unirfome(num_aleatorio_nevera,30, 50)
            random_consume = random_consume_nevera[random.randint(0, 499)]
            new_device = Device(device_name, random_consume, amount, 24)
        elif lower_name == "lavadora":
            random_consume_lavadora = self.random_generator.numero_dis_unirfome(num_aleatorio_lavadora,5, 10)
            random_consume = random_consume_lavadora[random.randint(0, 499)]
            new_device = Device(device_name, random_consume, amount, 3)
        elif lower_name == "freidora de aire":
            random_consume_freidora = self.random_generator.numero_dis_unirfome(num_aleatorio_freidora,2, 5)
            random_consume = random_consume_freidora[random.randint(0, 499)]
            new_device = Device(device_name, random_consume, amount, 1)
        elif lower_name == "televisor":
            random_consume_tv = self.random_generator.numero_dis_unirfome(num_aleatorio_televisor,10, 20)
            random_consume = random_consume_tv[random.randint(0, 499)]
            new_device = Device(device_name, random_consume, amount, 3)
        elif lower_name == "computador":
            random_consume_pc = self.random_generator.numero_dis_unirfome(num_aleatorio_computador,10, 30)
            random_consume = random_consume_pc[random.randint(0, 499)]
            new_device = Device(device_name, random_consume, amount, 8)
        self.device_list.append(new_device)
        return new_device.get_device_type, new_device.get_consumption

    def generate_property(self):
        new_property = Property(self.save_device())
        return new_property

    def calculate_monthly_consumption(self, property):
        total_consume = 0
        for value in property.get_devices:
            total_consume += value.get_consumption
        property.set_light_consumption = total_consume
        return total_consume

    def generate_solar_panel(self, active_area=1.6):
        Xi, num_aleatorio_efficiency = self.random_generator.congruencial_lineal(random.choice(self.semillas))
        random_consume_efficiency = self.random_generator.numero_dis_unirfome(num_aleatorio_efficiency,15, 22)
        random_efficiency = random_consume_efficiency[random.randint(0, 499)]
        new_solar_panel = SolarPanel(active_area, random_efficiency)

        return new_solar_panel

    def calculate_voltage(self):
        voltage = 0
        active_area = self.generate_solar_panel().get_active_area
        efficiency = self.generate_solar_panel().get_efficiency
        simulate_weather_radiation = simulate_weather(30)

        self.solar_generation_list = []  # Reiniciar la lista para una nueva simulación

        for day, weather in enumerate(simulate_weather_radiation, start=1):
            solar_radiation = weather["Radiación"]
            daily_voltage = active_area * solar_radiation * (efficiency / 100)
            voltage += daily_voltage
            self.solar_generation_list.append(daily_voltage)  # Guardar generación diaria

        average_voltage = voltage / 30
        return f"Voltaje promedio del panel al mes: {average_voltage}kWh"

    def add_solar_panel_to_property(self, property):
        property.set_solar_panel = self.generate_solar_panel()

    def build_property(self, property_under_construction):
        self.calculate_monthly_consumption(property_under_construction)
        self.add_solar_panel_to_property(
            property_under_construction
        )  # Recordar que es opcional
        completed_property = Property(
            property_under_construction.get_devices,
            property_under_construction.get_light_consumption,
            property_under_construction.get_solar_panel,
        )

        return completed_property.get_light_consumption

    def temporal_build_device(self):
        self.generate_device("nevera", 1)
        self.generate_device("Lavadora", 2)
        self.generate_device("Freidora de aire", 1)
        self.generate_device("Televisor", 2)
        self.generate_device("Computador", 3)

    def simulate_daily_consumption(self, light_consumption):
        months = 12
        anual_consume_sum = 0
        monthly_consume = 0
        Xi, num_aleatorio = self.random_generator.congruencial_lineal(random.choice(self.semillas))

        for _ in range(months):
            print("mes: ", _)
            anual_consume_sum += light_consumption
            monthly_consume += self.build_property(self.generate_property())
            self.consumption_list.append(monthly_consume)
            print(f"Consumo total del mes: {monthly_consume}")
            for value in self.save_device():
                print(value.get_device_type, value.get_consumption)

                value.set_consumption = 0
                monthly_consume = 0
                random_consumption1 = self.random_generator.numero_dis_unirfome(num_aleatorio,30, 50)               
                self.save_device()[0].set_ = (                   
                    random_consumption1[random.randint(0, 499)]
                )
                random_consumption2 = self.random_generator.numero_dis_unirfome(num_aleatorio,5, 10)    
                self.save_device()[1].set_consumption = (
                    random_consumption2[random.randint(0, 499)]
                )
                random_consumption3 = self.random_generator.numero_dis_unirfome(num_aleatorio,2, 5)    
                self.save_device()[2].set_consumption = (
                    random_consumption3[random.randint(0, 499)]
                )
                random_consumption4 = self.random_generator.numero_dis_unirfome(num_aleatorio,10, 20)   
                self.save_device()[3].set_consumption = (
                    random_consumption4[random.randint(0, 499)]
                )
                random_consumption5 = self.random_generator.numero_dis_unirfome(num_aleatorio,10, 30)   
                self.save_device()[4].set_consumption = (
                    random_consumption5[random.randint(0, 499)]
                )
        print(f"Consumo total del año: {anual_consume_sum}")


    def show_consume(self):
        months = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre",
        ]
        

        plt.ion()  # Activar modo interactivo
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 18))  # Crear tres subplots verticales

        # Configuración inicial del subplot 1 (Consumo)
        ax1.set_title("Consumo de energía mensual", fontsize=16)
        ax1.set_xlabel("Meses", fontsize=14)
        ax1.set_ylabel("Consumo (kWh)", fontsize=14)
        ax1.grid(True, linestyle="--", alpha=0.6)
        ax1.set_xticks(range(len(months)))
        ax1.set_xticklabels(months, rotation=45, fontsize=12)
        ax1.set_xlim(-1, len(months))

        # Configuración inicial del subplot 2 (Generación solar)
        ax2.set_title("Generación de energía solar mensual", fontsize=16)
        ax2.set_xlabel("Meses", fontsize=14)
        ax2.set_ylabel("Generación (kWh)", fontsize=14)
        ax2.grid(True, linestyle="--", alpha=0.6)
        ax2.set_xticks(range(len(months)))
        ax2.set_xticklabels(months, rotation=45, fontsize=12)
        ax2.set_xlim(-1, len(months))

        for i in range(len(months)):
            # Actualizar el subplot 1 con los datos de consumo
            

            ax1.clear()
            ax1.plot(
                months[: i + 1],
                self.consumption_list[: i + 1],
                marker="o",
                color="b",
                label="Consumo de energía (kWh)",
            )
            ax1.set_title("Consumo de energía mensual", fontsize=16)
            ax1.set_xlabel("Meses", fontsize=14)
            ax1.set_ylabel("Consumo (kWh)", fontsize=14)
            ax1.grid(True, linestyle="--", alpha=0.6)
            ax1.set_xticks(range(len(months)))
            ax1.set_xticklabels(months, rotation=45, fontsize=12)
            ax1.set_xlim(-1, len(months))
            ax1.legend(fontsize=12)

            # Actualizar el subplot 2 con los datos de generación solar
            ax2.clear()
            ax2.plot(
                months[: i + 1],
                self.solar_generation_list[: i + 1],
                marker="o",
                color="g",
                label="Generación de energía solar (kWh)",
            )
            ax2.set_title("Generación de energía solar mensual", fontsize=16)
            ax2.set_xlabel("Meses", fontsize=14)
            ax2.set_ylabel("Generación (kWh)", fontsize=14)
            ax2.grid(True, linestyle="--", alpha=0.6)
            ax2.set_xticks(range(len(months)))
            ax2.set_xticklabels(months, rotation=45, fontsize=12)
            ax2.set_xlim(-1, len(months))
            ax2.legend(fontsize=12)

            
            
            # Configuración del subplot 3 (Energía satisfecha y no satisfecha mensual)
            ax3.set_title("Energía satisfecha y no satisfecha mensual", fontsize=16)
            ax3.set_xlabel("Meses", fontsize=14)
            ax3.set_ylabel("Energía (kWh)", fontsize=14)
            ax3.grid(True, linestyle="--", alpha=0.6)
            ax3.set_xticks(range(len(months)))
            ax3.set_xticklabels(months, rotation=45, fontsize=12)

            # Recalcular energía cubierta y no cubierta en cada iteración
            energy_covered, energy_uncovered = self.calculate_coverage()

            # Barra apilada: energía satisfecha (verde) y energía no satisfecha (naranja)
            ax3.bar(months, energy_covered, color="g")  # Parte satisfecha
            ax3.bar(months, energy_uncovered, bottom=energy_covered, color="orange")  # Parte no satisfecha
            
            # Pausar para simular tiempo real
            plt.pause(0.5)


        plt.ioff()  # Desactivar modo interactivo
        plt.show()  # Mostrar ambas gráficas en la misma ventana
        
        #self.interface_menu.show_consumption_by_month(months, self.consumption_list, self.solar_generation_list, energy_covered, energy_uncovered)

    def calculate_coverage(self):
        # Calcular los valores absolutos de energía cubierta y no cubierta
        energy_covered = [
            min(gen, cons) for gen, cons in zip(self.solar_generation_list, self.consumption_list)
        ]
        energy_uncovered = [
            cons - cov for cons, cov in zip(self.consumption_list, energy_covered)
        ]
        return energy_covered, energy_uncovered



energy_consumption = EnergyConsumptionSimulation()

energy_consumption.temporal_build_device()
print(
    energy_consumption.simulate_daily_consumption(
        energy_consumption.build_property(energy_consumption.generate_property())
    )
)

print(
    "Energia: ",
    energy_consumption.build_property(energy_consumption.generate_property()),
)
print(energy_consumption.calculate_voltage())

energy_consumption.show_consume()
