# This function creates a project the same way like a React project.
import argparse
import os

from models.project_definition.project_definition_model import ProjectDefinitionModel

parser = argparse.ArgumentParser()
parser.add_argument('-n', dest='name', type=str, required=True, help="Name of the new project.")
args = parser.parse_args()


def invoke():
    print("Creating Project...")
    project_name = args.name
    print("p: " + project_name)
    create_project(project_name)
    pass


def create_project(project_name: str):
    path = project_name

    # Check if the directory already exists.
    if os.path.exists(path):
        raise IsADirectoryError(f"Cannot create project {project_name}. "
                                f"The directory {project_name} already exists.")

    # It doesn't exist, so we can try to make the project here.
    os.mkdir(path)

    # Create a project definition and save it locally.
    project_definition_model = ProjectDefinitionModel()
    project_definition_model.model_path = path
    project_definition_model.project_name = project_name
    project_definition_model.save_to_local()
