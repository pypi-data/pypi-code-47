from functools import partial
from itertools import product
from pathlib import Path
from typing import Callable, List, Optional

import attr
import cv2
import gym
import mlagents
import numpy as np
import torch
from mlagents.envs.environment import UnityEnvironment

from .unity import process_info


class UnityGymError(gym.error.Error):
    """
    Any error related to the gym wrapper of ml-agents.
    """


class Tower(gym.Env):
    """
        step
        reset
        render
        close
        seed

    And set the following attributes:

        action_space: The Space object corresponding to valid actions
        observation_space: The Space object corresponding to valid observations
        reward_range: A tuple corresponding to the min and max possible rewards
    """

    def __init__(self, env, conf, realtime):
        gym.Env.__init__(self)
        self._env = env
        self.brain_name = next(iter(env.external_brain_names))
        self._brain = brain = env.brains[self.brain_name]
        if len(brain.vector_action_space_size) == 1:
            self.action_space = gym.spaces.Discrete(brain.vector_action_space_size[0])
        else:
            self.action_space = gym.spaces.MultiDiscrete(brain.vector_action_space_size)
        self.observation_space = gym.spaces.Box(
            *(0, 1.0),
            dtype=np.float32,
            shape=(
                brain.camera_resolutions[0]["height"],
                brain.camera_resolutions[0]["width"],
                3,
            ),
        )
        self._config = conf
        self.realtime = realtime

    def step(self, action):
        info = self._env.step(action)[self.brain_name]
        return unity.process_info(info)

    def reset(self, **kwargs):
        config = dict(self._config)
        config.update(kwargs)
        if config["tower-seed"] == -1:
            config["tower-seed"] = np.random.randint(1, 100000)
        info = self._env.reset(config=config, train_mode=not self.realtime)[
            self.brain_name
        ]
        state, reward, done, info = unity.process_info(info)
        self.state = state
        self.reward = reward
        self.done = done
        self.info = info
        self.episode_seed = config["tower-seed"]
        return state

    def render(self):
        pass

    def close(self):
        self._env.close()

    def seed(self, seed):
        self._config["tower-seed"] = seed

    @property
    def brain(self):
        return self._brain


@attr.s(auto_attribs=True)
class Daedalus(object):

    # region params
    _layout: int = 2
    _difficulty: int = 2
    _room_content: int = 2
    _perspective: int = 1
    _theme: int = 0
    _dense: bool = False
    _lighting: int = 1

    _tower_seed: int = -1
    _theme_ordering: int = 1

    _path: Path = Path("")
    _realtime: bool = False
    _docker_training: bool = False

    _starting_floor: int = 0
    _total_floors: int = 100

    _worker_id: int = 0

    _allowed_versions: List[str] = ["3.1"]

    _observation_wrapper: Optional[Callable[[gym.Env], gym.ObservationWrapper]] = None
    _reward_wrapper: Optional[Callable[[gym.Env], gym.RewardWrapper]] = None
    _action_wrapper: Optional[Callable[[gym.Env], gym.ActionWrapper]] = None
    # endregion params
    # region properties

    @property
    def worker_id(self) -> int:
        return self._worker_id

    @worker_id.setter
    def worker_id(self, wid: int):
        self._worker_id = wid

    @property
    def action_wrapper(self) -> Optional[Callable[[gym.Env], gym.ActionWrapper]]:
        return self._action_wrapper

    @action_wrapper.setter
    def action_wrapper(self, wrapper: Optional[Callable[[gym.Env], gym.ActionWrapper]]):
        self._action_wrapper = wrapper

    @property
    def observation_wrapper(
        self,
    ) -> Optional[Callable[[gym.Env], gym.ObservationWrapper]]:
        return self._observation_wrapper

    @observation_wrapper.setter
    def observation_wrapper(
        self, wrapper: Optional[Callable[[gym.Env], gym.ObservationWrapper]]
    ):
        self._observation_wrapper = wrapper

    @property
    def reward_wrapper(self) -> Optional[Callable[[gym.Env], gym.RewardWrapper]]:
        return self._reward_wrapper

    @reward_wrapper.setter
    def reward_wrapper(self, wrapper: Optional[Callable[[gym.Env], gym.RewardWrapper]]):
        self._reward_wrapper = wrapper

    @property
    def tower_seed(self) -> int:
        """
        Tower seed: [-1,99999].
            -1 -> random
            other -> other
        """
        return self._tower_seed

    @tower_seed.setter
    def tower_seed(self, seed: int):
        assert -1 <= seed <= 99999 and isinstance(seed, int)
        self._tower_seed = seed

    @property
    def starting_floor(self) -> int:
        return self._starting_floor

    @starting_floor.setter
    def starting_floor(self, floor: int):
        assert 0 <= floor <= 99 and isinstance(floor, int)
        self._starting_floor = floor

    @property
    def total_floors(self) -> int:
        return self._total_floors

    @total_floors.setter
    def total_floors(self, n_floors: int):
        assert 1 <= n_floors <= 100 and isinstance(n_floors, int)

    @property
    def layout(self) -> int:
        """
        Layout Parameter.
        0 -> Simple
        1 -> Branching
        2 -> Circles
        """
        return self._layout

    @layout.setter
    def layout(self, layout: int):
        assert 0 <= layout <= 2 and isinstance(layout, int)
        self._layout = layout

    @property
    def difficulty(self) -> int:
        """
        Room difficulty
        0 -> Empty/Trivial
        1 -> Easy
        2 -> Difficult
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty: int):
        assert 0 <= difficulty <= 2 and isinstance(difficulty, int)
        self._difficulty = difficulty

    @property
    def room_content(self) -> int:
        """
        0 -> Normal Rooms
        1 -> Rooms with Keys
        2 -> Puzzle Rooms
        """
        return self._room_content

    @room_content.setter
    def room_content(self, room_content: int):
        assert 0 <= room_content <= 2
        self._room_content = 0

    @property
    def perspective(self) -> int:
        """
        0 -> First Person
        1 -> Third Person
        """
        return self._perspective

    @perspective.setter
    def perspective(self, perspective):
        assert 0 <= perspective <= 1
        self._perspective = perspective

    @property
    def theme(self) -> int:
        """
        Default theme
            0 -> AncientTheme
            1 -> MoorishTheme
            2 -> IndustrialTheme
            3 -> ModernTheme
            4 -> FutureTheme
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        assert 0 <= theme <= 5
        self._theme = theme

    @property
    def path(self) -> Path:
        """
        Path to executable
        """
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def dense(self) -> bool:
        """
        Whether to use a dense environment
        """
        return self._dense

    @dense.setter
    def dense(self, dense):
        assert 0 <= dense <= 1
        self._dense = dense

    @property
    def docker_training(self) -> bool:
        """
        Using docker to train
        """
        return self._docker_training

    @docker_training.setter
    def docker_training(self, dt):
        assert 0 <= dt <= 1
        self._docker_training = dt

    @property
    def realtime(self) -> bool:
        """
        Realtime mode
        0 -> Disabled
        1 -> Enabled
        """
        return self._realtime

    @property
    def train_mode(self) -> bool:
        return not self.realtime

    @realtime.setter
    def realtime(self, rt):
        assert 0 <= rt <= 1
        self._realtime = rt

    @property
    def lighting(self) -> int:
        """
        Lighting Conditions
        0 -> No Lighting
        1 -> Minimal Lighting
        2 -> Realtime Lighting
        """
        return self._lighting

    @lighting.setter
    def lighting(self, lt):
        assert 0 <= lt <= 2
        self._lighting = lt

    @property
    def allowed_versions(self) -> List[str]:
        """
        Allowed executable versions
        """
        return self._allowed_versions

    @allowed_versions.setter
    def allowed_versions(self, versions):
        self._allowed_versions = versions

    @property
    def theme_ordering(self) -> int:
        return self._theme_ordering

    @theme_ordering.setter
    def theme_ordering(self, ordering):
        assert 0 <= ordering <= 1
        self._theme_ordering = ordering

    # endregion properties

    @property
    def config(self) -> dict:
        return {
            "tower-seed": self.tower_seed,
            "starting-floor": self.starting_floor,
            "total-floors": self.total_floors,
            "dense-reward": self.dense,
            "lighting-type": self.lighting,
            "visual-theme": self.theme_ordering,
            "agent-perspective": self.perspective,
            "allowed-rooms": self.room_content,
            "allowed-modules": self.difficulty,
            "allowed-floors": self.layout,
            "default-theme": self.theme,
        }

    def build(self) -> Tower:
        config = self.config

        """
        me kapio tropo exw to env
        """
        env = _load_tower(
            self.path,
            self.worker_id,
            self.docker_training,
            allowed_versions=self.allowed_versions,
        )
        env = Tower(env, config, realtime=self.realtime)
        env = self.observation_wrapper and self.observation_wrapper(env) or env
        env = self.reward_wrapper and self.reward_wrapper(env) or env
        env = self.action_wrapper and self.action_wrapper(env) or env
        return env


def _load_tower(
    path: Path,
    worker_id: int = 0,
    docker_training: bool = False,
    allowed_versions=["3.1"],
) -> UnityEnvironment:
    try:
        env = UnityEnvironment(
            str(path), worker_id=worker_id, docker_training=docker_training
        )
        print("here")
        name, version = env.academy_name.split("-v")
        assert (
            name == "ObstacleTower"
        ), "Attempting to launch non-Obstacle Tower environment"
        assert (
            version in allowed_versions
        ), f"Invalid Obstacle Tower version.  Your build is v{version} but only the following versions are compatible with this gym: {allowed_versions}"

        if len(env.brains) != 1:
            raise UnityGymError(
                "There can only be one brain in a UnityEnvironment "
                "if it is wrapped in a gym."
            )
        return env
    except (AssertionError) as exception:
        raise ValueError(exception.args[0])
    except ValueError as _:
        raise ValueError("Attempting to launch a non-Unity Environment")


class FlatActionsWrapper(gym.ActionWrapper):
    def __init__(self, env):
        super(FlatActionsWrapper, self).__init__(env)
        aspace = self.action_space.nvec
        vectors = list(map(list, product(*map(range, aspace))))
        mapping = dict(enumerate(vectors))
        self.action_space = gym.spaces.Discrete(len(mapping))

        def action(action):
            return mapping[action]

        def reverse_action(action):
            return vectors[action]

        self.action = action
        self.reverse_action = reverse_action


class TensorObservationWrapper(gym.ObservationWrapper):
    def __init__(self, env):
        super(TensorObservationWrapper, self).__init__(env)

    @staticmethod
    def observation(obs):
        return torch.from_numpy(obs)


class RescalerObservationWrapper(gym.ObservationWrapper):
    def __init__(self, env, *, width, height, tensor=False):
        super(RescalerObservationWrapper, self).__init__(env)
        if tensor:

            def observation(obs):
                return torch.from_numpy(
                    cv2.resize(obs, (width, height), cv2.INTER_AREA)
                )

        else:

            def observation(obs):
                return cv2.resize(obs, (width, height), cv2.INTER_AREA)

        self.observation = observation


RetroTensorWrapper = partial(
    RescalerObservationWrapper, width=84, height=84, tensor=True
)
RetroWrapper = partial(RescalerObservationWrapper, width=84, height=84, tensor=True)


def TrivialBuilder():
    builder = Daedalus()
    builder.dense = True
    builder.difficulty = 0
    builder.lighting = 0
    builder.layout = 0
    builder.theme = 0
    builder.room_content = 0
    return builder


def default_reset_parameters():
    return {
        "starting-floor": 0,
        "dense-reward": 0,
        "lighting-type": 1,
        "visual-theme": 1,
        "agent-perspective": 1,
        "allowed-rooms": 2,
        "allowed-modules": 2,
        "allowed-floors": 2,
        "total-floors": 100,
        "default-theme": 0,
    }
