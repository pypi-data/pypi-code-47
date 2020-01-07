import json
def Show(obj):
	tipo = type(obj).__name__
	if tipo in ('dict', 'list'):
		print( '\033[3m' + '\033[1;36m' + json.dumps(obj, sort_keys=True, indent=4, ensure_ascii=False) )
		print( '\x1b[3;30;46m' + ' ' + tipo + ' '  + '\x1b[0m' + '\033[1;36m' + '\033[0m')
	else:
		print( '\033[3m' + '\033[1;93m')
		print( obj )
		print( '\033[3;30;43m' + ' ' + tipo + ' '  + '\033[0m' + '\033[1;93m' + '\033[0m')
