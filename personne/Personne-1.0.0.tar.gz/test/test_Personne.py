import unittest
from test import Personne
class TestPersonne(unittest.TestCase):
    def setUp(self):  #__c'est comme init__ au début de chaque test
        print("Setup")
        self.per1=Personne("Mehalli","Nassim",24)
        self.per2=Personne("Bensidhoum","Ines",23)        
    def tearDown(self): # a la fin de chaque test
        print("Turndown \n")
    def test_ShowEmail(self):
        print("test showmail")
        self.assertEqual(self.per1.showEmail(),"MehalliNassim@outlook.fr")
        self.assertEqual(self.per2.showEmail(),"BensidhoumInes@outlook.fr")
        self.per1.nom="Chebili"
        self.per2.prenom="Smail"
        self.assertEqual(self.per1.showEmail(),"ChebiliNassim@outlook.fr")
        self.assertEqual(self.per2.showEmail(),"BensidhoumSmail@outlook.fr")
    def test_FullName(self):
        print("test_fullname")
        self.assertEqual(self.per1.fullName(),"MehalliNassim")
        self.assertEqual(self.per2.fullName(),"BensidhoumInes")
        self.per1.nom="Chebili"
        self.per2.prenom="Smail"
        self.assertEqual(self.per1.fullName(),"ChebiliNassim")
        self.assertEqual(self.per2.fullName(),"BensidhoumSmail")
        
    def test_setAge(self):
        print("test_set thier age")
        self.per1.setAge()
        self.per2.setAge()
        self.assertEqual(self.per1.age,240)
        self.assertEqual(self.per2.age,230)
if __name__ == "__main__":
    unittest.main()   


