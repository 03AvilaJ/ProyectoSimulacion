class SolarPanel:
    def __init__(
        self,
        active_area,
        efficiency,
        solar_radiaton,
        voltage,
        inverter=None,
        battery=None,
    ):
        self._active_area = active_area
        self._efficiency = efficiency
        self._solar_radiaton = solar_radiaton
        self._voltage = voltage
        self._inverter = inverter
        self._battery = battery

    @property
    def get_active_area(self):
        return self._active_area

    @get_active_area
    def set_active_area(self, new_area):
        self._active_area = new_area

    @property
    def get_efficiency(self):
        return self._efficiency

    @get_efficiency
    def set_efficiency(self, new_efficiency):
        self._efficiency = new_efficiency

    @property
    def get_solar_radiaton(self):
        return self.get_solar_radiaton

    @get_solar_radiaton
    def set_solar_radiaton(self, new_solar_radiaton):
        self._solar_radiaton = new_solar_radiaton

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
