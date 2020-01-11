QUERIES = {
    'PING': '''query {
                    ping
                }''',
    'LIST_NODES': '''query {
                        listNodes
                    }''',

    'GET_NODE': '''query ($id: ID){
                    getNode(id: $id){
                        id
                        name
                        state
                        text1
                        text2
                        more
                    }
                }''',
    'GET_NODE_FULL': '''query ($id: ID){
                            getNode(id: $id){
                                id
                                name
                                state
                                text1
                                text2
                                more
                                messages
                                errors
                            }
                        }'''
}

MUTATIONS = {
    'PUSH_NODE': '''mutation ($appName: String, $options: JSONObject){
                    pushNode(appName: $appName, options: $options) {
                        id
                        state
                        name
                        text1
                        text2
                        options
                        more
                    }
                }''',

    'ACTION_NODE':
        '''mutation ($nodeId: ID, $action:String, $options: JSON){
            actionNode(nodeId: $nodeId, action: $action, options: $options)
        }'''

}

SUBSCRIPTIONS = {
    'PING': '''subscription {
                    ping
                }''',
    'NODE': '''subscription ($id: ID){
                node(id: $id){
                    topic
                    node {
                        id
                        state
                    }
                    data
                }
            }''',
    'NODES': '''subscription nodes{
                nodes {
                    topic
                    at
                    node {
                        id
                        name
                        state
                    }
                }
            }''',
}
