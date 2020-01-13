import gym
import numpy as np
import os
import psutil
import random
import shutil
import subprocess
import sys
import time

from pathlib import Path

try:
    from eye import CAMInit, CAMGet, CAMGetGray, QQVGA, QQVGA_X, QQVGA_Y
    from eye import SIMGetRobot, SIMSetRobot
    from eye import VWSetSpeed
except ImportError:
    print("Could not import eye. Please add eye.py to your path.")
    sys.exit()

from gym_eyesim.utils.road import detect_road


class EyeBotEnv(gym.Env):
    def __init__(
            self,
            path_to_sim,
            n_channels=3,
            crop=True,
            noise_fn=None,
    ):
        self.executable_name = "eyesim"
        if shutil.which(self.executable_name) is None:
            print(
                "No eyesim executable found. Please install it and add it to your path."
            )
            sys.exit()
        if os.path.isabs(path_to_sim):
            path_to_sim = os.path.relpath(path_to_sim)
        self._path_to_sim = Path(path_to_sim)
        self._noise_fn = noise_fn
        self._n_channels = n_channels
        if self._n_channels == 3:
            self._get_image_fn = CAMGet
        else:
            self._get_image_fn = CAMGetGray
        self._cam_img_size = [QQVGA_Y, QQVGA_X]
        self._crop = crop
        if self._crop:
            self._cropped_img_size = [QQVGA_Y // 2, QQVGA_X]
        else:
            self._cropped_img_size = [QQVGA_Y, QQVGA_X]
        self._cam_init = False
        self._robot_id = 0
        self._speed = 100
        self._road = detect_road(self._path_to_sim)
        self._lane_id = 0
        self.action_space = gym.spaces.Box(
            low=-1,
            high=1,
            shape=(1, ),
            dtype=np.float32,
        )
        self.observation_space = gym.spaces.Box(
            low=0,
            high=255,
            shape=(
                self._cropped_img_size[0],
                self._cropped_img_size[1],
                self._n_channels,
            ),
            dtype=np.float32,
        )

    def step(self, action):
        if not -1 <= action <= 1:
            raise ValueError(
                f"The `action` must not be smaller than -1 or larger than -1, but is {action}."
            )
        if self._noise_fn is not None:
            action = np.clip(action + self._noise_fn(), -1, 1)
        self._take_action(action)
        obs = self._get_observation()
        done = self._is_done()
        reward = self._reward_fn(done)
        return obs, reward, done, {}

    def render(self):
        return self._get_image()

    def _take_action(self, action):
        """Take an action

        Args:
            action (float): angular speed / linear speed
        """

        linear_speed = self._speed
        angular_speed = int(self._speed * action)
        VWSetSpeed(linear_speed, angular_speed)

    def _get_image(self):
        img = self._get_image_fn()
        img = np.array(img, dtype="float32")
        img = img / 255
        img = img.reshape(self._cam_img_size + [self._n_channels])
        if self._crop:
            img = img[(QQVGA_Y // 2):]
        return img

    def _get_observation(self):
        img = self._get_image()
        return img

    def _get_robot_pose(self):
        x, y, z, phi = [c_int.value for c_int in SIMGetRobot(self._robot_id)]
        return x, y, y, phi

    def _dist_to_road(self, x, y):
        dist_to_road = self._road.lanes[self._lane_id].dist(np.array([x, y]))
        return dist_to_road

    def _angle_to_road(self, x, y, phi):
        phi *= np.pi / 180
        road_angle = self._road.lanes[self._lane_id].angle(np.array([x, y]))
        diff = road_angle - phi
        smallest_diff = min(abs(diff), 2 * np.pi - abs(diff))
        return smallest_diff

    def _is_done(self):
        x, y, _, phi = self._get_robot_pose()
        dist_to_road = self._dist_to_road(x, y)
        angle_to_road = self._angle_to_road(x, y, phi)
        return dist_to_road > 1.2 * self._road.width / 4 or angle_to_road > np.pi / 2

    def _reward_fn(self, done):
        if done:
            return -100
        else:
            return 1

    def seed(self, seed=None):
        if seed is not None:
            np.random.seed(seed)
        return [seed]

    def reset(self, pose=None, lane_id=None):
        simulation_running = self.executable_name in (
            p.name() for p in psutil.process_iter())
        if not simulation_running:
            subprocess.Popen([self.executable_name, self._path_to_sim])
            time.sleep(5)

        if not self._cam_init:
            CAMInit(QQVGA)
            self._cam_init = True

        if lane_id is not None:
            self._lane_id = lane_id
        else:
            self._lane_id = random.randint(0, 1)

        # Set vehicle to random pose on road if no pose is given
        if pose is None:
            [x, y], phi = self._road.lanes[self._lane_id].random_pose()
        else:
            [x, y], phi = pose

        # Convert types and units
        x, y = int(x), int(y)
        phi = int(-180 / np.pi * phi)
        z = 4

        # Stop vehicle and set position
        VWSetSpeed(0, 0)
        SIMSetRobot(self._robot_id, x, y, z, phi)
        return self._get_observation()

    def close(self):
        subprocess.run(["pkill", "EyeSim"])
