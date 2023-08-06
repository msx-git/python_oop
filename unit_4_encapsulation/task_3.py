class WeatherCondition:
    def __init__(self, status, temperature):
        if status in ['sunny', 'cloudy', 'rainy', 'snowy']:
            self.__status = status
        else:
            raise ValueError('Weather status not valid')

        if temperature - 40 <= temperature <= 40:
            self.__temperature = temperature
        else:
            raise ValueError('Temperature must be between [-40 : 40]')

    def __str__(self):
        return f'Weather is {self.__status} and temperature is {self.__temperature}'

    # Getter for status
    @property
    def status(self):
        return self.__status

    # Setter for status
    @status.setter
    def status(self, status):
        assert status == 'sunny' or status == 'cloudy' or status == 'rainy' or status == 'snowy', 'Status not valid'
        self.__status = status

    # Getter for temperature
    @property
    def temp(self):
        return self.__temperature

    @temp.setter
    def temp(self, temp):
        assert -40 <= temp <= 40, 'Temperature must be between -40 and 40'
        self.__temperature = temp


# error case
# wc = WeatherCondition('very sunny', 60)

wc = WeatherCondition('rainy', 20)
print(wc)

# error case
# wc.status = 'foggy'

wc.status = 'sunny'

# error case
# wc.temp = 50

wc.temp = 30
print(wc)
