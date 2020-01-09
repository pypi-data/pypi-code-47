import pathlib

import gym
import numpy as np

import gym_shopping_cart
from gym_shopping_cart.data.parser import InstacartData


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
    assert reward == 6
    env.reset()
    _, reward, _, _ = env.step(np.zeros((env.data.n_products(),)))
    assert reward == 0
    action = np.ones((env.data.n_products(),))
    _, reward, _, _ = env.step(action)
    assert reward == -49979.0


def test_swap_data_class():
    env = gym.make("ShoppingCart-v0")
    current_directory = pathlib.Path(__file__).parent
    instacart_data = InstacartData(
        gz_file=current_directory
        / ".."
        / "gym_shopping_cart"
        / "data"
        / "test_data.tar.gz",
        max_products=2,
    )
    env.data = instacart_data
    env.reset()  # Have to reset the environment when you change the data source
    env.step(np.ones(instacart_data.n_products()))
    env.step(np.ones(instacart_data.n_products()))
