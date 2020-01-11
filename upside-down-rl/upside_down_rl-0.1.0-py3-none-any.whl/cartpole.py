import datetime

import gym
import tensorboardX
from torch import nn

import upside_down_rl


class CartPoleTorchModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.model_embedding = nn.Sequential(nn.Linear(4, 64), nn.PReLU(),)
        self.command_embedding = nn.Sequential(nn.Linear(2, 64), nn.PReLU(),)
        self.act_layer = nn.Sequential(nn.Linear(64, 64), nn.PReLU(), nn.Linear(64, 2),)

    def forward(self, state, command):
        embedded_state = self.model_embedding(state)
        embedded_cmd = self.command_embedding(command)
        return self.act_layer(embedded_state * embedded_cmd)


class CartPoleFinal(gym.Env):
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
        self.env = gym.make("CartPole-v0")

    @property
    def action_space(self):
        return self.env.action_space

    @property
    def observation_space(self):
        return self.env.observation_space


def main():
    env_factory = CartPoleFinal
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H%M")
    writer = tensorboardX.SummaryWriter(
        logdir="experiments/cartpole-{}".format(date_str)
    )
    model = upside_down_rl.gym_model.GymModel(CartPoleTorchModel(), 4, 2)
    saver = upside_down_rl.utils.MinioSaver("cartpole-{}".format(date_str))

    cfg = upside_down_rl.udrl.URLDConfig(
        verbose=0,
        model=model,
        show_plays=True,
        replay_buffer_size=5000,
        operation_episodes=500,
        num_random_plays=1000,
        num_epoch=20,
        return_sampling_size=500,
        writer=writer,
        save_model=saver,
        render=False,
    )
    upside_down_rl.udrl.train_udrl(env_factory, cfg)


if __name__ == "__main__":
    main()
