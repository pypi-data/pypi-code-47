from azure.keyvault.secrets import SecretClient
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient

def getSecretFromKeyVault(keyVaultName: str, secretName: str):
    keyVaultUri = "https://" + keyVaultName + ".vault.azure.net"
    credential = get_client_from_cli_profile(ComputeManagementClient).config.credentials
    client = SecretClient(keyVaultUri, credential)

    return client.get_secret(secretName).value

def setSecretInKeyVault(keyVaultName: str, secretName: str, secretValue):
    keyVaultUri = "https://" + keyVaultName + ".vault.azure.net"
    credential = get_client_from_cli_profile(ComputeManagementClient).config.credentials
    client = SecretClient(keyVaultUri, credential)
    client.set_secret(secretName, secretValue)
