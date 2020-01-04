import gym
from gym import spaces
from gym.utils import seeding
from enum import Enum
from six import StringIO
import sys

MAPS = {
    "map_1": ["                       ",
              "      BBBBBBBBBBBBBBBBF",
              "     BBBBBBBBBBBBBBBBBF",
              "   BBBBBBBBBBBBBBBBBBBF",
              "  BBBBBBBBBBBBBBBBBBBBF",
              " BBBBBBBBBBBBBBBBBBBBBF",
              " BBBBBBBBBBBB          ",
              " BBBBBBBBBBB           ",
              " BBBBBBBBBBB           ",
              " BBBBBBBBBBB           ",
              " BBBBBBBBBBB           ",
              " BBBBBBBBBBB           ",
              " BBBBBBBBBBB           ",
              "  BBBBBBBBBB           ",
              "  BBBBBBBBBB           ",
              "  BBBBBBBBBB           ",
              "  BBBBBBBBBB           ",
              "  BBBBBBBBBB           ",
              "  BBBBBBBBBB           ",
              "   BBBBBBBBB           ",
              "   BBBBBBBBB           ",
              "   BBBBBBBBB           ",
              "   BBBBBBBBB           ",
              "    BBBBBBBB           ",
              "    BBBBBBBB           ",
              "    SSSSSSSS           ",
              "                       "]
}


def action_to_space(action):
    return action[0] - 1, action[1] - 1


def space_to_action(space):
    return space[0] + 1, space[1] + 1

# v is not zero
def div_by_size(v):
    return 1 if v >= 0 else 0


# board  x ->
#       y
#       |
#       V
# action for y +1 = up -1 = down
class RaceboardEnv(gym.Env):
    metadata = {'render.modes': ['human', 'ansi']}

    class MoveResult(Enum):
        OKAY = 0
        FINISHED = 1
        CRASHED = 2

    action_space = spaces.MultiDiscrete([3, 3])
    observation_space = spaces.MultiDiscrete([[2, 2, 5, 5]])
    reward_range = (-1, 0)

    def __init__(self, map_type='map_1', is_noise=False):
        self.map = MAPS[map]
        self.is_noise = is_noise

        self.action_space = spaces.MultiDiscrete([3, 3])
        self.observation_space = spaces.MultiDiscrete([len(self.map), len(self.map[0]), 5, 5])

        self.start_pos = []
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == 'S':
                    self.start_pos.append((y, x))

        self._seed()

    def _step(self, action):
        delta_y, delta_x = action
        y, x, vel_y, vel_x = self.s

        if self.is_noise and self.np_random.random() <= 0.1:
            delta_y = 0
            delta_x = 0

        # minus for y because action direction is different from board
        vel_y -= delta_y
        vel_x += delta_x

        if vel_y < 0 or vel_x < 0 or (vel_y == 0 and vel_x == 0 and self.map[y][x] != 'S'):
            return self.s, -1, False, {}

        self.s = (y, x, vel_y, vel_x)
        finished = False
        result_code, y, x = self.move(y, x, vel_y, vel_x)
        if result_code == RaceboardEnv.MoveResult.CRASHED:
            self.crashed_pos = (y, x)
            self.s = self.get_random_start_state()
        elif result_code == RaceboardEnv.MoveResult.FINISHED:
            finished = True

        self.action_result = result_code

        return self.s, -1, finished, {}

    def _reset(self):
        self.s = self.get_random_start_state()
        self.action_result = RaceboardEnv.MoveResult.OKAY
        self.crashed_pos = None

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return seed

    def _render(self, mode='human', close=False):
        if close:
            return

        outfile = StringIO() if mode == 'ansi' else sys.stdout

        y, x, vel_y, vel_x = self.s
        outfile.write(f'Speed(x, y) =  ({vel_x}, {-vel_y}  Action Result: {self.action_result.name}\n')

        tmp = self.map[y][x]
        self.map[y][x] = 'A'

        if self.crashed_pos:
            crashed_tmp = self.map[self.crashed_pos[0]][self.crashed_pos[1]]
            self.map[self.crashed_pos[0]][self.crashed_pos[1]] = 'X'

        outfile.writelines(self.map)
        self.map[y][x] = tmp

        if self.crashed_pos:
            self.map[self.crashed_pos[0]][self.crashed_pos[1]] = crashed_tmp

        return outfile

    def get_random_start_state(self):
        return self.np_random.choice(self.start_pos) + action_to_space((0, 0))

    def check_collision(self, y, x):
        if self.map[y][x] == ' ':
            return RaceboardEnv.MoveResult.CRASHED, y, x
        elif self.map[y][x] == 'F':
            return RaceboardEnv.MoveResult.FINISHED, y, x
        else:
            return None

    def move(self, y, x, vel_y, vel_x):
        dest_y = y + vel_y
        dest_x = x + vel_x
        if vel_y == 0 or vel_x == 0:
            while y != dest_y or x != dest_x:
                y += vel_y == 1
                x += vel_x == 1

                ret = self.check_collision(y, x)
                if ret:
                    return ret
            return RaceboardEnv.MoveResult.OKAY, y, x

        checking_dir_y = div_by_size(vel_y)
        checking_dir_x = div_by_size(vel_x)
        real_y = y
        real_x = x
        while y != dest_y or x != dest_x:
            ret_y = self.check_collision(checking_dir_y + y, x)
            if ret_y:
                return ret_y

            ret_x = self.check_collision(y, checking_dir_x + x)
            if ret_x:
                return ret_x

            diff_y = (y + 1 - real_y) / vel_y
            diff_x = (x + 1 - real_x) / vel_x
            if diff_x > diff_y:
                delta = diff_y
                y += 1
            elif diff_x < diff_y:
                delta = diff_x
                x += 1
            else:
                delta = diff_y
                y += 1
                x +=1

            real_y += delta
            real_x += delta

        return RaceboardEnv.MoveResult.OKAY, y, x
