import gym
import numpy as np

import gym_shopping_cart


def test_simplified_shopping_cart():
    env = gym.make("SimpleShoppingCart-v0")
    state, _, _, _ = env.step(env.action_space.sample())
    assert isinstance(state, np.ndarray)
    assert state.shape[0] == 52
