class associations:
	def __init__(self):
		self.__a = []
	def add(self,value,name=None,method=None,case_sensitive=True,regular=False,**data):
		if type(value) != Association:
			if method == None and name == None:
				raise TypeError('add() missing 2 positional arguments: \'method\' and \'name\'');
			if method == None:
				raise TypeError('add() missing 1 positional argument: \'method\'');
			if name == None:
				raise TypeError('add() missing 1 positional argument: \'name\'');
			method = str(method)
			if method not in ['including','in','is']:
				return False;
			name = str(name)
			value = Association(str(value),name,method,case_sensitive,regular,**data)
		else:
			name = value.getname()
			method = value.getmethod()
			regular = value.isregular()
			case_sensitive = value.get_case_sensitive()
		self.__a.append({'value':value.word,'method':method,'regular':regular,'cs':case_sensitive,'assoc':value})
	def get(self,string):
		string=str(string)
		a = []
		for assoc in self.__a:
			if not assoc['cs']:
				assoc['value'] = assoc['value'].lower()
				string = string.lower()
			if assoc['method'] == 'in':
				if assoc['regular']:
					import re
					if re.search(string,assoc['value']):
						a.append(assoc['assoc']);
				else:
					if string in assoc['value']:
						a.append(assoc['assoc']);
			elif assoc['method'] == 'is':
				if assoc['regular']:
					import re
					if re.fullmatch(string,assoc['value']):
						a.append(assoc['assoc']);
				else:
					if string == assoc['value']:
						a.append(assoc['assoc']);
			elif assoc['method'] == 'including':
				if assoc['regular']:
					import re
					if re.search(assoc['value'],string):
						a.append(assoc['assoc']);
				else:
					if assoc['value'] in string:
						a.append(assoc['assoc']);
		return tuple(a);
	def __len__(self):
		return len(self.__a);
	def __dir__(self):
		return ['add','get'];
class Association():
	def __init__(self,word,name,method=None,case_sensitive=True,regular=False,**data):
		self.word = str(word)
		self.__d = data
		self.__m = method
		self.__n = name
		self.__cs = case_sensitive
		self.__r = regular
	def add(self):
		associations.add(self,method=self.__m,case_sensitive=self.__cs,regular=self.__r,**data)
	def getdata(self):
		return self.__d;
	def getmethod(self):
		return self.__m;
	def isregular(self):
		return self.__r;
	def get_case_sensitive(self):
		return self.__cs;
	def set_case_sensitive(self,state):
		self.__cs = bool(state)
	def __dir__(self):
		return ['add','getdata','getmethod','isregular','get_case_sensitive','getname','set_case_sensitive','word'];
	def getname(self):
		return self.__n;
Associations = associations()
del associations;
