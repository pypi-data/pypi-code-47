#!/usr/bin/env python
# -*- coding: utf-8 -*-

from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.containerregistry import ContainerRegistryManagementClient
from taz.acr import ContainerRegistry
from msrestazure.azure_active_directory import MSIAuthentication
from azure.mgmt.containerinstance.container_instance_management_client \
    import ContainerInstanceManagementClient

from azure.mgmt.containerinstance.models import (ContainerGroup,
                                                 Container,
                                                 ContainerGroupNetworkProtocol,
                                                 ContainerPort,
                                                 EnvironmentVariable,
                                                 IpAddress,
                                                 Port,
                                                 ResourceRequests,
                                                 ResourceRequirements,
                                                 OperatingSystemTypes)

from taz.auth import UserAssignedIdentity
import json


class SimpleContainerGroup:

    """Summary
    
    Attributes:
        - client (ContainerInstanceManagementClient): ACI management client
        - command (string): container entry point
        - cpus (int): vcpus
        - env_vars (list): environment variables
        - group (ContainerGroup): container group
        - identity (TYPE): Description
        - image (TYPE): Description
        - instances (list): Description
        - location (TYPE): Description
        - mem (int): Description
        - name (TYPE): Description
        - os_type (TYPE): Description
        - resource_group_name (TYPE): Description
        - restart_policy (str): Description
    """
    
    def __init__(
            self,
            name,
            resource_group_name,
            location,
            image,
            subscription_id=None):    
        """
        Simple container group object with one instance
        
        Args:
            - name (str): container group name
            - resource_group_name (str): resource group
            - location (str): location (westeurope for example)
            - image (taz.acr.ContainerImage): ContainerImage object
            - subscription_id (None, optional, str): subscription 
                id if not default
        """
        try:
            if subscription_id is None:
                self.client = get_client_from_cli_profile(
                    ContainerInstanceManagementClient)
            else:
                self.client = get_client_from_cli_profile(
                    ContainerInstanceManagementClient,
                    subscription_id=subscription_id)
        except:
            self.client = ContainerInstanceManagementClient(
                MSIAuthentication())

        # Required parameters
        self.name = name
        self.resource_group_name = resource_group_name
        self.location = location
        self.image = image

        # default values
        self.cpus = 1
        self.mem = 1
        self.env_vars = []
        self.identity = None
        self.restart_policy = "Never"
        self.os_type = OperatingSystemTypes.linux
        self.command = None
        self.group = None
        self.instances = []

    def add_env_var(self, name, value):
        """
        add environement var
        
        Args:
            - name (str): env var name
            - value (str): env var value
        """
        self.env_vars.append(
            EnvironmentVariable(
                name=name,
                value=value))

    def set_cpus(self, cpus):
        """
        set cores number
        
        Args:
            - cpus (int): 1-4 (actual limit for westeurope)
        """
        self.cpus = cpus

    def set_mem(self, mem):
        """
        set amount of memory in GB
        
        Args:
            - mem (int): 1-14 (actual limit for westeurope)
        """
        self.mem = mem

    def set_identity(self, identity):
        """
        set user managed identity
        
        Args:
            - identity (taz.auth.UserAssignedIdentity): container group identity
        """
        self.identity = identity.get_container_group_identity()

    def set_command(self, command):
        """
        set command entry point of container
        
        Args:
            - command (str): entry point script of container
        """
        self.command = command

    def create(self):
        """
        Create the container group and instance
        """

        # Configure the container
        container_resource_requests = ResourceRequests(
            memory_in_gb=self.mem, cpu=self.cpus)
        container_resource_requirements = ResourceRequirements(
            requests=container_resource_requests)

        container = Container(
            name="container-001",
            image="{0}.azurecr.io/{1}:latest".format(
                self.image.container_registry.name,
                self.image.name),
            resources=container_resource_requirements,
            environment_variables=self.env_vars,
            command=self.command)

        group = ContainerGroup(
            location=self.location,
            containers=[container],
            os_type=self.os_type,
            restart_policy=self.restart_policy,
            image_registry_credentials=[
                self.image.container_registry.get_credentials()
            ],
            identity=self.identity)

        self.client.container_groups.create_or_update(
            self.resource_group_name,
            self.name,
            group)

        self.group = self.client.container_groups.get(
            self.resource_group_name,
            self.name)

        for instance in self.group.containers:
            self.instances.append(instance)

    def get_group(self):
        """
        Return container group attribute
        
        Returns:
            - azure.mgmt.containerinstance.models.ContainerGroup: container 
                group object
        """
        return self.group

    def get_instances(self):
        """
        Summary
        
        Returns:
            - [ azure.mgmt.containerinstance.models.Container ]: List of
                container instances
        """
        return self.instances

    def delete(self):
        """
        delete container group and his containers
        """
        self.client.container_groups.delete(
            self.resource_group_name,
            self.name)

    def __str__(self):
        """
        prints container group as json string
        
        Returns:
            - str: json encoded as string
        """
        
        instances =[]

        for instance in self.instances:
            try:
                state = instance.instance_view.current_state.state
            except:
                state = 'unknown'
            instances.append(
                {
                    'name': instance.name,
                    'image': instance.image,
                    'state': state,
                }
            )

        return json.dumps({ 
            'name': self.group.name,
            'cpus': self.cpus,
            'mem': self.mem,
            'restart_policy': self.restart_policy,
            'command': self.command,
            'instances': instances
        })