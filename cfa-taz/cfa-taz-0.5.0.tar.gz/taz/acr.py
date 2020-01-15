#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Taz library: Container Registry operations
"""

from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.containerregistry import ContainerRegistryManagementClient
from msrestazure.azure_active_directory import MSIAuthentication
from azure.mgmt.containerinstance.models import ImageRegistryCredential


class ContainerRegistry:

    """Summary
    
    Attributes:
        - client (TYPE): Description
        - credentials (TYPE): Description
        - name (TYPE): Description
        - resource_group (TYPE): Description
    """
    
    def __init__(self,
                 resource_group,
                 name,
                 subscription_id=None):

        try:
            if subscription_id is None:
                self.client = get_client_from_cli_profile(
                    ContainerRegistryManagementClient)
            else:
                self.client = get_client_from_cli_profile(
                    ContainerRegistryManagementClient,
                    subscription_id=subscription_id)

        except:
            self.client = ContainerRegistryManagementClient(
                MSIAuthentication())

        self.name = name
        self.resource_group = resource_group
        self.credentials = self.client.registries.list_credentials(
            resource_group, name)

    def get_credentials(self):
        return ImageRegistryCredential(
            server="{0}.azurecr.io".format(self.name),
            username=self.credentials.username,
            password=self.credentials.passwords[0].value)


class ContainerImage:

    """Summary

    Attributes:
        container_registry (TYPE): Description
        name (TYPE): Description
    """

    def __init__(self,
                 name,
                 container_registry):

        self.container_registry = container_registry
        self.name = name

    def get_name(self):
        return(self.name)
