

def get_sg(sg_name: str, profile: str):
    import boto3
    sg_name = sg_name or 'jakub'
    profile = profile or 'default'

    ec2 = boto3.session.Session(profile_name=profile, region_name='eu-west-1').client('ec2')
    resp = ec2.describe_security_groups()
    target_sg_str = list(filter(lambda x: x['GroupName']==sg_name, resp['SecurityGroups']))
    return target_sg_str

def update_sg_to_ip(sg_name='jakub', ip='2.222.105.71/32', 
                    ports=[22, 8888], profile='default'):
    import boto3
    ec2 = boto3.session.Session(profile_name=profile, region_name='eu-west-1').client('ec2')
    profile = profile or 'default'

    target_sg_str = get_sg(sg_name, profile=profile)[0]
    ec2_res = boto3.session.Session(profile_name=profile, region_name='eu-west-1').resource('ec2')
    sg_res = ec2_res.SecurityGroup(target_sg_str['GroupId'])

    # TODO: make into a loop using ports
    # Removes all previous permissions from this group (hence `jakub`)
    if sg_res.ip_permissions!=[]:
        sg_res.revoke_ingress(IpPermissions=sg_res.ip_permissions)


    description = 'Jakub Aux Jupyter'
    description2 = 'Jakub Aux SSH'
    data = ec2.authorize_security_group_ingress(
            GroupId=target_sg_str['GroupId'],
            IpPermissions=[
                {'IpProtocol': 'tcp',
                'FromPort': 8888,
                'ToPort': 8888,
                'IpRanges': [{'CidrIp': ip, 'Description': description}] },
                {'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': ip, 'Description': description2}]}
            ])
    print('Ingress Successfully Set %s' % data)



# WIP 


# for permit in sg_res.ip_permissions:
#     ip_permit_map = { x['CidrIp']: permit for x in permit['IpRanges'] if x['Description'].startswith('Jakub') }
#     print(ip_permit_map)
    

# my_ip = '2.222.105.71/32'

# # sg_res.ip_permissions
# list( filter(lambda x: x['IpRanges']['Description'].startswith('Jakub'), sg_res.ip_permissions[0]))
# list(filter( list( filter(lambda x: descr_filter, y)) for y in sg_res )) 
# sg_res.ip_permissions[0]['IpRanges']
# sg_res.ip_permissions[0]['IpRanges'][0]['Description']