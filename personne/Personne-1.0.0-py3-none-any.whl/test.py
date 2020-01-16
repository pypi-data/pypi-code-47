class Personne():
    count=10
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
        
    def showEmail(self):
        return "{}{}@outlook.fr".format(self.nom,self.prenom)
    def fullName(self):
        return "{}{}".format(self.nom,self.prenom)
    def setAge(self):
        self.age=self.age * self.count
