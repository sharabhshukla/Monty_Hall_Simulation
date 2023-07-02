import random
from enum import Enum, auto


class Door(Enum):
    DOOR1 = auto()
    DOOR2 = auto()
    DOOR3 = auto()


class Strategy(Enum):
    FLIP = auto()
    STAY = auto()


class Outcome(Enum):
    WIN = True
    LOSS = False


class MHSim:
    """
    This class simulates a game of the Monty Hall problem.

    Parameters:
        prize_door (Door): The door concealing the prize.
        strategy (Strategy): The strategy used by the player, either FLIP or STAY.

    Attributes:
        prize_door (Door): The door concealing the prize.
        player_door (Door): The door initially chosen by the player.
        strategy (Strategy): The strategy used by the player, either FLIP or STAY.
    """
    def __init__(self, prize_door: Door, strategy: Strategy):
        self.prize_door = prize_door
        self.player_door = None
        self.strategy = strategy

    @staticmethod
    def flip_choice(player_door: Door):
        """
        Flips the player's choice of door.

        :param player_door: The door chosen by the player.
        :type player_door: Door
        :return: The flipped choice for the door.
        :rtype: Door
        """
        for door in random.sample(list(Door), len(list(Door))):
            if door != player_door:
                return door

    def simulate(self) -> Outcome:
        """
        Simulates a game of the Monty Hall problem.

        Returns:
            Outcome: The outcome of the game, either Outcome.WIN or Outcome.LOSS.

        Raises:
            None
        """
        self.player_door = random.choice(list(Door))
        if self.player_door == self.prize_door:
            return Outcome.WIN.value
        self.player_door = MHSim.flip_choice(self.player_door) if self.strategy == Strategy.FLIP else self.player_door
        if self.player_door == self.prize_door:
            return Outcome.WIN.value
        return Outcome.LOSS.value


if __name__ == '__main__':
    mhsim = MHSim(prize_door=Door.DOOR2, strategy=Strategy.FLIP)
    mhsim.simulate()
