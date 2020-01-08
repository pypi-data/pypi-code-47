from azure.devops.connection import Connection
import pprint
import sys

def listProjects(credentials,organization_url):
 """ List Project and service connection on this project. Just print to test """
 connection = Connection(base_url=organization_url, creds=credentials)
 # Get a client (the "core" client provides access to projects, teams, etc)
 core_client = connection.clients.get_core_client()
 # Get the first page of projects
 get_projects_response = core_client.get_projects()
 index = 0
 while get_projects_response is not None:
     for project in get_projects_response.value:
         pprint.pprint("[" + str(index) + "] " + project.name)
         if sys.version_info.major > 2:
          result = getServiceEndPoint(credentials,organization_url, project.name)
         else:
          result = getServiceEndPoint(credentials,organization_url, (project.name).encode('utf-8'))
         for service_endpoint in result:
          print(service_endpoint.name)
          print(service_endpoint.type)
          print(service_endpoint.authorization)
         index += 1
     if get_projects_response.continuation_token is not None and get_projects_response.continuation_token != "":
         # Get the next page of projects
         get_projects_response = core_client.get_projects(continuation_token=get_projects_response.continuation_token)
     else:
         # All projects have been retrieved
         get_projects_response = None


def updateServiceEndPointAzureRmCredential(credentials,organization_url, project, spnId,spnKey):
 """ Update service connection azure rm . """
 result = getServiceEndPoint(credentials,organization_url, project)
 for service_endpoint in result:
  if service_endpoint.type == 'azurerm' and service_endpoint.authorization.parameters['serviceprincipalid'] == spnId :
   service_endpoint.authorization.parameters.update({'serviceprincipalkey':spnKey})
   print(service_endpoint.name)
   print(service_endpoint.id)
   print(service_endpoint.authorization.parameters)
   connection = Connection(base_url=organization_url, creds=credentials)
   service_client = connection.clients._connection.get_client('azure.devops.v5_1.service_endpoint.service_endpoint_client.ServiceEndpointClient')
   service_client.update_service_endpoint(service_endpoint, project, service_endpoint.id)   


def getServiceEndPoint(credentials,organization_url, project):
 """ Get service connection azure rm . """
 connection = Connection(base_url=organization_url, creds=credentials)
 service_client = connection.clients._connection.get_client('azure.devops.v5_1.service_endpoint.service_endpoint_client.ServiceEndpointClient') 
 get_service_endpoint_response = service_client.get_service_endpoints(project)
 return get_service_endpoint_response


if __name__ == "__main__":
    main()
