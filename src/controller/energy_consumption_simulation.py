from ..models import Device, Property, RandomGenerator, SolarPanel, simulate_weather
from ..views import Menu


class EnergyConsumptionSimulation:
    def __init__(self):
        self.random_generator = RandomGenerator()
        self.interface_menu = Menu()
        self.device_list = []
        self.consumption_list = []

    def save_device(self):
        return self.device_list

    def generate_device(self, device_name, amount):
        lower_name = device_name.lower()
        new_device = ""
        if lower_name == "nevera":
            random_consume = self.random_generator.generate_in_range(30, 50)
            new_device = Device(device_name, random_consume, amount, 24)
        elif lower_name == "lavadora":
            random_consume = self.random_generator.generate_in_range(5, 10)
            new_device = Device(device_name, random_consume, amount, 3)
        elif lower_name == "freidora de aire":
            random_consume = self.random_generator.generate_in_range(2, 5)
            new_device = Device(device_name, random_consume, amount, 1)
        elif lower_name == "televisor":
            random_consume = self.random_generator.generate_in_range(10, 20)
            new_device = Device(device_name, random_consume, amount, 3)
        elif lower_name == "computador":
            random_consume = self.random_generator.generate_in_range(10, 30)
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
        random_efficiency = self.random_generator.generate_in_range(15, 22)
        new_solar_panel = SolarPanel(active_area, random_efficiency)

        return new_solar_panel

    def calculate_voltage(self):
        voltage = 0
        active_area = self.generate_solar_panel().get_active_area
        efficiency = self.generate_solar_panel().get_efficiency
        simulate_weather_radiation = simulate_weather(30)
        for day, weather in enumerate(simulate_weather_radiation, start=1):
            solar_radiation = weather["Radiación"]
            voltage += active_area * solar_radiation * (efficiency / 100)
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
                self.save_device()[0].set_consumption = (
                    self.random_generator.generate_in_range(30, 50)
                )
                self.save_device()[1].set_consumption = (
                    self.random_generator.generate_in_range(5, 10)
                )
                self.save_device()[2].set_consumption = (
                    self.random_generator.generate_in_range(2, 5)
                )
                self.save_device()[3].set_consumption = (
                    self.random_generator.generate_in_range(10, 20)
                )
                self.save_device()[4].set_consumption = (
                    self.random_generator.generate_in_range(10, 30)
                )
        print(f"Consumo total del año: {anual_consume_sum}")


    def show_consume(self):
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
        self.interface_menu.show_consumption_by_month(months, self.consumption_list)


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
