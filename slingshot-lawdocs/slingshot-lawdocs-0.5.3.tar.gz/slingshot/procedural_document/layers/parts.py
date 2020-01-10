from .base import *

class Author(Part):

    """
    This layer introduces the author of the procedural_document and creates the text where it states the who the author is
    On Brazil, the author must have a CPF (SSN-like), profession, address and name.
    We inherit from the Part layer and introduce some more attributes and methods.

    The create parraf create th author declaring statement 
    The _add method introduces them on the right places of the procedural_document
    """
    def __init__(self, name, address, cpf, profession):
        super(Author, self).__init__(name, address)
        self.layer_type = "Autor"
        self.CPF = cpf
        self.profession = profession
        self.priority = 1000000000
        self.create_parraf()
    
    def create_parraf(self):
        base = "{}, {}, domiciliado em {}, sob o CPF {} vem diante da Vossa Exa. ajuizar"
        base = base.format(self.name, self.profession, self.address, self.CPF)
        self.parraf.append(base)


    def _add(self):
        self.procedural_document.author.extend(self.parraf)
        self.procedural_document.author_name = self.name

class CounterPart(Part):
    """
    This layer introduces the counterpart of the procedural_document and creates the text where it states the who the counterpart is
    On Brazil, the author must have a CNPJ (register number-like), profession, address and name.
    We inherit from the Part layer and introduce some more attributes and methods.

    The create parraf create the counterpart declaring statement 
    The _add method introduces them on the right places of the procedural_document
    """
    
    def __init__(self, name, address, cnpj):
        super(CounterPart, self).__init__(name, address)
        self.layer_type = "Parte Re"
        self.CNPJ = cnpj
        self.priority = 1000000000 - 1
        self.create_parraf()
    
    def create_parraf(self):
        base = """Em face de {}, com sede em {}, sob o CNPJ {}, pelas razoes de fato e Direito aqui expostas:"""
        base = base.format(self.name, self.address, self.CNPJ)
        self.parraf.append(base)

    def _add(self):
        self.procedural_document.counter_part.extend(self.parraf)


#AS MAIS IMPORTANTES TELES
#SE VC VAI COMEÇAR A AUTOMATIZAR PROCESSO, CERTAMENTE VAI PASSAR POR AQUI

TIM_SP_re = CounterPart(name = "TIM Celular S/A",
                     cnpj = "04.206.050/0001-80",
                     address = "Av Giovanni Gronchi, 7143, São Paulo - SP, CEP: 05724-003")

Claro_SP_re = CounterPart(name = "Claro S/A",
                     cnpj = "40.432.544/0001-47",
                     address = "Rua Henri Durant, 780, Santo Amaro, Sao Paulo - SP, CEP: 04709-110")

Vivo_SP_re = CounterPart(name = "Telefonica Brasil S/A (Vivo)",
                     cnpj = "02.558.157/0001-62",
                     address = "Av. Engenheiro Luiz Carlos Berrini, 1376, São Paulo -SP, CEP: 04571-936")

Oi_SP_re = CounterPart(name = "Oi Móvel S/A – em recuperação judicial",
                     cnpj = "05.423.963/0026-70",
                     address = "Rua Arquiteto Olavo Redig de Campos, 105 Torre A - 15º andar - Chácara Santo Antônio, São Paulo / SP - CEP: 04711-904")

Nextel_SP_re = CounterPart(name = "NEXTEL TELECOMUNICAÇÕES S/A",
                     cnpj = "66.970.229/0001-67",
                     address = "Avenida das Nações Unidas, nº 14.171, 32º andar - Condomínio Rochaverá Corporate Towers - Crystal TowerVila Gertrudes, São Paulo -SP, CEP 04794-000")                