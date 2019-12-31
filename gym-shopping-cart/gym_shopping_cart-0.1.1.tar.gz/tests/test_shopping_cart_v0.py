import pathlib

import gym
import numpy as np

import gym_shopping_cart
from gym_shopping_cart.envs.shopping_cart_v0 import F1_score
from gym_shopping_cart.data.parser import InstacartData


def test_f1_score():
    labels = np.array([0, 1, 0, 1])
    predicted = np.array([0, 1, 0, 1])
    res = F1_score(labels, predicted)
    assert res == 1.0
    predicted = np.array([1, 0, 1, 0])
    res = F1_score(labels, predicted)
    assert res == 0.0
    predicted = np.array([0, 1, 1, 0])
    res = F1_score(labels, predicted)
    assert res == 0.5
    predicted = np.array([0, 0, 0, 1])
    res = F1_score(labels, predicted)
    assert res == 2 / 3


def test_registration():
    env = gym.make("ShoppingCart-v0")
    assert env != None


def test_correct_num_episodes():
    env = gym.make("ShoppingCart-v0")
    episode_over = False
    buffer = []
    while not episode_over:
        _, reward, episode_over, _ = env.step(env.action_space.sample())
        buffer.append(reward)
    assert len(buffer) == 70


def test_state_is_not_empty():
    env = gym.make("ShoppingCart-v0")
    state, _, _, _ = env.step(env.action_space.sample())
    assert isinstance(state, np.ndarray)


def test_env_within_observation_space():
    env = gym.make("ShoppingCart-v0")
    assert hasattr(env, "observation_space")
    assert env.observation_space != None
    state, _, _, _ = env.step(env.action_space.sample())
    np.testing.assert_array_equal(env.observation_space.shape, state.shape)
    assert env.observation_space.contains(state)


def test_correct_reward():
    env = gym.make("ShoppingCart-v0")
    action = np.zeros((env.data.n_products(),))
    action[[8518, 9637, 14651, 37188, 45807, 46782]] = 1
    _, reward, _, _ = env.step(action)
    assert reward == 1
    env.reset()
    _, reward, _, _ = env.step(action - 1)
    assert reward == 0
