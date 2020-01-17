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
import glob
import jinja2
import json
import os
import pprint
import yaml

class PackerTemplate:
    """This class implements one packer template.
    Basically, a packer template is made of four sections:
    - description: a string that explains the purpose of the template
    - variables: a dictionary of variables used in the template through jinja2 mechanism
    - builders: a list of dictionaries where each dictionary defines the type of image that will be built
    - provisioners: a list of dictionaries where each dictionary defines actions used to configure the image
    - processors: a list of dictionaries where each dictionary defines actions to be run after the image is built
    """

    def __init__(self, name, yaml_node, packages):

        self._name = name

        self._parameters = yaml_node.get("parameters", {})

        # Fetch the 'packer' node
        packer_node = yaml_node.get("packer", {})

        # Fetch the 'description' node from the packer node
        self._description = packer_node.get("description", "No description provided")

        # Fetch the '_variables' node from the packer node
        self._variables = packer_node.get("variables", {})

        # Fetch the 'builders' node from the packer node
        self._builders = packer_node.get("builders", [])

        # Fetch the 'provisioners' node from the packer node
        self._provisioners = packer_node.get("provisioners", [])

        # Fetch the 'postprocessors' node from the packer node
        self._postprocessors = packer_node.get("postprocessors", [])

        bin_dir = os.path.realpath(os.path.dirname(__file__))
        root_dir = os.path.dirname(bin_dir)
        self._packages_root_dir = os.path.join(root_dir,"packages")
        self._templates_dir = os.path.join(root_dir,"templates")

        self._load_packages(packages)

    @property
    def builders(self):
        """Property for _builders attribute.

        Returns
        -------
        list
            The list of packer builders for this PackerTemplate.
        """

        return self._builders

    @property
    def description(self):
        """Property for _description attribute.

        Returns
        -------
        str
            The description of this PackerTemplate.
        """

        return self._description

    @property
    def name(self):
        """Property for _name attribute.

        Returns
        -------
        str
            The name of this PackerTemplate.
        """

        return self._name

    @property
    def parameters(self):
        """Property for _parameters attribute.

        Returns
        -------
        dict
            The parameters that will be used by Jinja 2 when creating the template json file.
        """

        return self._parameters

    @property
    def postprocessors(self):
        """Property for _postprocessors attribute.

        Returns
        -------
        list
            The list of packer postprocessors for this PackerTemplate.
        """

        return self._postprocessors

    @property
    def provisioners(self):
        """Property for _provisioners attribute.

        Returns
        -------
        list
            The list of packer provisioners for this PackerTemplate.
        """

        return self._provisioners

    @property
    def variables(self):
        """Property for _variables attribute.

        Returns
        -------
        list
            The list of packer variables for this PackerTemplate.
        """

        return self._variables

    def set_parent(self, parent_template):
        """Set the parent template to this PackerTemplate.

        This defines a relationship for future packer run in the sense that the child template will start directly from the image of 
        its parent template.

        Parameters
        ----------
        parent_template: :obj: `PackerTemplate`
            The PackerTemplate of the parent template to connect the child template with.
            
        """

        # List of the builder names for the child template
        child_builder_names = [builder["name"] for builder in self._builders]

        # Loop over the builder of the parent template
        for builder in parent_template.builders:

            builder_name = builder["name"]

            # If this is a builder specific to the parent config, copy it in the child config and set it with an image dependency
            if builder_name not in child_builder_names:
                parent_builder = {}
                parent_builder["name"] = builder_name
                parent_builder["type"] = builder["type"]
                parent_builder["vm_name"] = self._name
                parent_builder["iso_url"] = "./builds/{}-{}".format(parent_template.name, builder_name)
                parent_builder["iso_checksum_type"] = "none"
                parent_builder["iso_checksum_url"] = "none"
                parent_builder["output_directory"] = os.path.join(self._templates_dir,self._name)
                self._builders.insert(0,parent_builder)

            # If the builder is also defined in the child config, use the child config one and specify the image dependency
            else:

                builder = next((b for b in self._builders if b["name"] == builder_name),None)
                if builder is None:
                    continue

                builder["vm_name"] = self._name
                builder["iso_url"] = "./builds/{}-{}".format(parent_template.name, builder_name)
                builder["iso_checksum_type"] = "none"
                builder["iso_checksum_url"] = "none"
                builder["output_directory"] = os.path.join(self._templates_dir,self._name)            

    def _load_packages(self, packages):
        """Load the non-standard package YAML file and append them as provisioners of this PackerTemplate.

        Parameters
        ----------
        list
            The list of the packages to append.    
        """

        # If *" is in the list, fetch all the packages
        if "*" in packages:
            packages_dir = glob.glob(os.path.join(self._packages_root_dir,"*"))
        # Otherwise just fetch the selected ones
        else:
            packages_dir = []
            for package in packages:
                package_dir = os.path.join(self._packages_dir,package)
                if os.path.exists(package_dir) and os.path.isdir(package_dir):
                    packages_dir.append(package_dir)

        # Loop over the packages directories
        for package_dir in packages_dir:
            
            # Build the path to the package manifest file (YAML)
            manifest_file = os.path.join(package_dir,"manifest.yml")
            
            # Open and load the provisioners list from the manifest file
            try:
              fin = open(manifest_file, "r")
            # If the manifest does not exist, the provisioners list is set to an empty list
            except FileNotFoundError:
                manifest_data = []
            else:
                manifest_data = yaml.safe_load(fin)
                manifest_data = manifest_data["provisioners"]

            # Loop over the provisioners list and update when necessary relative paths with absolute one for packer to run correctly
            for provisioner in manifest_data:
                if provisioner["type"] in ["file"]:
                    provisioner["source"] = os.path.join(package_dir,provisioner["source"])
                elif provisioner["type"] in ["shell"]:
                    provisioner["script"] = os.path.join(package_dir,provisioner["script"])

            # Extend the current provisioners list with the ones of the selected packages
            self._provisioners.extend(manifest_data)
            
    def dump(self, output_file, **kwargs):
        """Dump this PackerTemplate to a file.

        Parameters
        ----------
        output_file: str
            The path to the output json file for this PackerTemplate.
        """

        # Get the basename and the ext of the output_file
        basename, ext = os.path.splitext(output_file)
        # If the ext is different from .json set it to .json
        if ext != ".json":
            ext = ".json"

        # Reformat the output_file
        output_file = "{}{}".format(basename, ext)

        # This will be the node to be dumped
        node = {}
        node["description"] = self._description
        node["variables"] = self._variables
        node["builders"] = self._builders
        node["provisioners"] = self._provisioners
        node["post-processors"] = self._postprocessors

        # Render the jinja2 templates with the parameters dictionary provided in the template file and the available environment variables
        jinja_template = jinja2.Template(repr(node))
        s = jinja_template.render(parameters=self._parameters, environment=os.environ)

        # Dump to the output file
        with open(output_file, "w") as fout:
            json.dump(yaml.safe_load(s), fout, **kwargs)

    def __str__(self):
        """Returns fancy output for this PackerTemplate.

        Returns
        -------
        str
            The string that will result from a str call to a PackerTemplate object.
        """

        d = collections.OrderedDict()
        d["description"] = self._description
        d["variables"] = self._variables
        d["builders"] = self._builders
        d["provisioners"] = self._provisioners
        d["post-processors"] = self._postprocessors

        return pprint.pformat(d)



