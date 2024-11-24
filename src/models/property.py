class Property:
    def __init__(self, devices, light_consumption=None, solar_panel=None):
        self._light_consumption = light_consumption
        self._devices = devices
        self._solar_panel = solar_panel

    @property
    def get_light_consumption(self):
        return self._light_consumption

    @get_light_consumption.setter
    def set_light_consumption(self, new_consumption):
        self._light_consumption = new_consumption

    @property
    def get_devices(self):
        return self._devices

    @get_devices.setter
    def set_devices(self, new_device):
        self._devices = new_device

    @property
    def get_solar_panel(self):
        return self._solar_panel

    @get_solar_panel.setter
    def set_solar_panel(self, new_solar_panel):
        self._solar_panel = new_solar_panel
