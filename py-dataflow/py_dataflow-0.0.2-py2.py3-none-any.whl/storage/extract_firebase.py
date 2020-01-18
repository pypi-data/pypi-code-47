from collections import OrderedDict
from utils import firebase


db = firebase.connect_firebase()
# results = db.child("users").push(data, user['idToken'])
# results = db.push('invest': extract.get('invest'))

def saveFirebase(extract= {}):
	# import ipdb; ipdb.set_trace()
	# extract = {"saldo": "61.33", "transactions": [{"data": "21-03-2018", "descricao": "SAQUE NO BANCO 24 HORAS", "docto": "338164", "value": "-20.00"}, {"data": "21-03-2018", "descricao": "SAQUE NO BANCO 24 HORAS", "docto": "223164", "value": "-20.00"}, {"data": "21-03-2018", "descricao": "TED MESMA TITULARIDADE STR         102-0002-000000039370", "docto": "000000", "value": "-100.00"}, {"data": "21-03-2018", "descricao": "RESG POUP - SUPERLINHA / INTERNET  DE: 0001.60.044669-6", "docto": "323369", "value": "200.00"}, {"data": "20-03-2018", "descricao": "COMPRA CARTAO MAESTRO              20/03 MADERO CIDADE S", "docto": "415750", "value": "-41.80"}, {"data": "20-03-2018", "descricao": "COMPRA CARTAO MAESTRO              20/03 LANCHONETE PAMP", "docto": "065050", "value": "-6.50"}, {"data": "19-03-2018", "descricao": "COMPRA CARTAO MAESTRO              19/03 PORTO DA SERRA", "docto": "055650", "value": "-10.00"}, {"data": "19-03-2018", "descricao": "COMPRA CARTAO MAESTRO              19/03 PRODATA MOBILIT", "docto": "435450", "value": "-20.00"}, {"data": "19-03-2018", "descricao": "RESG POUP - SUPERLINHA / INTERNET  DE: 0001.60.044669-6", "docto": "225930", "value": "50.00"}, {"data": "19-03-2018", "descricao": "RESG POUP - SUPERLINHA / INTERNET  DE: 0001.60.044669-6", "docto": "555689", "value": "20.00"}, {"data": "19-03-2018", "descricao": "SAQUE NO BANCO 24 HORAS", "docto": "211322", "value": "-20.00"}, {"data": "19-03-2018", "descricao": "COMPRA CARTAO MAESTRO              17/03 LANCHONETE GAND", "docto": "121150", "value": "-10.60"}, {"data": "16-03-2018", "descricao": "COMPRA CARTAO MAESTRO              16/03 PERA MACA SUCOS", "docto": "353650", "value": "-4.00"}, {"data": "16-03-2018", "descricao": "SAQUE NO ATM INTERAGENCIA", "docto": "600248", "value": "-40.00"}, {"data": "16-03-2018", "descricao": "TRANSF DE CONTA POUPANCA PARA C/C  DE: 0001.60.044669-6", "docto": "251048", "value": "80.00"}, {"data": "16-03-2018", "descricao": "SAQUE NO ATM INTERAGENCIA", "docto": "600248", "value": "-40.00"}, {"data": "16-03-2018", "descricao": "COMPRA CARTAO MAESTRO              16/03 PERTO", "docto": "354450", "value": "-21.00"}, {"data": "16-03-2018", "descricao": "TED MESMA TITULARIDADE STR         102-0002-000000039370", "docto": "324000", "value": "-110.00"}, {"data": "15-03-2018", "descricao": "RESG POUP - SUPERLINHA / INTERNET  DE: 0001.60.044669-6", "docto": "105097", "value": "170.00"}, {"data": "14-03-2018", "descricao": "COMPRA CARTAO MAESTRO              14/03 MULLEQUINHO.S", "docto": "531650", "value": "-9.00"}, {"data": "14-03-2018", "descricao": "COMPRA CARTAO MAESTRO              14/03 MULLEQUINHO.S", "docto": "525450", "value": "-42.00"}], "invest": "1758.80"}
	# extFirebase = db.child("extract") #.get().val()
	# if extFirebase:
	saldo = extract.get('saldo')
	invest = extract.get('invest')
	if saldo and extract:
		# extract = FirebaseDict(extFirebase.val())
		# extract.prepend('saldo', saldo)
		# extract.prepend('invest', invest)
		db.child("extract").update({'saldo': saldo})
		db.child("extract").update({'invest': invest})
	
	for launchSant in extract.get('transactions'):
		trans = db.child("extract").child('transactions').get().val()
		if not trans or not launchSant in trans.values():
			db.child("extract").child('transactions').push(launchSant)


class FirebaseDict(OrderedDict):

    def prepend(self, key, value, dict_setitem=dict.__setitem__):
		# 'Store items in the order the keys were last added'
        root = self._OrderedDict__root
        first = root[1]

        if key in self:
            link = self._OrderedDict__map[key]
            link_prev, link_next, _ = link
            link_prev[1] = link_next
            link_next[0] = link_prev
            link[0] = root
            link[1] = first
            root[1] = first[0] = link
        else:
            root[1] = first[0] = self._OrderedDict__map[key] = [root, first, key]
            dict_setitem(self, key, value)

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)