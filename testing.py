import random


class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.dice = []
        self.dice_number = 5

    def roll_dice(self):
        for i in range(self.dice_number):
            self.dice.append(random.randint(1, 6))


player = Player(1)

print(player.dice)  # Empty

player.roll_dice()

print(player.dice)  # Populated
