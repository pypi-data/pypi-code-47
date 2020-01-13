import numpy as np


class Shape(object):
	def contains(self, points):
		raise NotImplementedError


class SphericalPatch(Shape):
	def __init__(self, theta_min, theta_max, phi_min, phi_max):
		self.theta_min = theta_min
		self.theta_max = theta_max
		self.phi_min = phi_min
		self.phi_max = phi_max

	def contains(self, points):
		# Calculate theta, phi for these points
		x, y, z = points.T
		r = np.linalg.norm(points, axis=1)
		theta = np.arccos(z / r)
		phi = np.arctan2(y, x)
		return (self.theta_min < theta) & (theta < self.theta_max) & \
			(self.phi_min < phi) & (phi < self.phi_max)
