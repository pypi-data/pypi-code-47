import pathlib

import gym
import numpy as np
import pandas as pd

from gym_shopping_cart.data import InstacartData


def F1_score(labels: np.array, predicted: np.array) -> float:
    tp = (labels.astype(bool) & predicted.astype(bool)).sum()
    fp = predicted.sum() - tp
    fn = labels.sum() - tp
    if tp > 0:
        precision = tp / (tp + fp)
        recall = float(tp) / (tp + fn)
        return 2 * ((precision * recall) / (precision + recall))
    else:
        return 0


class ShoppingCart(gym.Env):
    """
    Simulates real customer product purchases using the Instacart dataset.

    Data:
        The data comes from the Instacart dataset 
        (see https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2).
        You must pass in an instance of the InstacartData class containing the data. If you
        do not, I will load a test dataset that comes with this library.

    Goal:
        Automatically pick products when people want to order (i.e. a bit like Stitch Fix)

    State: 
        The state comprises of:
        [products bought in previous shop, day of the week, hour of the day, days since last order]

        All values have a range of 0.0-1.0.

        All are one-hot encoded except the days since last order which is normalised to 1.

    Actions:
        A vector of length N, where N are the total number of products in the catalogue.

    Reward:
        F1-score over all products
    """

    metadata = {"render.modes": [""]}

    def __init__(self, data: InstacartData = None, user_id: int = None):
        if data is None:
            data = get_test_data()
        self.data = data
        self.user_id = user_id
        self.action_space = gym.spaces.MultiBinary(InstacartData.N_PRODUCTS)
        self.observation_space = gym.spaces.Box(
            0.0, 1.0, shape=(InstacartData.N_OBSERVATIONS,), dtype=np.float32
        )
        self.reset()

    def step(self, action: np.ndarray):
        # Get next observation
        next_observation = self._get_observation()

        # Get reward
        reward = self._reward(next_observation, action)

        # Check if this is the end of the batch
        done = bool(self._order_number > self._n_orders)

        return next_observation, reward, done, {}

    def _get_observation(self) -> np.ndarray:
        # Get the next order (indexed by order number)
        obs = self._user_data.loc[[self._order_number]].to_numpy()[0, :]
        self._order_number += 1
        return obs

    def _reward(self, obs: np.ndarray, action: np.ndarray) -> float:
        # Pull out the products ordered
        ordered_products = obs[: InstacartData.N_PRODUCTS]
        assert len(ordered_products) == len(action)
        # The reward is the F1-score
        return F1_score(ordered_products, action)

    def reset(self) -> np.ndarray:
        self._user_data = self.data.orders_for_user(self.user_id)
        self._n_orders = self._user_data.index.max()
        self._order_number = self._user_data.index.min()
        return self._get_observation()

    def render(self, mode="human"):
        pass

    def close(self):
        pass


def get_test_data() -> InstacartData:
    current_directory = pathlib.Path(__file__).parent
    instacart_data = InstacartData(
        gz_file=current_directory / ".." / ".." / "data" / "test_data.tar.gz"
    )
    return instacart_data
