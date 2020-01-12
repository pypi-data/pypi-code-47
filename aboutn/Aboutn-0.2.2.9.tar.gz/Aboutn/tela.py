HEXADECIMAL = '0123456789ABCDEF'
FUNDO	= "bg"
TEXTO	= "fg"
VERMELHO='RED'; 	VER	= {FUNDO:VERMELHO,TEXTO:VERMELHO}
BRANCO	= 'WHITE'; 	BRA	= {FUNDO: BRANCO, TEXTO:BRANCO}
PRETO	= 'BLACK'; 	PRE	= {FUNDO: PRETO, TEXTO: PRETO}
CORES	= {VERMELHO:"vermelho",BRANCO:"branco",PRETO:"preto"}


#	diferença entre x,y da coisa relativa e do objeto de origem (ex: player relativo ao bot)
	#		(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(2,0),(2,2),(0,2),(-2,2),(-2,0),(-2,-2),(0,-2),(2,-2), (2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1), (-1, -2), (1, -2)
sentidos = [(1,0),(1,1),(0,1),(-1,1)]
for i in (-1,2):
	j,k = 0,len(sentidos)
	while j < k:
		sentidos.append((sentidos[j][0]*i,sentidos[j][1]*i))
		#print(sentidos[len(sentidos)-1])
		j += 1
#k = 1
#for i in range(len(sentidos)//2,len(sentidos)):
#	if 0 in sentidos[i]:
#		for j in range(2):#"''":
#			j = list(sentidos[i])
#			k = -k
		#	k *= -1
#			j[j.index(0)] = k
#			sentidos.append(tuple(j))
i,j = 1,2
z = '"'*2#range(2)
for x in z:
	for y in z:
		sentidos.append((i,j))
		sentidos.append((j,i))
		i = -i
	j = -j

sentidos= tuple(sentidos)		
mx,my	=	32,16
qx,qy	=	mx//2, my//2
d_max	= ((mx-1)**2 + (my-1)**2)**(1/2)
#teto = mx,my
#quad 	= [qx,qy]
#vence 	= [0,0]
#qtd 	= 2

try:
	from tkinter import BOTH, RIGHT, LEFT, Tk, Frame, Button, Label, EventType#.KeyRelease
	from threading import Thread
	from time import sleep, time
	from random import random
except ImportError as ie:
	print("\a\tTkinter requerida para execução gráfica: ",ie)
else:
	print("\n\tImportações sem nenhum problema, por enquanto....\n")
try:
	from quadro import Quadro
except ImportError:
	from Aboutn.quadro import Quadro#, quadrado


'''
 #	aptidão
def avaliar (d,g=None): 
	global quad
	if g == None:
		global d_max
		global f_max
		return f_max*(1-(d/d_max))
	return avaliar(((d-quad[0])**2 + (g-quad[1])**2)**(1/2))

c = d_max
while c >= 0:
	print(c,avaliar(c))
	c -= 1
c = 0
while c <= d_max:
	print(c,avaliar(c))
	c += 1

def gerar ():
	return [int(mx*random()),int(my*random())]


def andar (*coord):
	quadrados[quad[1]][quad[0]].config(**BRA)
	c = 0
	try:
		while len(coord)>c:
			if teto[c] > coord[c] and coord[c] >= 0:
				quad[c] = coord[c]
			c += 1
	except Exception:
		pass
	quadrados[quad[1]][quad[0]].config(**VER)
'''

def xadrez (mestre, c=8,h=None,espera=0,matriz=[],ligue=False,*ligargs):
	try:
		mestre = Frame(mestre)
		mestre.pack(fill=BOTH)
		t = time()
		if (h==None):
			h = c
		y = h
		while y>0:
			x = c
			m = Frame(mestre)
			m.pack(fill=BOTH)
			matriz.insert(0,[])
			while x>0:
			#	l = Frame(m,width=mestre.winfo_screenwidth()//n,height=mestre.winfo_screenheight()//n)
			#	l.pack()
				matriz[0].insert(0,Button(m,text=(x,y)))
				matriz[0][0].pack(fill=BOTH, side=RIGHT)
				matriz[0][0].coord = x-1,y-1
			#	matriz[0][0].ir = lambda col=x-1,lin=y-1: funcao(col,lin)#matriz[lin][col].config(**VER)#print(pos)
				#print(x,y)
				sleep(espera/(x*y))
				x -= 1
			y -= 1
	except Exception:
		return print('Construção abortada')

	if ligue:
		t = time() - t
		mestre.master.title("About n []")
		print('Espera máxima:\t%f\nTempo total:\t%f\nTempo médio:\t%f\nTotal:\t%d botões\n'%(espera,t,t/(h*c),c*h))
		ativar(matriz,*ligargs)
	return matriz

def iniciar (mestre, x=16,y=None,*imolados,tempo=1/13,botoes=[],inicio=lambda: print('\t\aFunção para ativação não fornecida'),comando=lambda para: print('\tMétodo para pressão não fornecido',*para),fechar=lambda: print('\t\aFunção para finalização não fornecida')):
	for i in imolados:
		try:
			i.destroy()
		except Exception:
			print('\t\aNão foi possível destruir o elemento',i)
	Thread(None, xadrez, "Breve-montagem-ambiental", (mestre,x,y,tempo,botoes,True,comando,inicio)).start()
	print('Tupla de objetos destruídos:',imolados)
	mestre.protocol("WM_DELETE_WINDOW", fechar)
	mestre.bind("<End>", fechar)
	mestre.title('About n')
	

def ativar (tabuleiro,pressionar=None,principiar=input,cdif=0):
	try:
		for l in tabuleiro:
			for c in l:
				if c[FUNDO] != PRETO:
					cdif += 1
					#print(cdif,c['text'])
				if pressionar:
					c.config(command=lambda to=c.coord: pressionar(para=to))#c.ir)#lambda pos=c.coord: print(pos))
				c.config(**BRA)
			c.master.config(bg=BRANCO)
		c.master.master.config(bg=BRANCO)
		c.master.master.master.config(bg=BRANCO)
		c.master.master.master.title ('About n [Squares]')
	#	c.master.master.master.protocol("WM_DELETE_WINDOW", DISABLED)
	except Exception:
		print('\t\aUm erro ocorreu na construção da tela branca, no caso de permanência do cinza claro padrão em algum elemento, por favor, repita esta operação.')
	principiar()
	return cdif
"""	cuidar()

def cuidar (b=None,bots=[]):
	global vence
	global quad
	global qtd
	global BRA
	global PRE
	global PRETO
	global BRANCO

	if b != None:
		while len(bots) > 0 and not quad in bots:
			quadrados[b[1]][b[0]].config(**BRA)
			dv = sentidos[int(random()*len(sentidos))]
			c = len(b)
			while c > 0:
				c	+= -1
				b[c]+= dv[c]
				if b[c] < 0:
					b[c] = 0
				if b[c] >= teto[c]:
					b[c] = teto[c] - 1
			quadrados[b[1]][b[0]].config(**PRE)
			print(b,avaliar(*b))
			if b != quad:
				sleep((11/12)-(random()/8))
			if b == quad:
				print('\a\t',b)
				bots.clear()
				qtd += 1#= len(bots) + 1
				vence,quad = b,[mx//2,my//2]
				sleep((12/11)+(random()/4))
				ativar(quadrados)
				return
		quadrados[b[1]][b[0]].config(**BRA)
		BRANCO,BRA,PRE,PRETO = PRETO,PRE,BRA,BRANCO
		return
	
	b = vence
	c = qtd
	while c>0:	
		if b != quad:
			bots.append(b)
		b = gerar()
		c -= 1
	if len(bots) < 2:
		b = bots
		cuidar(bots=b)
		print("Ação de emergência utilizada")
	else:
		print(len(bots),bots)
	for b in bots:
		Thread(None, lambda: cuidar(b,bots)).start()
	
a = Tk()
#a.config(bg='WHITE')
a.title("About 2") #a História de n Quadrados
#a.attributes('-fullscreen', True)
#a.geometry('%dx%d' %(a.winfo_screenwidth()//2, a.winfo_screenheight()//2))
#b = {'width':a.winfo_screenwidth()//9,'height':a.winfo_screenheight()//8,'master':a}
#b = Frame(**b),Frame(**b)
b = [Label(a,text="\n\n")]
b.extend((Button(a,command=lambda destruir=b: iniciar(a,mx,my,*destruir,botoes=quadrados),**VER,text=VERMELHO), Button(a,command=a.quit,bg=PRETO,text="n")))
b[1].pack(side=RIGHT)
b[2].pack()
b[0].pack()
b = '0123456789ABCDEF'
c = 0
while c < len(sentidos):
	for d in (b[c]*2).title():
		a.bind(d,lambda event,x=sentidos[c][0],y=sentidos[c][1]: andar(quad[0]+x,quad[1]+y))
	c += 1
#Thread(None, xadrez, None, (a,)).start()
#Thread(None, ).start()
a.mainloop()
"""

class Tela:

	x = q = n = d = b = a = correr = tela = None
	def __gt__ (self, o):
		try:
			return (self.q > o.q or (self.q == o.q and self.n > o.n))
		except Exception:
			return NotImplemented
	def __lt__ (self, o):
		try:
			return (self.q < o.q or (self.q == o.q and self.n < o.n))
		except Exception:
			return NotImplemented
	def __le__ (self, o):
		return type(o) == Tela and not self.__gt__(o)
	def __ge__ (self, o):
		return type(o) == Tela and not self.__lt__(o)
	def __ne__ (self, o):
		return not (self.__ge__(o) and self.__le__(o))
	def __eq__ (self, o):
		return not self.__ne__(o)
	def __repr__ (self):
		return self.__str__()
	def __str__ (self):
		res = 'Tela(%s,%s)' %(self.q.__repr__(),self.n.__repr__())
		if __name__ != '__main__':
			res = 'tela.%s' %res
		return res

	def __init__ (self, vermelho=None, quadrados=None):
		if type(vermelho) == Tela:
			if quadrados == None:
				quadrados =	vermelho.n
			vermelho	=	vermelho.q#protagonista()
		if type(quadrados) == Quadro:
			quadrados.mestra(self)
		elif type(quadrados) in (tuple,list,set):
			quadrados = Quadro(self,quadrados)
		else:
			quadrados = Quadro(self)
		self.n = quadrados
		self.protagonista(vermelho)

	def quit (self,event=0):
		if self.correr:
			self.reiniciar()
		elif self.a or self.x != False:
			self.tela.quit()

	def alt (self,event=0):
		if not self.correr:
			try:
				self.a = event.type == EventType.KeyPress
				print(self.a,event,type(event.type))
			except AttributeError:
				return

	def run (self, v = True):
		self.correr = v

	def protagonista (self,principal=None):
		if principal == None:
			return self.q
		self.q = principal
		if self != principal.s:
			self.q.mestra(self,VER)
	#	self.q.ir(para=(mx//2,my//2))

	def colorir (self,x,y,cor=BRA):
		try:
			self.b[y][x].config(**cor)
			return True
		except IndexError:
			#print('Posição [',x,y,'] inválida')
			return False
		except:
			#print('Erro em configurar o botão [',x,y,'] de', self.b)
			return 
	
	def iniciar (self,tela=None,quadrados=[],x=None):
		if None == x:
			x = self.x
		else:
			self.x = x
		if self.tela == None:
			if tela == None:
				tela = Tk()
			self.tela = tela
		self.tela.title('About 2')
		self.tela.protocol("WM_DELETE_WINDOW",self.quit)
		self.tela.bind('<End>',self.quit)
		self.run(False)
		self.b = quadrados
		b = [Label(tela,text='\n\n',bg=self.tela[FUNDO])]
		#print(b)
		b.append(Button(tela,command=lambda destruir=b: iniciar(self.tela,mx,my,*destruir,botoes=self.b,comando=self.q.ir,inicio=self.n.iniciar,fechar=self.reiniciar),**VER,text=VERMELHO))
		b.append(Button(tela,command=self.n.reiniciar,bg=PRETO,text='n'))
		b[1].pack(side=RIGHT)
		b[2].pack()
		b[0].pack()
		b = HEXADECIMAL
		c = len(b)#sentidos) - 1
		tela.bind('<Escape>', self.reiniciar)
		tela.bind('<KeyRelease-Alt_L>', self.alt)
		tela.bind('<Alt_L>', self.alt)
		while c > 0:
			c += -1
			for d in (b[c]*2).title():
				tela.bind(d,lambda event,to=sentidos[c]: self.q.ir(*to))
		tela.mainloop()

	def reiniciar (self,event=0):
		try:
			self.n.pausar()
			self.b.pop(0).pop(0).master.master.destroy()
			self.b.clear()
			self.iniciar()
		except Exception:
			return
			#print(self,'incapaz de reiniciar neste momento, tente novamente mais tarde.')

	def continuar (self,geracao=None):
		if self.d:
			global BRANCO, PRETO
			BRANCO, PRETO = PRETO, BRANCO
			BRA[FUNDO],BRA[TEXTO],PRE[TEXTO],PRE[FUNDO] = PRE[FUNDO],PRE[TEXTO],BRA[TEXTO],BRA[FUNDO]
			
		self.d = ativar(self.b,principiar=self.n.iniciar)%2 == 1