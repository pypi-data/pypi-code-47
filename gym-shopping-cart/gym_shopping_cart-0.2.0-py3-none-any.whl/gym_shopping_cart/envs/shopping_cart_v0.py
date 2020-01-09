import pathlib

import gym
import numpy as np
import pandas as pd

from gym_shopping_cart.data.parser import InstacartData


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
        [day of the week, hour of the day, days since last order]

        All values have a range of 0.0-1.0.

        All are one-hot encoded except the days since last order which is normalised to 1.

    Actions:
        A vector of length N, where N are the total number of products in the catalogue.

    Reward:
        +1 for a correctly ordered product (true positive). -1 for an incorrectly ordered product (false positive).
    """

    metadata = {"render.modes": [""]}

    def __init__(self, data: InstacartData = None, user_id: int = None):
        """
        data: an instance of the class representing the Instacart Data. Default: some test data from a single customer
        user_id: only use data from a specific customer. Default: a random customer
        """
        if data is None:
            data = self.test_data()
        self.data = data
        self.user_id = user_id
        self.reset()

    @property
    def action_space(self):
        return gym.spaces.MultiBinary(self.data.n_products())

    @property
    def observation_space(self):
        return gym.spaces.Box(
            0.0, 1.0, shape=(self.data.n_observations(),), dtype=np.float32
        )

    def test_data(self) -> InstacartData:
        return get_test_data()

    def step(self, action: np.ndarray):
        # Get next observation
        next_observation = self._get_observation()

        # Get reward
        reward = self._reward(action)

        # Check if this is the end of the batch
        done = bool(self._order_number > self._n_orders)

        return next_observation, reward, done, {}

    def _get_observation(self) -> np.ndarray:
        # Get the next order (indexed by order number)
        obs = self._user_data.loc[[self._order_number]].to_numpy()[0, :]
        self._order_number += 1
        return obs

    def _reward(self, action: np.ndarray) -> float:
        # Pull out the products ordered
        previous_purchased_products = self._purchase_data.loc[
            [self._order_number - 1]
        ].to_numpy()[0, :]
        if len(previous_purchased_products) != len(action):
            raise ValueError(
                "Provided action vector ({}) is not the same size as the customer's purchased products ({}).".format(
                    len(action), len(previous_purchased_products)
                )
            )
        tp = (previous_purchased_products.astype(bool) & action.astype(bool)).sum()
        fp = action.astype(bool).sum() - tp
        return tp - fp

    def reset(self) -> np.ndarray:
        self._user_data, self._purchase_data = self.data.orders_for_user(self.user_id)
        self._n_orders = self._user_data.index.max()
        self._order_number = self._user_data.index.min()
        return self._get_observation()

    def render(self, mode="human"):
        pass

    def close(self):
        pass


class SimpleShoppingCart(ShoppingCart):
    """
    Exactly the same as ShoppingCart except I limit the number of products to the DEFAULT_MAX_PRODUCTS most popular
    """

    DEFAULT_MAX_PRODUCTS = 25

    def test_data(self) -> InstacartData:
        return get_test_data(max_products=SimpleShoppingCart.DEFAULT_MAX_PRODUCTS)


def get_test_data(max_products: int = None) -> InstacartData:
    current_directory = pathlib.Path(__file__).parent
    instacart_data = InstacartData(
        gz_file=current_directory / ".." / "data" / "test_data.tar.gz",
        max_products=max_products,
    )
    return instacart_data
