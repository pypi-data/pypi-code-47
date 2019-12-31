class sub:
    '''
                      --------------------
                       Ni test lib
    '''
    def __init__(self,pr,bud):
        self.cap='Ni'
        self.name='noey'
        self.price= pr
        self.k=0
        self.bu=bud
        self.to=0

    def miss(self):
        print('we are love')

    def cal(self):
        per=self.price *(10/100)
        print('price :{} Bath'.format(per))

    def goto(self,en,dis):
        print(f"let go: {en} Distance: {dis}")
        self.k=self.k+dis

    def fu(self):
        d= 20
        cal_f=d*self.k
        print('cost:{:,d}'.format(cal_f))
        self.to+=cal_f
        
    @property

    def bur(self):
        re=self.bu-self.to
        print('Budjest:{:,d} Bath'.format(re))
        return re
        
class ele(sub):
    def __init__(self,pr,bud):
        self.sub_n= 'Test'
        self.bat_d=1000000
        super().__init__(pr,bud)
    def bat(self):
        alls=100
        cal=(self.k*1000)/self.bat_d
        print('we have batt: {}'.format(alls-cal))

    def fu(self):
        d= 5
        cal_f=d*self.k
        print('cost:{:,d}'.format(cal_f))
        self.to+=cal_f
        
if __name__ == '__main__':
    te=ele(4000,500000)
    print(te.cap)     
    print(te.bu)
    te.goto('Japan',10000)
    te.fu()
    te.bat()
    print(te.bur)
print('---------------------------')
'''#kong=sub(500)
#kong2=sub(70000)
#kong.cal()
#########################################
print('---------------------------')
kong2.cal()
kong2.cap='Jam'
#print(kong2.cap)
kong2.goto('china',500)
#print(kong2.k)
kong2.fu()
a=kong2.bur
print('Curren :{}'.format(a*0.2))'''

        
