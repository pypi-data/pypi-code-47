from gym.envs.registration import register

register(
    id='random_walk-v0',
    entry_point='gym_fearbun2.envs.random_walk:RandomWalk'
)