from pathlib import Path
import ast
import os

class TCParser():
     def __init__(self, directory_path:[]):
          self.directory_list = directory_path

     def get_list_of_class(self):
          lst_class = []

          for directory_path in self.directory_list:
               pathlist = Path(directory_path).glob('**/*.py')
               for path in pathlist:
                    path_in_str = str(path)
                    with open(path_in_str, "r") as source:
                         tree = ast.parse(source.read())
                         classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
                         lst_class.append({
                              "file_path": os.path.splitext(path_in_str)[0] + "/" + classes[0],
                              'class_name': classes[0]
                         })
          return lst_class
