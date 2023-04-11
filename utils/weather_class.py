class WeatherData:
    def __init__(self, temp, unit):
        self._temp = temp
        self._unit = unit


    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = value

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value

    def  __str__(self):
        return f'{self.temp} {self.unit}'
