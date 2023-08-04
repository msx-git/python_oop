class Player:
    maxHearts = 3

    def __init__(self, name):
        self.name = name
        self.hearts = Player.maxHearts

    def __str__(self):
        return f'Player: name-{self.name}, hearts-{self.hearts}'

    def loose(self):
        self.hearts -= 1
        if self.hearts > 0:
            print(f'You died, {self.hearts} heart left')
        else:
            print('Game Over')


p1 = Player('Player-1')
print(p1)
p1.loose()
p1.loose()
p1.loose()
