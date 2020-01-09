import time
from datetime import datetime, date, timedelta

def timestamp():
	return int(time.time())

def timestamp2():
	return int(str(time.time()).replace('.', ''))

def get_date(ts = None, **param):

	if ts ==  None:
		ts = timestamp()

	data = [
		datetime.fromtimestamp( ts ).strftime('%Y-%m-%d'),
		datetime.fromtimestamp( ts ).strftime('%Y-%m-%d %H:%M:%S'),
		datetime.fromtimestamp( ts ).strftime('%d/%m/%Y'),
		datetime.fromtimestamp( ts ).strftime('%d/%m/%Y %H:%M:%S'),
	]

	if 'tipo' in param:
		if param['tipo'] == 'date':
			return data[0]
		elif param['tipo'] == 'datetime':	
			return data[1]
		elif param['tipo'] == 'datebr':	
			return data[2]
		elif param['tipo'] == 'datetimebr':	
			return data[3]
		else:
			return data			
	else:
		return data

def date_from_string(string):
	'''formato: 2019-09-18'''
	try:
		return datetime.strptime(string, '%Y-%m-%d').date()
	except Exception as e:
		return 'Erro no formato. Correto:YYYY-MM-DD'

def datetime_from_string(string):
	'''formato: 2019-09-18 13:55:26'''
	try:
		return datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
	except Exception as e:
		return 'Erro no formato. Correto:YYYY-MM-DD HH:MM:SS'

def date_from_string_br(string):
	'''formato: 18/09/2019'''
	try:
		return datetime.strptime(string, '%d/%m/%Y').date()
	except Exception as e:
		return 'Erro no formato. Correto:DD/MM/AAAA'

def datetime_from_string_br(string):
	'''formato: 18/09/2019 13:55:26'''
	try:
		return datetime.strptime(string, '%d/%m/%Y %H:%M:%S')
	except Exception as e:
		return 'Erro no formato. Correto:DD/MM/AAAA HH:MM:SS'

def date_to_datebr(string):
	return date_from_string(string).strftime('%d/%m/%Y')

def datebr_to_date(string):
	return date_from_string_br(string).strftime('%Y-%m-%d')

def diff_datetime(d1, d2):
	fmt = '%Y-%m-%d %H:%M:%S'
	dt1 = datetime.strptime(d1, fmt)
	dt2 = datetime.strptime(d2, fmt)
	diff = (dt2 - dt1).total_seconds()
	
	df = divmod(diff, 60)
	minutos = df[0] + (df[1] / 100)

	return dict(
			segundos = int( diff ),
			minutos = minutos,
			dias = int( divmod( diff, 86400 )[0] ),
			horas = int( divmod( diff, 3600 )[0] ),
			anos = int( divmod( diff, 31556926 )[0] )
		)

def sleep(segundos):
	time.sleep( int(segundos) )

