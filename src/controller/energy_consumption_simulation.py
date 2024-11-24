from ..models import Device, Property, RandomGenerator, SolarPanel


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


energy_consumption = EnergyConsumptionSimulation()
print(energy_consumption.generate_device("nevera", 1))
print(energy_consumption.generate_device("Lavadora", 2))
print(energy_consumption.generate_device("Freidora de aire", 1))
print(energy_consumption.generate_device("Televisor", 2))
print(energy_consumption.generate_device("Computador", 3))
# print(energy_consumption.save_device())
print(
    "Consumo de un mes: ",
    energy_consumption.calculate_monthly_consumption(
        energy_consumption.generate_property()
    ),
)
