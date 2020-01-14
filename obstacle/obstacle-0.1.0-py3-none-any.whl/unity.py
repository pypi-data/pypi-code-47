

import numpy as np


def process_vector_obs(vobs):
    return vector_obs[6], vector_obs[7], np.argmax(vector_obs[0:6], axis=0)

def process_info(info):
    obs = info.visual_observations[0][0]
    reward = info.rewards[0]
    done = info.local_done[0]
    vector_obs = info.vector_observations[0]
    info = dict(
        time=vector_obs[6],
        current_floor=vector_obs[7],
        key_num=np.argmax(vector_obs[0:6], axis=0),
        previous_action=info.previous_vector_actions[0],
        vector_obs=vector_obs
    )
    return (obs, reward, done, info)

