from ..models import Device, Property, RandomGenerator, SolarPanel, simulate_weather


class EnergyConsumptionSimulation:
    def __init__(self):
        self.random_generator = RandomGenerator()
        self.device_list = []

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

    def get_radiation(self):
        simulate_weather_radiation = simulate_weather(30)
        for day, weather in enumerate(simulate_weather_radiation, start=1):

            return weather["Radiación"]

    def generate_solar_panel(self, active_area=1.6):
        random_efficiency = self.random_generator.generate_in_range(15, 22)
        radiation = self.get_radiation()
        new_solar_panel = SolarPanel(active_area, random_efficiency, radiation)

        return (
            new_solar_panel.get_active_area,
            new_solar_panel.get_efficiency,
            new_solar_panel.get_solar_radiaton,
        )

    def add_solar_panel_to_property(self, property):
        property.set_solar_panel = self.generate_solar_panel()

    def build_property(self, property_under_construction):
        light_consumption = self.calculate_monthly_consumption(
            property_under_construction
        )
        solar_panel = self.add_solar_panel_to_property(
            property_under_construction
        )  # Recordar que es opcional
        completed_property = Property(
            property_under_construction.get_devices, light_consumption, solar_panel
        )

        return completed_property


energy_consumption = EnergyConsumptionSimulation()
print(energy_consumption.generate_device("nevera", 1))
print(energy_consumption.generate_device("Lavadora", 2))
print(energy_consumption.generate_device("Freidora de aire", 1))
print(energy_consumption.generate_device("Televisor", 2))
print(energy_consumption.generate_device("Computador", 3))
# print(energy_consumption.save_device())
# print(
#     "Consumo de un mes: ",
#     energy_consumption.calculate_monthly_consumption(
#         energy_consumption.generate_property()
#     ),
# )

# print(energy_consumption.generate_solar_panel())
# energy_consumption.add_solar_panel_to_property(energy_consumption.generate_property())
# print(energy_consumption.generate_property().get_solar_panel)