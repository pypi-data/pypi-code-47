import random


def roulette(choices):
    total_prob = sum(list(choices.values()))
    choice = random.uniform(0, total_prob)
    running_total = 0
    for k, v in choices.items():
        running_total += v
        if running_total > choice:
            return k
