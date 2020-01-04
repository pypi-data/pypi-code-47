import numpy as np
import tables as t
import os
from contextlib import contextmanager


class LOSE:
	def __init__(self, fname=None):
		self.fname = fname
		self.atom = t.Float32Atom()

		self.batch_size = 1

		self.iterItems = None
		self.iterOutput = None
		self.loopforever = False
		self.limit = None
		self.shuffle = False
		self.mask_callback = None

		self._slices = []
		self._useCallback = False

	def __repr__(self):
		messsage = '<lose hdf5 data handler, fname={}, atom={}>'.format(self.fname, self.atom)
		messsage += '\ngenerator parameters: iterItems={}, iterOutput={}, batch_size={}, limit={}, loopforever={}, shuffle={}'.format(self.iterItems, self.iterOutput, self.batch_size, self.limit, self.loopforever, self.shuffle)
		if self.fname is not None:
			try:
				with t.open_file(self.fname, mode='r') as f:
					messsage += '\nhdf5 file structure:\n{}'.format(f.__repr__())

			except Exception as e:
				messsage += '\nfailed to open file at \'{}\':{}, make sure it\'s a not corrupted hdf5 file and is a real file'.format(self.fname, e)

		return messsage

	def __str__(self):
		messsage = '<lose hdf5 data handler, fname={}, atom={}>'.format(self.fname, self.atom)
		if self.fname is not None:
			try:
				with t.open_file(self.fname, mode='r') as f:
					messsage += '\nhdf5 file structure:\n{}'.format(f)

			except Exception as e:
				messsage += '\nfailed to open file at \'{}\':{}, make sure it\'s a not corrupted hdf5 file and is a real file'.format(self.fname, e)

		return messsage

	def newGroup(self, fmode='a', **kwards):
		if type(fmode) is not str or fmode not in ['a', 'w']:
			raise ValueError('unexpected value passed to fmode, expected \'a\' or \'w\', got \'{}\''.format(fmode))

		with t.open_file(self.fname, mode=fmode) as f:
			for groupName, val in kwards.items():
				f.create_earray(f.root, groupName, self.atom, (0, *val))

	def removeGroup(self, *args):
		with t.open_file(self.fname, mode='a') as f:
			for groupName in args:
				f.remove_node('/{}'.format(groupName), recursive=True)

	def renameGroup(self, **kwards):
		with t.open_file(self.fname, mode='a') as f:
			for oldName, newName in kwards.items():
				x = eval('f.root.{}'.format(oldName))
				f.rename_node(x, newName)

	def save(self, **kwards):
		with t.open_file(self.fname, mode='a') as f:
			for key, val in kwards.items():
				x = eval('f.root.{}'.format(key))
				x.append(val)

	def load(self, *args, batch_obj=':'):
		out = []
		with t.open_file(self.fname, mode='r') as f:
			for key in args:
				x = eval('f.root.{}[np.s_[{}]]'.format(key, batch_obj))
				out.append(x)

		return out

	def getShape(self, arrName):
		return self.getShapes(arrName)[0]

	def getShapes(self, *arrNames):
		out = []
		with t.open_file(self.fname, mode='r') as f:
			for i in arrNames:
				out.append(eval('f.root.{}.shape'.format(i)))

		return out

	def _iterator_init(self):
		if self.fname is None:
			raise ValueError('self.fname is empty')

		if self.iterItems is None or self.iterOutput is None:
			raise ValueError('self.iterItems and/or self.iterOutput are not defined')

		if len(self.iterItems) != 2 or len(self.iterOutput) != 2:
			raise ValueError('self.iterItems or self.iterOutput has wrong dimensions, self.iterItems has to be [[list of x array names], [list of y array names]] and self.iterOutput is the name map self.iterItems folowing the same dimensions')

		if not isinstance(self.mask_callback, type(None)) and hasattr(self.mask_callback, '__call__'):
			self._useCallback = True

		L = [i[0] for i in self.getShapes(*self.iterItems[0])]
		L.extend([i[0] for i in self.getShapes(*self.iterItems[1])])
		dataset_limit = min(L)

		index = 0

		while 1:
			self._slices.append(np.s_[index:index+self.batch_size])

			index += self.batch_size

			if self.limit is not None:
				if index >= self.limit or index >= dataset_limit:
					break

			elif index >= dataset_limit:
				break

	def _iterator(self):
		if self.iterItems is None or self.iterOutput is None or self.fname is None:
			raise ValueError('self.iterItems and/or self.iterOutput and/or self.fname is empty')

		if len(self.iterItems) != 2 or len(self.iterOutput) != 2:
			raise ValueError('self.iterItems or self.iterOutput has wrong dimensions, self.iterItems is [[list of x array names], [list of y array names]] and self.iterOutput is the name map for them')

		with t.open_file(self.fname, mode='r') as f:
			while 1:
				if self.shuffle:
					np.random.seed(None)
					np.random.shuffle(self._slices)

				for cheeseSlice in self._slices:
					if self.shuffle:
						np.random.seed(None)
						st = np.random.get_state()

					stepX = {}
					stepY = {}
					for name, key in zip(self.iterItems[0], self.iterOutput[0]):
						x = eval('f.root.{}[{}]'.format(name, cheeseSlice))
						if self.shuffle:
							np.random.set_state(st)
							np.random.shuffle(x)

						stepX[key] = x

					for name, key in zip(self.iterItems[1], self.iterOutput[1]):
						y = eval('f.root.{}[{}]'.format(name, cheeseSlice))
						if self.shuffle:
							np.random.set_state(st)
							np.random.shuffle(y)

						stepY[key] = y

					if self._useCallback:
						yield self.mask_callback((stepX, stepY))
					else:
						yield (stepX, stepY)

				if self.loopforever != True:
					break

		return

	@contextmanager
	def generator(self, mask_callback=None):
		try:
			self.mask_callback = mask_callback
			self._iterator_init()

			yield self._iterator

		except:
			raise

	@contextmanager
	def makeGenerator(self, layerNames, limit=None, batch_size=1, shuffle=False, mask_callback=None, **kwards):
		try:
			self.fname = './temp.h5'

			self.iterItems = layerNames
			self.iterOutput = layerNames
			self.limit = limit
			self.batch_size = batch_size
			self.shuffle = shuffle
			self.mask_callback = mask_callback

			d = {layerName: val.shape[1:] for layerName, val in kwards.items()}

			self.newGroup(fmode='w', **d)
			self.save(**kwards)

			del d
			del kwards

			self._iterator_init()

			yield self._iterator

		except:
			raise

		finally:
			if os.path.isfile('./temp.h5'):
				os.unlink('./temp.h5')