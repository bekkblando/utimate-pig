import random


class Player:

    def __init__(self, number_of_rolls=1, strategy=0):
        self.number_of_rolls = number_of_rolls
        self.player_points = 0
        self.strategy = strategy

    def roll_turn(self):
        if not self.strategy:
            turn = 0
            for number in range(self.number_of_rolls):
                value = self.roll()
                if value == 1:
                    return 0
                else:
                    turn += value
            return turn

    def roll(self):
        return random.randint(1, 6)


class Strategy_player(Player):

    def roll_turn(self):
        pass


class Game:

    def turn(self, player1):
        turn = player1.roll_turn()
        player1.player_points += turn
        return player1.player_points

    def check_player_win():
        pass

    def stop():
        pass
