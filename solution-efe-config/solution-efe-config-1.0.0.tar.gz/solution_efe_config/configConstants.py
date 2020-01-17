from solution_efe_config.configService import Config
data=Config()
constants=data.yamlToDict()
DEBUG=constants.get('debug', True)
MYSQL = {}
MYSQL['host']=constants.get('mysql.host', 'localhost')
MYSQL['port']=constants.get('mysql.port', 3306)
MYSQL['user']=constants.get('mysql.user', 'root')
MYSQL['password']=constants.get('mysql.password', 'root')
MYSQL['name']=constants.get('mysql.name', 'bdname')

HTTP={}
HTTP['host']=constants.get('http.host', '0.0.0.0')
HTTP['port']=constants.get('http.port', 3000)

TCP={}
TCP['host']=constants.get('tcp.host', '0.0.0.0')
TCP['port']=constants.get('tcp.port', 3000)

SWAGGER = {}
SWAGGER['host']=constants.get('swagger.host', '0.0.0.0')

CLIENTS={}
CLIENTS['security']=constants.get('client.security', {'host':'0.0.0.0','port':3000})
CLIENTS['mailing']=constants.get('client.mailing', {'host':'0.0.0.0','port':3000})
CLIENTS['notification']=constants.get('client.notification', {'host':'0.0.0.0','port':3000})
CLIENTS['document']=constants.get('client.document', {'host':'0.0.0.0','port':3000})
CLIENTS['user']=constants.get('client.user', {'host':'0.0.0.0','port':3000})
CLIENTS['objective']=constants.get('client.objective', {'host':'0.0.0.0','port':3000})
CLIENTS['member']=constants.get('client.member', {'host':'0.0.0.0','port':3000})
CLIENTS['learning']=constants.get('client.learning', {'host':'0.0.0.0','port':3000})
CLIENTS['leader']=constants.get('client.leader', {'host':'0.0.0.0','port':3000})
CLIENTS['event']=constants.get('client.event', {'host':'0.0.0.0','port':3000})
CLIENTS['profile']=constants.get('client.profile', {'host':'0.0.0.0','port':3000})