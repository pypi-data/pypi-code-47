import os
import yaml

from zinc_cli.models.base_model import BaseModel


class ProjectDefinitionModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.project_name: str = "MyProject"
        self.model_path: str = ""

    def serialize(self):
        # Get serialized to a JSON Object.
        payload = {
            "project_name": self.project_name
        }
        return payload

    def get_local_path(self):
        return os.path.join(self.model_path, "project_definition.yaml")
        pass

    def save_to_local(self):
        # Saves the definition file locally.
        payload = self.serialize()
        path = self.get_local_path()
        with open(path, "w") as file:
            yaml.dump(payload, file)
