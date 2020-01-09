import json

def show(obj):
	tipo = type(obj).__name__

	code = '\033['

	if tipo == 'dict':
		code += '96;1;'
		code_pre = code[:-1]+'m'
		code += '7;'
		code_end = code[:-1]+'m'
	elif tipo == 'list':
		code += '92;1;'
		code_pre = code[:-1]+'m'
		code += '7;'
		code_end = code[:-1]+'m'
	elif tipo == 'int':
		code += '93;1;'
		code_pre = code[:-1]+'m'
		code += '7;'
		code_end = code[:-1]+'m'
	elif tipo == 'str':
		code += '97;1;'
		code_pre = code[:-1]+'m'
		code += '7;'
		code_end = code[:-1]+'m'
	elif tipo == 'float':
		code += '95;1;'
		code_pre = code[:-1]+'m'
		code += '7;'
		code_end = code[:-1]+'m'
	else:
		code += '91;1;'
		code_pre = code[:-1]+'m'
		code += '7;'
		code_end = code[:-1]+'m' + '\033[91;1;5m'

	print(code_pre + '↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
	try:
		if tipo == 'tuple':
			print(obj)
		else:
			r = json.dumps(obj, sort_keys=True, indent=4, ensure_ascii=False)
			print( r )
	except Exception as e:
		# print( '\033[91;1;3mErro no dumps do objeto' )
		print( obj )
	finally:
		print(code_end, '↑ ' + tipo, '\033[0m')

def niceprint(obj, **kwargs):
	
	cor_args = list(kwargs.pop('cor', ''))

	code = '\033['
	if 'k' in cor_args:
		code += '90;'
	elif 'r' in cor_args:
		code += '91;'
	elif 'g' in cor_args:
		code += '92;'
	elif 'y' in cor_args:
		code += '93;'
	elif 'b' in cor_args:
		code += '94;'
	elif 'm' in cor_args:
		code += '95;'
	elif 'c' in cor_args:
		code += '96;'
	elif 'w' in cor_args:
		code += '97;'

	if 'B' in cor_args:
		code += '1;'
	if 'D' in cor_args:
		code += '2;'
	if 'I' in cor_args:
		code += '3;'
	if 'U' in cor_args:
		code += '4;'
	if 'F' in cor_args:
		code += '5;'
	if 'R' in cor_args:
		code += '7;'
	if 'C' in cor_args:
		code += '9;'

	print(code[:-1]+'m', obj, '\033[0m')
