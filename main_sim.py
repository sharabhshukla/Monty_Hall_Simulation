from random import choice
from loguru import logger
from src.sim.monty_hall_sim import Strategy, Door, MHSim

n_trials = 2_000_000


logger.info("Running monty hall simulation!!")
for strategy in Strategy:
    outcomes = []
    logger.info(f"Running simulation for {strategy}")
    for n in range(n_trials):
        mh_sim = MHSim(prize_door=choice(list(Door)), strategy=strategy)
        outcomes.append(mh_sim.simulate())
    probability = sum(outcomes)/len(outcomes)
    logger.info(f"probability of winning with {strategy} -> {probability}")



