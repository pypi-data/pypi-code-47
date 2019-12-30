import gym
from gym import spaces as _spaces
import numpy as _np
from StarkLego.lego_builders.model.blocks import TwoXTwoBlock
from StarkLego.lego_builders.service.builder import LegoWorld

from ldraw.pieces import Group, Piece

class LegoEnv(gym.Env):
	def __init__(self, x, y, z, noLegoPieces):
		super(LegoEnv, self).__init__()

		self.action_space = _spaces.Box(low=_np.array([0, 0]), high=_np.array([x,z], dtype=_np.int8))
		self.observation_space = _spaces.Box(
            low=0, high=1, shape=(x, y, z), dtype=_np.int8)
		
		self.current_step = 0
		self.reward = noLegoPieces
		self.world = LegoWorld(x, y, z)
		self.number_of_lego_pieces = noLegoPieces
		self.consecutiveWrongChoices = 0
		self.steps_taken = 0
		self.previous_global_maximum = 0

	def _take_action(self, action):
		
		action_x = action[0]
		action_z = action[1]
		
		legoBlock = TwoXTwoBlock()
	
		self.world.add_part_to_world(legoBlock, action_x, action_z)
		return self.world.y_global_max
		

	def _next_observation(self):
		self.current_step += 1
		return self.world.content

	def step(self, action):
		done=False
		reward = 0
		
		try:
			global_maximum = self._take_action(action)
			if self.previous_global_maximum >= global_maximum:
				reward = 10
			else:
				self.previous_global_maximum = global_maximum
				reward = -100
		except:
			reward = -10000

		self.steps_taken += 1
		
		if self.steps_taken >= self.number_of_lego_pieces:
			done = True
		obs = self._next_observation()
		return obs, reward, done, {"ldrContent": self.world.ldraw_content}

	def reset(self):
		self.reward = 0
		self.world.reset()
		self.current_step = 0
		self.steps_taken = 0
		self.previous_global_maximum = 0

		return self.world.content

	def render(self, mode='human', close=False):
		print(self.world.ldraw_content)
		
