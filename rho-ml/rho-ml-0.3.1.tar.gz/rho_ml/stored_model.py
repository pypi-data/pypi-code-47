import base64
import importlib
import json
from typing import Type

import attr
from rho_ml.rho_model import RhoModel


@attr.s(auto_attribs=True, frozen=True)
class StoredModel(object):
    """ This stores the bytes of a serialized model, along with the module and
    qualified class name needed to correctly deserialize the model later. """
    module_name: str
    class_name: str
    model_bytes: bytes

    @classmethod
    def from_model(cls, model: Type[RhoModel]):
        return cls(module_name=model.__module__,
                   class_name=model.__class__.__qualname__,
                   model_bytes=model.serialize())

    def load_model(self) -> RhoModel:
        """ Use the instantiated StoredPredictor to load the Predictor using
        the appropriate class. """
        predictor_module = importlib.import_module(self.module_name)
        predictor_cls = getattr(predictor_module, self.class_name)
        predictor = predictor_cls.deserialize(self.model_bytes)
        return predictor

    def to_json(self) -> str:
        """ JSON serialize the StoredPredictor so it can be saved to Redis, S3,
        etc. This uses base64 encoding on the predictor bytes, so it is often
        not going to be the most efficient way to store a given model. """
        # todo: consider encoding module_name and class_name in redis/s3 keys
        # todo: consider alternate encodings
        # todo: test out base64 performance, both memory and speed
        storage_dict = attr.asdict(self)
        storage_dict['model_bytes'] = base64.encodebytes(
            storage_dict['model_bytes']).decode('ascii')
        return json.dumps(storage_dict)

    @classmethod
    def from_json(cls, storage_json: str):
        storage_dict = json.loads(storage_json)
        encoded_model = storage_dict['model_bytes'].encode('ascii')
        storage_dict['model_bytes'] = base64.decodebytes(encoded_model)
        return cls(**storage_dict)
