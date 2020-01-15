#!/usr/bin/env python
# -*- coding: utf-8 -*-

from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.msi import ManagedServiceIdentityClient
from azure.mgmt.containerinstance.models import ContainerGroupIdentity
from msrestazure.azure_active_directory import MSIAuthentication


class UserAssignedIdentity:

    """User Assigned identity
    
    Attributes:
        - client (ManagedServiceIdentityClient): MSI client
        - container_group_identity (ContainerGroupIdentity): identity to use
        with container group
        - identity (TYPE): Description
        - managed_identity_name (TYPE): Description
        - resource_group_name (string): Resource Group
        - subscription_id (string): subscription id
    """
    
    def __init__(self, resource_group_name, managed_identity_name, subscription_id=None):
        """
        Create a user assigned identity object

        Args:
            resource_group (string): resource group name
            managed_identity (string): managed identity name
            subscription_id (None, optional): subscription id (if None default)
        """
        try:
            if subscription_id is None:
                self.client = get_client_from_cli_profile(
                    ManagedServiceIdentityClient)
            else:
                self.client = get_client_from_cli_profile(
                    ManagedServiceIdentityClient,
                    subscription_id=subscription_id)
        except:
            self.client = ManagedServiceIdentityClient(MSIAuthentication())

        self.subscription_id = subscription_id
        self.resource_group_name = resource_group_name
        self.managed_identity_name = managed_identity_name

    def get_identity(self):
        self.identity = self.client.user_assigned_identities.get(
            self.resource_group_name,
            self.managed_identity_name)

        return self.identity

    def get_container_group_identity(self):
        self.get_identity()

        self.container_group_identity = ContainerGroupIdentity(
            type='UserAssigned',
            user_assigned_identities={self.identity.id: {}}
        )
        return self.container_group_identity


class MsiAuthentication:
    def __init__(self):
        self.credentials = MSIAuthentication()

    def get_credentials(self):
        return self.credentials
