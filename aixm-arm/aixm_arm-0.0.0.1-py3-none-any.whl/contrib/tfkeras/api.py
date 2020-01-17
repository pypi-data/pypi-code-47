# @Time   : 2019-10-14
# @Author : zhangxinhao
from . import *
keras = tf.keras
from .model import *
from .layers import *
if False:
    import keras
    from keras.layers import *

    class ScaleLayer(Layer):
        pass

    def save_model(model, filepath, overwrite=True, include_optimizer=True,
                   save_format=None, signatures=None, options=None) -> None:
        """Saves a model as a TensorFlow SavedModel or HDF5 file.

         The saved model contains:
             - the model's configuration (topology)
             - the model's weights
             - the model's optimizer's state (if any)

         Thus the saved model can be reinstantiated in
         the exact same state, without any of the code
         used for model definition or training.

         _SavedModel serialization_ (not yet added)

         The SavedModel serialization path uses `tf.saved_model.save` to save the model
         and all trackable objects attached to the model (e.g. layers and variables).
         `@tf.function`-decorated methods are also saved. Additional trackable objects
         and functions are added to the SavedModel to allow the model to be
         loaded back as a Keras Model object.

         Arguments:
             model: Keras model instance to be saved.
             filepath: One of the following:
               - String, path where to save the model
               - `h5py.File` object where to save the model
             overwrite: Whether we should overwrite any existing model at the target
               location, or instead ask the user with a manual prompt.
             include_optimizer: If True, save optimizer's state together.
             save_format: Either 'tf' or 'h5', indicating whether to save the model
               to Tensorflow SavedModel or HDF5. Defaults to 'tf' in TF 2.X, and 'h5'
               in TF 1.X.
             signatures: Signatures to save with the SavedModel. Applicable to the 'tf'
               format only. Please see the `signatures` argument in
               `tf.saved_model.save` for details.
             options: Optional `tf.saved_model.SaveOptions` object that specifies
               options for saving to SavedModel.

         Raises:
             ImportError: If save format is hdf5, and h5py is not available.
         """
        pass


    def load_model(filepath, custom_objects=None, compile=True) -> keras.models.Model:
        # from tensorflow_core.python.keras.engine.training import Model
        """Loads a model saved via `save_model`.

          Arguments:
              filepath: One of the following:
                  - String, path to the saved model
                  - `h5py.File` object from which to load the model
              custom_objects: Optional dictionary mapping names
                  (strings) to custom classes or functions to be
                  considered during deserialization.
              compile: Boolean, whether to compile the model
                  after loading.

          Returns:
              A Keras model instance. If an optimizer was found
              as part of the saved model, the model is already
              compiled. Otherwise, the model is uncompiled and
              a warning will be displayed. When `compile` is set
              to False, the compilation is omitted without any
              warning.

          Raises:
              ImportError: if loading from an hdf5 file and h5py is not available.
              IOError: In case of an invalid savefile.
          """
        pass
