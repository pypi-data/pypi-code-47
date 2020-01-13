import numpy as np


def spherical_sample(patch, n):
	"""Generate `n` length-1 vectors within `patch`"""
	points = np.zeros((n, 3))
	n_sampled = 0
	# Start with random Cartesian points, `n` at a time
	while n_sampled < n:
		batch = 0.5 - np.random.random(size=(n, 3))
		# Filter an isotropic non-zero sample
		norms = np.linalg.norm(batch, axis=1)
		iso_mask = (norms > 0) & (norms <= 0.5)
		batch = batch[iso_mask]
		norms = norms[iso_mask]
		# Filter by inclusion in `patch`
		inclusion_mask = patch.contains(batch)
		batch = batch[inclusion_mask]
		norms = norms[inclusion_mask]
		# Normalize
		batch /= norms[:, np.newaxis]
		# Add to count
		if len(batch):
			points[
				n_sampled:(
					min(n_sampled + len(batch), n)
				)] = batch[:min(n - n_sampled, len(batch))]
			n_sampled += len(batch)
	return points
