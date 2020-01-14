from functools import singledispatch
from pathlib import Path
from typing import Any, Dict, Hashable, List, Optional, Union

import pendulum
import toml
from mlagents.trainers import demo_loader
from mlagents.envs.brain import BrainInfo, BrainParameters

from .common import *
from .tower import default_reset_parameters
from .unity import process_info

from operator import attrgetter
from more_itertools import groupby_transform, windowed
from collections import defaultdict
import numpy as np


@singledispatch
def load_meta(meta: str) -> Dict[Hashable, Any]:
    return toml.load(meta)


load_meta.register(Path, lambda p: load_meta(str(p)))
load_meta.register(dict, lambda m: m)
load_meta.register(type(None), lambda _: {})


def _load_unity_run(infos: List[BrainInfo]) -> Dict[int, Run]:
    infos = windowed(map(process_info, infos), 2)
    infos = list(infos)
    runs = groupby_transform(infos, lambda x: x[0][3]["current_floor"])
    result = defaultdict(list)
    for floor, exps in runs:
        if floor in result:
            continue
        for (obs, _, _, _), (newobs, reward, done, info) in exps:
            result[floor].append(
                Experience(
                    obs,
                    info["previous_action"],
                    reward,
                    newobs,
                    done,
                    info["vector_obs"],
                )
            )

    result = {floor: Experience(*zip(*exps)) for floor, exps in result.items()}
    result = {
        floor: Run(
            Experience(
                np.stack(exp.observation),
                np.stack(exp.action),
                np.stack(exp.reward),
                np.stack(exp.new_observation),
                np.stack(exp.terminal),
                np.stack(exp.vector_obs),
            ),
            floor,
        )
        for floor, exp in result.items()
    }
    return result


def load_unity_demo(
    path: Union[Path, str], meta: Optional[Union[Path, str, dict]] = None
) -> Trajectory:
    brain_infos: List[BrainInfo]
    brain_params: BrainParameters
    brain_params, brain_infos, total_expected = demo_loader.load_demonstration(
        str(path)
    )
    reset_params = default_reset_parameters()
    meta: dict = load_meta(meta)
    reset_params.update(meta.get("reset_parameters", {}))
    runs = _load_unity_run(brain_infos)
    return Trajectory(
        reset_params,
        start_time=meta.get("start_time", pendulum.now()),
        end_time=meta.get("end_time", pendulum.now()),
        runs=runs,
        name=meta.get("name", None),
        info=brain_params,
        steps=len(brain_infos),
        reward=sum(run.experience.reward.sum() for run in runs.values()),
    )
