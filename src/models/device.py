class Device:
    def __init__(self, device_type, consumptiom, amount):
        self._device_type = device_type
        self._consumption = consumptiom
        self._amount = amount

    @property
    def get_device_type(self):
        return self._device_type

    @get_device_type.setter
    def set_device_type(self, new_device):
        self._device_type = new_device

    @property
    def get_consumption(self):
        return self._consumption

    @get_consumption.setter
    def set_consumption(self, new_consumption):
        self._consumption = new_consumption

    @property
    def get_amount(self):
        return self._amount

    @get_amount.setter
    def set_amount(self, new_amount):
        self._amount = new_amount
