from azure.mgmt.containerservice  import ContainerServiceClient
from azure.graphrbac import GraphRbacManagementClient
from az_k8s_operations import spn 

def rotateKeysForK8sCluster( azure_credential,graph_credentials,TENANT_ID, subscription,resource_group_name,cluster_name,nbDays):
    """ Rotate spn key of cluster and spn key for server rbac spn
        Update kv infra in rg
        Update service connection of linked azure devops project"""

    print("==Start of rotateKeysForK8sCluster")
    graphrbac_client = GraphRbacManagementClient(graph_credentials, TENANT_ID)
    K8sClient = ContainerServiceClient(azure_credential,subscription)
    cluster = K8sClient.managed_clusters.get(resource_group_name,cluster_name)
    print(("Cluster_app_id: "+cluster.service_principal_profile.client_id))
    #listKeys = graphrbac_client.applications.list_password_credentials(spn.getObjectIdFromAppId(TENANT_ID,graph_credentials,cluster.service_principal_profile.client_id ))
    newKeyValueCluster = spn.update_password_key(graph_credentials,TENANT_ID,
             spn.getObjectIdFromAppId(TENANT_ID,graph_credentials,cluster.service_principal_profile.client_id ), nbDays,'Cluster',"create")
    print(newKeyValueCluster)
    if cluster.aad_profile:
     print(("RBAC_server_app_id: "+cluster.aad_profile.server_app_id))
    # listKeys = graphrbac_client.applications.list_password_credentials(spn.getObjectIdFromAppId(TENANT_ID,graph_credentials,cluster.aad_profile.server_app_id ))
     newKeyValueServer = spn.update_password_key(graph_credentials,TENANT_ID,
              spn.getObjectIdFromAppId(TENANT_ID,graph_credentials,cluster.aad_profile.server_app_id ), nbDays,'rbacServer',"create")
     print(newKeyValueServer)
    print("==End of rotateKeysForK8sCluster")
