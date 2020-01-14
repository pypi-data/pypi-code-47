from collections import namedtuple, deque
from dataclasses import dataclass
from typing import List, Dict, Any, Union, Hashable, Optional
from pendulum import DateTime, parse as parse_dt
from pathlib import Path
import numpy as np

try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle


"""
Trajectory: List of Runs
Run: List of Experiences in same floor
"""

Experience = namedtuple(
    "Experience",
    ["observation", "action", "reward", "new_observation", "terminal", "vector_obs"],
)


@dataclass
class Run(object):
    experience: Experience
    floor: int


@dataclass
class Trajectory(object):
    reset_parameters: Dict[str, int]
    start_time: DateTime
    end_time: DateTime
    runs: Dict[int, Experience]
    info: Dict[Hashable, Any]
    steps: int = 0
    reward: float = 0
    name: Optional[str] = None

    def dump(self, path: Union[str, Path]):
        with Path(path).open("wb") as fp:
            pickle.dump(self.reset_parameters, fp)
            pickle.dump(str(self.start_time), fp)
            pickle.dump(str(self.end_time), fp)
            pickle.dump(self.info, fp)
            pickle.dump(self.steps, fp)
            pickle.dump(self.reward, fp)
            pickle.dump(self.name, fp)
            pickle.dump(list(self.runs.keys()), fp)
            for run in self.runs.values():
                np.savez_compressed(fp, run)

    @classmethod
    def load(cls, path: Union[str, Path]):
        with Path(path).open("rb") as fp:
            reset_params = pickle.load(fp)
            start_time = pickle.load(fp)
            end_time = pickle.load(fp)
            info = pickle.load(fp)
            steps = pickle.load(fp)
            reward = pickle.load(fp)
            name = pickle.load(fp)
            floors = pickle.load(fp)
            runs = {
                floor: Experience(*np.load(fp)) for floor in floors
            }
            return cls(
                reset_params,
                parse_dt(start_time),
                parse_dt(end_time),
                {},
                info,
                steps,
                reward,
                name,
            )

