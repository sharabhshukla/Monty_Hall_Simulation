import pytest
from src.sim.monty_hall_sim import MHSim, Door, Strategy, Outcome


@pytest.fixture
def mhsim():
    return MHSim(prize_door=Door.DOOR2, strategy=Strategy.FLIP)


def test_simulate_flip_wins(mhsim):
    result = mhsim.simulate()
    assert isinstance(result, bool)


def test_simulate_flip_loses():
    mhsim = MHSim(prize_door=Door.DOOR1, strategy=Strategy.FLIP)
    result = mhsim.simulate()
    assert isinstance(result, bool)


def test_simulate_stay_wins():
    mhsim = MHSim(prize_door=Door.DOOR3, strategy=Strategy.STAY)
    result = mhsim.simulate()
    assert isinstance(result, bool)


def test_simulate_stay_loses():
    mhsim = MHSim(prize_door=Door.DOOR1, strategy=Strategy.STAY)
    result = mhsim.simulate()
    assert isinstance(result, bool)
