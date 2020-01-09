from dataclasses import asdict, dataclass

from marmot.ml.ensemble_model import EnsembleRidge, BaseEnsembleModel
from marmot.ml.preprocess import BaseFillna, MeanFillna, KneignborFillna
from marmot.ml.aggregate import BaseAggregate, MeanAggregate, MedianAggregate


@dataclass
class BaseModelConfig:

    fillna: str = "MeanFillna"

    poly: int = 1

    scale = True

    ensemble_layer: str = "EnsembleRidge"

    aggregate: str = "AverageAggregate"

    class Meta:
        ordered = True


if __name__ == '__main__':
    import marshmallow_dataclass
    import json
    import os

    ModelSchema = marshmallow_dataclass.class_schema(BaseModelConfig)
    config = BaseModelConfig()
    config_json = ModelSchema().dump(config)

    print(config_json)
    print(type(config_json))
    if os.path.exists("example/test.json"):
        os.remove("example/test.json")

    with open("example/test.json", "w") as f:
        json.dump(config_json, f, indent=4)

    with open("example/test.json", "r") as f:
        json_config = json.load(f)

    config_2 = ModelSchema().load(json_config)
    print(config_2)

