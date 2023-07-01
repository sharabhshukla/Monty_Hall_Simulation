import random
from enum import Enum, auto
from loguru import logger


class Door(Enum):
    DOOR1 = auto()
    DOOR2 = auto()
    DOOR3 = auto()


class Strategy(Enum):
    FLIP = auto()
    NO_FLIP = auto()


class MHSim:
    """
    This is a class that sets up a simulation for monty hall game
    """

    def __init__(self, prize_door: Door, strategy: Strategy):
        """

        :param prize_door: the door that has the car hidden behind it
        :param strategy: Type of strategy to be used, to flip or not, when the door is revealed to the player
        """
        self.prize_door = prize_door
        self.player_door = None
        self.strategy = strategy

    @staticmethod
    def flip_choice(player_door):
        """
        A static method that flip the players choice
        :param player_door: door choosen by the player
        :return: the flipped choice for the door
        """
        for door in random.sample(list(Door), len(list(Door))):
            if door != player_door:
                return door

    def simulate(self):
        """
        The method simulates the monty hall
        :return: the outcome of the gams, True if won and False when lost
        """
        self.player_door = random.choice(list(Door))
        if self.player_door == self.prize_door:
            return True
        self.player_door = MHSim.flip_choice(self.player_door) if self.strategy == Strategy.FLIP else self.player_door
        if self.player_door == self.prize_door:
            return True
        return False


if __name__ == '__main__':
    mhsim = MHSim(prize_door=Door.DOOR2, strategy=Strategy.FLIP)
    mhsim.simulate()
