import gym
from gym import spaces
from gym.utils import seeding


class RandomWalk(gym.Env):
    reward_range = (0, 1)
    action_space = spaces.Discrete(1)
    observation_space = spaces.Discrete(7)

    def __init__(self):
        self.np_random = None
        self.s = None
        self.seed()

    def step(self, action):
        if self.np_random.random() <= 0.5:
            self.s -= 1
        else:
            self.s += 1

        done = False
        reward = 0
        if self.s == 0:
            done = True
        if self.s == 6:
            done = True
            reward = 1

        return self.s, reward, done, {}

    def reset(self):
        self.s = 3
        return self.s

    def render(self, mode='human'):
        raise NotImplementedError

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
