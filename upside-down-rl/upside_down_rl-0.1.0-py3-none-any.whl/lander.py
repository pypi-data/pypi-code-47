import datetime

import gym
import tensorboardX
from torch import nn

import upside_down_rl


class LanderTorchModel(nn.Module):
    DIM = 64

    def __init__(self, state_dim, act_dim):
        super().__init__()
        self.model_embedding = nn.Sequential(
            nn.Linear(state_dim, self.DIM), nn.Sigmoid(),
        )
        self.command_embedding = nn.Sequential(nn.Linear(2, self.DIM), nn.Sigmoid(),)
        self.act_layer = nn.Linear(self.DIM, act_dim)

    def forward(self, state, command):
        embedded_state = self.model_embedding(state)
        embedded_cmd = self.command_embedding(command)
        return self.act_layer(embedded_state * embedded_cmd)


class LanderFinal(gym.Env):
    def step(self, action):
        observation, reward, done, info = self.env.step(action)
        self.curr_reward += reward
        if done:
            return observation, self.curr_reward, done, info
        return observation, 0.0, done, info

    def reset(self):
        self.curr_reward = 0
        return self.env.reset()

    def render(self, mode="human"):
        return self.env.render(mode=mode)

    def __init__(self):
        self.curr_reward = 0
        self.env = gym.make("LunarLander-v2")

    @property
    def action_space(self):
        return self.env.action_space

    @property
    def observation_space(self):
        return self.env.observation_space


def env_factory():
    return gym.make("LunarLander-v2")


def main():
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H%M")
    writer = tensorboardX.SummaryWriter(logdir="experiments/lander-{}".format(date_str))
    model = upside_down_rl.gym_model.GymModel(LanderTorchModel(8, 4), 8, 4)
    saver = upside_down_rl.utils.MinioSaver("lander-{}".format(date_str))

    cfg = upside_down_rl.udrl.URLDConfig(
        verbose=0,
        model=model,
        show_plays=True,
        replay_buffer_size=5000,
        operation_episodes=500,
        num_random_plays=1000,
        num_epoch=200,
        return_sampling_size=500,
        writer=writer,
        render=False,
        save_model=saver
    )
    upside_down_rl.udrl.train_udrl(env_factory, cfg)


if __name__ == "__main__":
    main()
