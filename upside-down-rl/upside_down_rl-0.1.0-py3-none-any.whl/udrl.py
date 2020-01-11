import concurrent.futures
import heapq
import multiprocessing
import typing as t

import attr
import gym
import numpy as np
import tensorboardX
from grappa import expect
from tqdm import tqdm


class ReplayBuffer:
    def __init__(self, max_size):
        expect(max_size).to.be.above(0)
        self.max_size = max_size
        self._buffer: t.List["Episode"] = []
        self._recent_buffer: t.List["Episode"] = []

    def add_episode(self, episode: "Episode"):
        expect(len(self._buffer)).to.be.below_or_equal(self.max_size)
        if len(self._buffer) == self.max_size:
            heapq.heappushpop(self._buffer, episode)
        else:
            heapq.heappush(self._buffer, episode)

        if len(self._recent_buffer) >= self.max_size:
            self._recent_buffer.pop(0)
        self._recent_buffer.append(episode)

    def episodes(self) -> t.List["Episode"]:
        return self._buffer + self._recent_buffer

    def clear(self):
        self._buffer = []
        self._recent_buffer = []

    def nlargest(self, num) -> t.List["Episode"]:
        return heapq.nlargest(num, self._buffer)


@attr.s
class TrainItem:
    state = attr.ib()
    delta_t = attr.ib()
    delta_r = attr.ib()
    action = attr.ib()


class ModelInferface:
    def train(self, data: t.List[TrainItem]):
        raise NotImplementedError()

    def run(self, observation, delta_t: int, delta_r: int):
        raise NotImplementedError()

    def random_action(self):
        raise NotImplementedError()


@attr.s
class URLDConfig:
    replay_buffer_size = attr.ib(default=5000)
    num_random_plays = attr.ib(default=500)
    verbose = attr.ib(default=0)
    show_plays = attr.ib(default=False)
    num_epoch = attr.ib(default=100)
    return_sampling_size = attr.ib(default=100)
    operation_episodes = attr.ib(default=100)
    model: ModelInferface = attr.ib(default=None)
    writer: t.Optional[tensorboardX.SummaryWriter] = attr.ib(default=None)
    global_step: int = attr.ib(default=0)
    save_model = attr.ib(default=None)
    render = attr.ib(default=True)

    def disable_tqdm_bars(self):
        return self.verbose < 10


# noinspection PyArgumentList
@attr.s(order=False, eq=False)
class Episode:
    actions = attr.ib()
    observations = attr.ib()
    rewards = attr.ib()
    total_reward = attr.ib()

    # noinspection PyDataclass
    def __lt__(self, other):
        if self.total_reward == other.total_reward:
            return self.length < other.length
        return self.total_reward < other.total_reward

    # noinspection PyDataclass
    def __le__(self, other):
        if self.total_reward == other.total_reward:
            return self.length <= other.length
        return self.total_reward <= other.total_reward

    def __eq__(self, other):
        cond_1 = self.total_reward == other.total_reward
        cond_2 = self.length == other.length
        return cond_1 and cond_2

    @property
    def length(self):
        return len(self.rewards)


def _run_episode(
    env: gym.Env, urld_config: URLDConfig, take_random_actions, render, run_conf
):
    actions = []
    observations = []
    rewards = []

    observation = env.reset()
    done = False

    if not take_random_actions:
        horizon, reward_lb, reward_ub = run_conf
        assert reward_lb <= reward_ub
        reward_target = np.random.uniform(reward_lb, reward_ub)
    else:
        horizon, reward_target = 0, 0

    while not done:
        if render:
            env.render()
        if take_random_actions:
            action = urld_config.model.random_action()
        else:
            action = urld_config.model.run(observation, horizon, reward_target)

        next_observation, reward, done, _ = env.step(action)
        actions.append(action)
        observations.append(observation)
        rewards.append(reward)
        horizon -= 1
        reward_target -= reward
        observation = next_observation

    if not rewards:
        return None
    # noinspection PyArgumentList
    return Episode(
        actions=actions,
        observations=observations,
        rewards=rewards,
        total_reward=np.sum(rewards),
    )


def _run_multi_episodes(
    env_factory,
    urld_config: URLDConfig,
    num_episodes: int,
    take_random_actions,
    run_conf,
):
    env = env_factory()
    return [
        _run_episode(env, urld_config, take_random_actions, False, run_conf)
        for _ in range(num_episodes)
    ]


def _par_run_episodes(
    env_factory,
    urld_config: URLDConfig,
    num_episodes: int,
    take_random_actions,
    run_conf,
):
    num_cpu = multiprocessing.cpu_count()
    task_count = num_episodes // num_cpu
    task_results = []

    urld_config = attr.evolve(urld_config, writer=None)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for cpu in range(num_cpu):
            if cpu == 0:
                cpu_num_eps = num_episodes - (task_count * (num_cpu - 1))
            else:
                cpu_num_eps = task_count
            args = (
                env_factory,
                urld_config,
                cpu_num_eps,
                take_random_actions,
                run_conf,
            )
            task_results.append(executor.submit(_run_multi_episodes, *args))

        results = concurrent.futures.wait(task_results)
    final_result = []
    for done_task in results.done:
        final_result.extend([t for t in done_task.result() if t is not None])

    return final_result


def _random_fill(env_factory, replay_buffer: ReplayBuffer, urld_config: URLDConfig):
    episodes = _par_run_episodes(
        env_factory, urld_config, urld_config.num_random_plays, True, None
    )
    urld_config.global_step += len(episodes)

    for episode in episodes:
        replay_buffer.add_episode(episode)


def _run_model(
    env_factory, replay_buffer: ReplayBuffer, urld_config: URLDConfig, render_env
):
    n_largest_entries = replay_buffer.nlargest(urld_config.return_sampling_size)
    horizons = [x.length for x in n_largest_entries]
    returns = [x.total_reward for x in n_largest_entries]

    desired_horizon = np.mean(horizons)
    desired_return_sd = np.std([x.total_reward for x in n_largest_entries])
    desired_return_lb = float(np.mean(returns))
    desired_return_ub = float(desired_return_lb + desired_return_sd)
    expect(desired_return_lb).to.be.below_or_equal(desired_return_ub)

    run_conf = (desired_horizon, desired_return_lb, desired_return_ub)

    episodes = _par_run_episodes(
        env_factory, urld_config, urld_config.num_random_plays, False, run_conf
    )
    urld_config.global_step += len(episodes)

    for episode in episodes:
        replay_buffer.add_episode(episode)

    if urld_config.writer is not None:
        all_total_rewards = [e.total_reward for e in episodes]
        all_horizons = [e.length for e in episodes]

        global_step = urld_config.global_step
        urld_config.writer.add_histogram(
            "run/rewards", all_total_rewards, global_step=global_step
        )
        urld_config.writer.add_scalar(
            "run/avg-reward", np.mean(all_total_rewards), global_step=global_step
        )
        urld_config.writer.add_histogram(
            "run/horizons", all_horizons, global_step=global_step
        )
        urld_config.writer.add_scalar(
            "run/avg-horizons", np.mean(all_horizons), global_step=global_step
        )

    if urld_config.render:
        _run_episode(render_env, urld_config, False, True, run_conf)
        _run_episode(render_env, urld_config, False, True, run_conf)
        _run_episode(render_env, urld_config, False, True, run_conf)


def _train_model(replay_buffer: ReplayBuffer, urld_config: URLDConfig):
    episodes = [e for e in replay_buffer.episodes() if len(e.rewards) >= 2]
    expect(len(episodes)).to.be.above(0)
    train_data = []

    for episode in tqdm(
        episodes,
        desc="Building training data",
        disable=urld_config.disable_tqdm_bars(),
    ):
        total_t = len(episode.rewards)
        time_1, time_2 = np.random.choice(total_t, size=2, replace=False)
        if np.random.rand() < 0.5:
            time_2 = total_t

        s_t1 = episode.observations[time_1]
        delta_r = np.sum(episode.rewards[time_1:time_2])
        delta_t = time_2 - time_1
        action = episode.actions[time_1]

        train_entry = TrainItem(
            state=s_t1, delta_t=delta_t, delta_r=delta_r, action=action
        )
        train_data.append(train_entry)

    urld_config.model.train(train_data)


def _save_model(urld_config):
    if urld_config.save_model is not None:
        urld_config.save_model(urld_config, urld_config.model)


def train_udrl(env_factory, urld_config: URLDConfig):
    buffer = ReplayBuffer(urld_config.num_random_plays)
    render_env = env_factory()
    _random_fill(env_factory, buffer, urld_config)
    for _ in range(urld_config.num_epoch):
        _train_model(buffer, urld_config)
        _run_model(env_factory, buffer, urld_config, render_env)
        _save_model(urld_config)
