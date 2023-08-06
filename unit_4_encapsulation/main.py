class TV:
    def __init__(self):
        self.status = 'off'
        self._channel = 1
        self.__volume = 18

    def __str__(self):
        return f'TV status: {self.status}, channel: {self._channel}, volume: {self.__volume}'

    #  Getter
    @property
    def volume(self):
        return self.__volume

    # Setter
    @volume.setter
    def volume(self, volume):
        assert 0 <= volume <= 100, 'Volume must be between 0 and 100'
        self.__volume = volume

    # ANOTHER VERSION OF GETTER
    # def getVolume(self):
    #     return self.__volume
    # --------------------------------
    # ANOTHER VERSION OF SETTER
    # def setVolume(self, volume):
    #     assert 0 <= volume <= 100, 'Volume must be between 0 and 100'
    #     self.__volume = volume


tv1 = TV()
print(tv1)

print(tv1.volume)
tv1.status = 'on'
tv1._channel = 7
tv1.volume = 30

# tv1._TV__volume = 30
# tv1.setVolume(300)

print(tv1)
print(tv1.volume)
