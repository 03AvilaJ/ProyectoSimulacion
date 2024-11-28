from matplotlib import pyplot as plt
from matplotlib.widgets import Button
from ..models import Device, Property, RandomGenerator, SolarPanel, simulate_weather
from ..views import Menu
import random


class EnergyConsumptionSimulation:
    def __init__(self):
        self.semillas = [77, 13, 55, 20, 90, 4434]
        self.random_generator = RandomGenerator(832262, 1013904223, 32, 500)
        self.interface_menu = Menu()
        self.device_list = []
        self.consumption_list = []
        self.solar_generation_list = []
        self.consumption_list_yearly = []
        self.solar_generation_list_yearly = []

    def save_device(self):
        return self.device_list

    def generate_device(self, device_name, amount):

        Xi, num_aleatorio_nevera = self.random_generator.congruencial_lineal(
            random.choice(self.semillas)
        )
        Xi, num_aleatorio_lavadora = self.random_generator.congruencial_lineal(
            random.choice(self.semillas)
        )
        Xi, num_aleatorio_freidora = self.random_generator.congruencial_lineal(
            random.choice(self.semillas)
        )
        Xi, num_aleatorio_televisor = self.random_generator.congruencial_lineal(
            random.choice(self.semillas)
        )
        Xi, num_aleatorio_computador = self.random_generator.congruencial_lineal(
            random.choice(self.semillas)
        )
        lower_name = device_name.lower()
        new_device = ""
        if lower_name == "nevera":
            random_consume_nevera = self.random_generator.numero_dis_unirfome(
                num_aleatorio_nevera, 30, 50
            )
            random_consume = random_consume_nevera[random.randint(0, 499)]
            new_device = Device(device_name, random_consume, amount, 24)
        elif lower_name == "lavadora":
            random_consume_lavadora = self.random_generator.numero_dis_unirfome(
                num_aleatorio_lavadora, 10, 25
            )
            random_consume = random_consume_lavadora[random.randint(0, 499)]
            new_device = Device(device_name, random_consume, amount, 3)
        elif lower_name == "freidora de aire":
            random_consume_freidora = self.random_generator.numero_dis_unirfome(
                num_aleatorio_freidora, 5, 15
            )
            random_consume = random_consume_freidora[random.randint(0, 499)]
            new_device = Device(device_name, random_consume, amount, 1)
        elif lower_name == "televisor":
            random_consume_tv = self.random_generator.numero_dis_unirfome(
                num_aleatorio_televisor, 10, 20
            )
            random_consume = random_consume_tv[random.randint(0, 499)]
            new_device = Device(device_name, random_consume, amount, 3)
        elif lower_name == "computador":
            random_consume_pc = self.random_generator.numero_dis_unirfome(
                num_aleatorio_computador, 5, 20
            )
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
        Xi, num_aleatorio_efficiency = self.random_generator.congruencial_lineal(
            random.choice(self.semillas)
        )
        random_consume_efficiency = self.random_generator.numero_dis_unirfome(
            num_aleatorio_efficiency, 15, 22
        )
        random_efficiency = random_consume_efficiency[random.randint(0, 499)]
        new_solar_panel = SolarPanel(active_area, random_efficiency)

        return new_solar_panel

    def calculate_voltage(self):
        voltage = 0
        active_area = self.generate_solar_panel().get_active_area
        efficiency = self.generate_solar_panel().get_efficiency
        simulate_weather_radiation = simulate_weather(30)

        for day, weather in enumerate(simulate_weather_radiation, start=1):
            solar_radiation = weather["Radiación"]
            daily_voltage = active_area * solar_radiation * (efficiency / 100)
            voltage += daily_voltage
            average_voltage = voltage / 30
        return average_voltage

    def add_solar_panel_to_property(self, property):
        solar_panel_completed = self.generate_solar_panel()
        solar_panel_completed.set_voltage = self.calculate_voltage()
        property.set_solar_panel = solar_panel_completed

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

        return completed_property

    def temporal_build_device(self):
        self.generate_device("nevera", 1)
        self.generate_device("Lavadora", 2)
        self.generate_device("Freidora de aire", 1)
        self.generate_device("Televisor", 2)
        self.generate_device("Computador", 3)

    def simulate_daily_consumption(self, light_consumption):
        continue_simulation = True
        months = 12
        anual_consume_sum = 0
        monthly_consume = 0
        years_elapsed = 0
        solar_panel_consume_yearly = 0
        monthly_consume_yearly = 0
        solar_panel_years = light_consumption.get_solar_panel.get_shelf_life
        Xi, num_aleatorio = self.random_generator.congruencial_lineal(
            random.choice(self.semillas)
        )

        while continue_simulation and years_elapsed < solar_panel_years:
            print(continue_simulation)
            for _ in range(months):
                print("mes: ", _, " año: ", years_elapsed)
                anual_consume_sum += light_consumption.get_light_consumption
                monthly_consume += self.build_property(
                    self.generate_property()
                ).get_light_consumption
                anual_consume_sum += monthly_consume
                solar_panel_generation = self.calculate_voltage()
                solar_panel_consume_yearly += solar_panel_generation
                self.consumption_list.append(monthly_consume)
                self.solar_generation_list.append(solar_panel_generation)
                print(f"Consumo total del mes: {monthly_consume}")

                for value in self.save_device():
                    print(value.get_device_type, value.get_consumption)
                    value.set_consumption = 0
                    monthly_consume = 0
                    random_consumption1 = self.random_generator.numero_dis_unirfome(
                        num_aleatorio, 30, 50
                    )
                    self.save_device()[0].set_consumption = random_consumption1[
                        random.randint(0, 499)
                    ]
                    random_consumption2 = self.random_generator.numero_dis_unirfome(
                        num_aleatorio, 20, 35
                    )
                    self.save_device()[1].set_consumption = random_consumption2[
                        random.randint(0, 499)
                    ]
                    random_consumption3 = self.random_generator.numero_dis_unirfome(
                        num_aleatorio, 5, 15
                    )
                    self.save_device()[2].set_consumption = random_consumption3[
                        random.randint(0, 499)
                    ]
                    random_consumption4 = self.random_generator.numero_dis_unirfome(
                        num_aleatorio, 15, 30
                    )
                    self.save_device()[3].set_consumption = random_consumption4[
                        random.randint(0, 499)
                    ]
                    random_consumption5 = self.random_generator.numero_dis_unirfome(
                        num_aleatorio, 5, 20
                    )
                    self.save_device()[4].set_consumption = random_consumption5[
                        random.randint(0, 499)
                    ]
            years_elapsed += 1
            self.consumption_list_yearly.append(anual_consume_sum)
            self.solar_generation_list_yearly.append(solar_panel_consume_yearly)
            self.show_consume(
                self.consumption_list, self.solar_generation_list, years_elapsed
            )
            print(f"Consumo total del año: {anual_consume_sum}")
            print(f"Consumo total del año LISTA: {self.consumption_list_yearly}")
            print(f"Consumo total del año LISTA: {self.solar_generation_list_yearly}")
            anual_consume_sum = 0
            solar_panel_consume_yearly = 0
            self.solar_generation_list = []
        self.show_consume_yearly(
            self.consumption_list_yearly,
            self.solar_generation_list_yearly,
            years_elapsed,
        )

    def show_consume(self, list_consumption, list_solar_panel, year):
        months = [
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Diciembre",
        ]

        plt.ion()  # Activar modo interactivo
        fig, (ax1, ax2, ax3) = plt.subplots(
            3, 1, figsize=(12, 18)
        )  # Crear tres subplots verticales

        # Configuración inicial del subplot 1 (Consumo)
        ax1.set_title(f"Consumo de energía mensual. Año :{year}", fontsize=16)
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
                list_consumption[: i + 1],
                marker="o",
                color="b",
                label="Consumo de energía (kWh)",
            )
            ax1.set_title(f"Consumo de energía mensual. Año: {year}", fontsize=16)
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
                list_solar_panel[: i + 1],
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
            ax3.bar(
                months, energy_uncovered, bottom=energy_covered, color="orange"
            )  # Parte no satisfecha

            # Pausar para simular tiempo real
            fig.subplots_adjust(hspace=0.9, wspace=0.3)
            plt.pause(0.5)

        plt.ioff()  # Desactivar modo interactivo
        plt.show()  # Mostrar ambas gráficas en la misma ventana

        # self.interface_menu.show_consumption_by_month(months, self.consumption_list, self.solar_generation_list, energy_covered, energy_uncovered)

    def calculate_coverage(self):
        # Calcular los valores absolutos de energía cubierta y no cubierta
        print(f"Lista energia solar dentro de cobertura: {self.solar_generation_list}")
        energy_covered = [
            min(gen, cons)
            for gen, cons in zip(self.solar_generation_list, self.consumption_list)
        ]
        energy_uncovered = [
            cons - cov for cons, cov in zip(self.consumption_list, energy_covered)
        ]
        return energy_covered, energy_uncovered

    def show_consume_yearly(self, list_consumption, list_solar_panel, year):
        months = [
            "Año_1",
            "Año_2",
            "Año_3",
            "Año_4",
            "Año_5",
            "Año_6",
            "Año_7",
            "Año_8",
            "Año_9",
            "Año_10",
            "Año_11",
            "Año_12",
            "Año_13",
            "Año_14",
            "Año_15",
            "Año_16",
            "Año_17",
            "Año_18",
            "Año_19",
            "Año_20",
            "Año_21",
            "Año_22",
            "Año_23",
            "Año_24",
            "Año_25",
        ]

        plt.ion()  # Activar modo interactivo
        fig, (ax1, ax2, ax3) = plt.subplots(
            3, 1, figsize=(12, 18)
        )  # Crear tres subplots verticales

        # Configuración inicial del subplot 1 (Consumo)
        ax1.set_title(f"Consumo de energía mensual. Año :{year}", fontsize=16)
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
                list_consumption[: i + 1],
                marker="o",
                color="b",
                label="Consumo de energía (kWh)",
            )
            ax1.set_title(f"Consumo de energía mensual. Año: {year}", fontsize=16)
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
                list_solar_panel[: i + 1],
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
            energy_covered, energy_uncovered = self.calculate_coverage_yearly()

            # Barra apilada: energía satisfecha (verde) y energía no satisfecha (naranja)
            ax3.bar(months, energy_covered, color="g")  # Parte satisfecha
            ax3.bar(
                months, energy_uncovered, bottom=energy_covered, color="orange"
            )  # Parte no satisfecha

            # Pausar para simular tiempo real
            fig.subplots_adjust(hspace=0.9, wspace=0.3)
            plt.pause(0.5)

        plt.ioff()  # Desactivar modo interactivo
        plt.show()  # Mostrar ambas gráficas en la misma ventana

        # self.interface_menu.show_consumption_by_month(months, self.consumption_list, self.solar_generation_list, energy_covered, energy_uncovered)

    def calculate_coverage_yearly(self):
        # Calcular los valores absolutos de energía cubierta y no cubierta
        print(f"Lista energia solar dentro de cobertura: {self.solar_generation_list}")
        energy_covered = [
            min(gen, cons)
            for gen, cons in zip(
                self.solar_generation_list_yearly, self.consumption_list_yearly
            )
        ]
        energy_uncovered = [
            cons - cov
            for cons, cov in zip(self.consumption_list_yearly, energy_covered)
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
    energy_consumption.build_property(
        energy_consumption.generate_property()
    ).get_light_consumption,
)
# print(energy_consumption.calculate_voltage())

# energy_consumption.show_consume()
