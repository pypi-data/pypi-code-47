from .base import ErConnector, ET, xmltodict
from .candidate import Candidate



def validate_rest(username, password):
    # using REST API. If valid, returns Candidate object. If not, returns False
    connector = ErConnector(api_version='rest')
    path = 'User/Validate?UserName={UserName}&Password={Password}&EntityID={EntityID}'.format(
        UserName=username,
        Password=password,
        EntityID=connector.rest_entity_id
    )
    params = {}
    params['UserName'] = username
    params['Password'] = password
    params['EntityID'] = connector.rest_entity_id
    try:
        result = (connector.send_request(
            path,
            payload=params,
            verb='POST',
        ))
        return Candidate(result['ReferenceID'])
    except Exception as e:
        return False

def lookup_rest(email):
    # using REST API.
    connector = ErConnector(api_version='rest')
    path = 'User/{entityid}/{email}'.format(
        email=email,
        entityid=connector.rest_entity_id
    )
    result = connector.send_request(
        path,
        verb='GET',
    )
    print(connector.api_user_guid_rest)
    try:
        data = result[0]
        return Candidate(data['CandidateID'], data=data)
    except:
        return result[0]


def get_candidate_data_rest(candidate_id):
    # using REST API.
    connector = ErConnector(api_version='rest')
    path = 'Candidate/{entityid}/{candidateid}'.format(
        candidateid=candidate_id,
        entityid=connector.rest_entity_id
    )
    result = connector.send_request(
        path,
        verb='GET',
        rawresponse=False
    )
    return result[0]

def list_candidate_custom_fields_rest(candidate_id, conversion_map=None, return_map_only=False):
    # using REST API.
    connector = ErConnector(api_version='rest')
    cfields = get_candidate_data_rest(candidate_id)['CustomFieldValues']
    out = []
    data = connector.convert_xml_to_json(cfields)
    for x in data:
        elem = {}
        for y in x.keys():
            val = x[y]
            if conversion_map and conversion_map.get(y, None):
                elem[conversion_map.get(y, None)] = val
                out.append(elem)
            else:
                if conversion_map and return_map_only:
                    pass
                else:
                    elem[y] = val
                    out.append(elem)
    return out

def parse_rest_result(result):
    parsed = str(result['Message']).split('|')
    return parsed[0], parsed[1]

def change_password_rest(candidate_id, newpassword, note=None):
    # using REST API.
    connector = ErConnector(api_version='rest')
    candidate = Candidate(candidate_id)
    path = 'Candidate/{entityid}/{candidateid}/Update/'.format(
        candidateid=candidate_id,
        entityid=connector.rest_entity_id
    )
    params = {}
    params['Email'] = candidate.email_address
    params['Password'] = newpassword
    params['WithPermissions'] = True
    params['ChangedByID'] = connector.api_user_guid_rest
    result = connector.send_request(
            path,
            payload=params,
            verb='POST',
        )

    status = int(parse_rest_result(result)[0])
    message = parse_rest_result(result)[0]
    if status == 100 and note:
        candidate.add_note(note)
    return message

