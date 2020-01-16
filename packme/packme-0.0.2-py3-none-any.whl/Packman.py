#!/usr/bin/env python3

#################################################################
# This apps allows the creation of packer json file out of
# YAML template
# One of its main feature is to handle template inheritance
# which is not covered yet natively by packer
# To run the application:
# env_var_1 env_var_2 ... env_var_n rackman.py template.yml
# where env_var_1 ... env_var_n are environment variables
# passed at the command line level and template.yml is the YAML
# which contain the packer configuration
#################################################################

import collections
import os
import shutil
import subprocess
import yaml

from .PackerTemplate import PackerTemplate

class Packman:
    """This class implements the Packman engine for generating packer template json files and run packer optionally .
    """

    def __init__(self, input_file, templates_dir):
        """Constructor.

        Parameters
        ----------
        input_file: str
            Path to the Packman input file.
        """

        # The base directory for templates
        self._templates_dir = os.path.abspath(templates_dir)

        with open(input_file, "r") as fin:
            data = yaml.safe_load(fin)

        # The input file must ne a YAML file which declares a 'templates' dictionary
        if "templates" not in data:
            raise IOError("Invalid YAML file: must contains 'templates' tag")

        self._templates = data["templates"]

    def get_template(self, template_name):
        """Return the YAML contents of a given template.

        Parameters
        ----------
        template_name: str
            The name of the template to fetch.

        Returns
        -------
        :obj: `PackerTemplate`

            The YAML contents of the template to be fetched.
        """

        return self._templates[template_name] if isinstance(self._templates[template_name],dict) else {}

    def _build_template(self, template_name):
        """Build a PackerTemplate object from a template name.

        Parameters
        ----------
        template_name: str
            The name of the template to build.

        Returns
        -------
        :obj: `PackerTemplate`

            The template object used by packman to build the manifest.json file.        
        """

        # Fetch the template matching template_name key
        template_node = self.get_template(template_name)

        # Build the path for the template manifest file (YAML)
        manifest_file = os.path.join(self._templates_dir,template_name,"manifest.yml")
        
        # Opens the file and load its contents
        try:
          fin = open(manifest_file, "r")
        # If the file does not exist, the manifest contents is just an empty dict
        except FileNotFoundError:
            manifest_data = {}
        else:
            manifest_data = yaml.safe_load(fin)

        # Get the packages node which gives the list of non-standard applications to add to the packer process 
        packages = template_node.get("packages", [])

        # Build a PackerTemplate object that can be dumped to a manifest.json file
        template = PackerTemplate(template_name, manifest_data, packages)

        return template

    def _build_template_hierarchy(self, template_name, hierarchy):
        """Build a single template hierarchy.

        A template can have a parent template. In that case for packer neig able to run on those templates, 
        the parent tenplate must have been built before.

        Getting a hierarchy of templates, the first one being  the ones with no parent is the goal of this method.

        Parameters
        ----------
        template_name: str
            The template on which the hierarchy will be built upon.

        hierarchy: list
            A list of strings corresponding tot the template hierarchy.

            This argument is just used for passing the template hierarchy across recursive calls of this method. 
        """

        # Fetch the template matching template_name key
        template_node = self.get_template(template_name)

        extends = template_node.get("extends",None)

        hierarchy.append(template_name)

        if extends is None:
            return

        else:
            self._build_template_hierarchy(extends, hierarchy)
            
    def _build_config_hierarchy(self, selected_templates=None):
        """Build the templates hierarchy.

        A template can have a parent template. In that case for packer neig able to run on those templates, 
        the parent tenplate must have been built before.

        Getting a hierarchy of templates, the first one being  the ones with no parent is the goal of this method.

        Parameters
        ----------
        selected_templates: list, optional
            List of strings corresponding to the packer templates from which the hierarchy should be built.

        Returns
        -------
        List of str
            Returns the hierarchy of templates from the one with no parent to the ones with parents.
        """

        if selected_templates is None:
            templates = set(self._templates.keys())
        else:
            # Filter out the image names not present in the yaml file
            templates = set([template for template in selected_templates if template in self._templates])

        config_hierarchy = []
        for template in templates:
            self._build_template_hierarchy(template, config_hierarchy)

        config_hierarchy.reverse()
        config_hierarchy = list(collections.OrderedDict.fromkeys(config_hierarchy))

        return config_hierarchy

    def run(self, selected_templates=None, log=False):
        """Run packer on the generated manifest.json files.

        Parameters
        ----------
        selected_templates: list, optional
            List of strings corresponding to the packer templates to ru with packer.
        """

        # Check first that packer program is installed somewhere
        if shutil.which("packer") is None:
            raise FileNotFoundError("packer could not be found.")

        # Set env variables for packer run environment
        packer_env = os.environ.copy()
        # This allow to speed up the typing of the preseed command line
        packer_env["PACKER_KEY_INTERVAL"] = "10ms"
        # This will add log output for packer run    
        packer_env["PACKER_LOG"] = "1" if log else "0"

        # Define the template hierarchy for the selected templates
        config_hierarchy = self._build_config_hierarchy(selected_templates)

        # Save the current directory
        current_dir = os.getcwd()

        # Loop over the template hierarchy and run packer
        for template in config_hierarchy:

            # cd to the the template directory
            current_template_dir = os.path.join(self._templates_dir,template)

            build_dir = os.path.join(current_template_dir,"builds",template)

            if os.path.exists(build_dir):
                print("An image already exists for {} template. This image will be used.".format(template))
                continue

            print("Building image for {}:".format(template))

            os.chdir(current_template_dir)

            # Run packer upon the manifest.json file
            manifest_json = os.path.join(current_template_dir,"manifest.json")
            subprocess.Popen(["packer","build",manifest_json], env=packer_env)

        # cd back to the current dir
        os.chdir(current_dir)
                    
    def build(self, selected_templates=None, **kwargs):
        """Build packer on the generated manifest.json files.

        Parameters
        ----------
        selected_templates: list, optional
            List of strings corresponding to the packer templates to build.

        run: bool, optional
            If True packer will be run from the generated manifest.json files.
        """

        if selected_templates is None:
            templates = self._templates.keys()
        else:
            # Filter out the image names not present in the yaml file
            templates = [template for template in selected_templates if template in self._templates]

        # Loop over the selected templates
        for template_name in templates:

            template = self._build_template(template_name)
            template_node = self.get_template(template_name)

            # Fetch the parent template if any
            parent_template = template_node.get("extends", None)
            if parent_template is not None:
                parent_template = self._build_template(parent_template)
                template.set_parent(parent_template)

            # Dump the template
            ouput_file = os.path.join(self._templates_dir,template_name,"manifest.json")
            template.dump(ouput_file,**kwargs)

