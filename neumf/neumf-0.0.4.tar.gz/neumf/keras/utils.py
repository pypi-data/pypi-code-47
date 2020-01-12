import tensorflow as tf, numpy as np

def shared_shuffle(arrays):
    idx = np.arange(len(arrays[0]))
    np.random.shuffle(idx)
    return (arr[idx] for arr in arrays)

def shared_sort(arrays, which=0):
    idx = np.argsort(arrays[which])
    return (arr[idx] for arr in arrays)

def batch_idx(i, batch_size):
    return i * batch_size, (i + 1) * batch_size

def sparse_to_dense_grads(grads_and_vars):
  """Convert sparse gradients to dense gradients.
  All sparse gradients, which are represented as instances of tf.IndexedSlices,
  are converted to dense Tensors. Dense gradients, which are represents as
  Tensors, are unchanged.
  The purpose of this conversion is that for small embeddings, which are used by
  this model, applying dense gradients with the AdamOptimizer is faster than
  applying sparse gradients.
  Args
    grads_and_vars: A list of (gradient, variable) tuples. Each gradient can
      be a Tensor or an IndexedSlices. Tensors are unchanged, and IndexedSlices
      are converted to dense Tensors.
  Returns:
    The same list of (gradient, variable) as `grads_and_vars`, except each
    IndexedSlices gradient is converted to a Tensor.
  """

  # Calling convert_to_tensor changes IndexedSlices into Tensors, and leaves
  # Tensors unchanged.
  return [(tf.convert_to_tensor(g), v) for g, v in grads_and_vars]

def _strip_first_and_last_dimension(x, batch_size):
  return tf.reshape(x[0, :], (batch_size,))


def convert_to_softmax_logits(logits):
  """Convert the logits returned by the base model to softmax logits.
  Args:
    logits: used to create softmax.
  Returns:
    Softmax with the first column of zeros is equivalent to sigmoid.
  """
  softmax_logits = tf.concat([logits * 0, logits], axis=1)
  return softmax_logits

def softmax_sparse_softmax_cross_entropy_with_logits(labels, logits):
    softmax_logits = convert_to_softmax_logits(logits)
    # print(logits, softmax_logits)
    # loss = tf.nn.sparse_softmax_cross_entropy_with_logits(
    #     labels=labels,
    #     logits=logits#softmax_logits
    # )
    loss = tf.nn.softmax_cross_entropy_with_logits(
        labels=labels,
        logits=softmax_logits
    )

    return loss



def mask_duplicates(x, axis=1):  # type: (np.ndarray, int) -> np.ndarray
    """Identify duplicates from sampling with replacement.
    Args:
    x: A 2D NumPy array of samples
    axis: The axis along which to de-dupe.
    Returns:
    A NumPy array with the same shape as x with one if an element appeared
    previously along axis 1, else zero.
    """
    if axis != 1:
        raise NotImplementedError

    x_sort_ind = np.argsort(x, axis=1, kind="mergesort")
    sorted_x = x[np.arange(x.shape[0])[:, np.newaxis], x_sort_ind]

    # compute the indices needed to map values back to their original position.
    inv_x_sort_ind = np.argsort(x_sort_ind, axis=1, kind="mergesort")

    # Compute the difference of adjacent sorted elements.
    diffs = sorted_x[:, :-1] - sorted_x[:, 1:]

    # We are only interested in whether an element is zero. Therefore left padding
    # with ones to restore the original shape is sufficient.
    diffs = np.concatenate([
        np.ones((diffs.shape[0], 1), dtype=diffs.dtype),
        diffs
    ], axis=1)

    # Duplicate values will have a difference of zero. By definition the first
    # element is never a duplicate.
    return np.where(diffs[np.arange(x.shape[0])[:, np.newaxis], inv_x_sort_ind], 0, 1)
