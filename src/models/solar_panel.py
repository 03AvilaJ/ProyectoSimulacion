class SolarPanel:
    def __init__(self, voltage, inverter, battery=None):
        self._voltage = voltage
        self._inverter = inverter
        self._battery = battery

    @property
    def get_voltage(self):
        return self._voltage

    @get_voltage.setter
    def set_voltage(self, new_voltage):
        self._voltage = new_voltage

    @property
    def get_inverter(self):
        return self._inverter

    @get_inverter.setter
    def set_inverter(self, new_inverter):
        self._inverter = new_inverter

    @property
    def get_battery(self):
        self._battery

    @get_battery.setter
    def set_battery(self, new_baterry):
        self._battery = new_baterry
