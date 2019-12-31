from gym.envs.registration import register

register(id="ShoppingCart-v0", entry_point="gym_shopping_cart.envs:ShoppingCart")
register(
    id="SimpleShoppingCart-v0", entry_point="gym_shopping_cart.envs:SimpleShoppingCart"
)
