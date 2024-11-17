class Property:
    def __init__(self, light_consumption, devices, address, city, solar_panel=None):
        self._light_consumption = light_consumption
        self._devices = devices
        self._address = address
        self._city = city
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
    def get_address(self):
        self._address

    @get_address.setter
    def set_address(self, new_address):
        self._address = new_address

    @property
    def get_city(self):
        return self._city

    @get_city.setter
    def set_city(self, new_city):
        self._city = new_city

    @property
    def get_solar_panel(self):
        return self._solar_panel

    @get_solar_panel.setter
    def set_solar_panel(self, new_solar_panel):
        self._solar_panel = new_solar_panel
