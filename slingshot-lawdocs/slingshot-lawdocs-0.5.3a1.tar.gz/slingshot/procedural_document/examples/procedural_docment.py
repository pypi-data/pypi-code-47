from slingshot.procedural_document.layers.models import ContratoServicos, InversaoOnusProva, PropagandaEnganosa
from slingshot.procedural_document.layers.models import CobrancaIndevida, ImpossivelCancelar, DanoMoral, RegistroSerasa
from slingshot.procedural_document.layers.parts import *
from slingshot.procedural_document.core import ProceduralDocument

pet = ProceduralDocument()

pet.add(Author(name="A Mosca",
               profession="nerds bravos com computadores",
               address="Rua da Nossa Casinha, casa 1000",
               cpf="123.456.789-00"))

pet.add(ContratoServicos(service="adesão a plano de celular",
                        docs = ["contas pagas"]))

pet.add(Claro_SP_re)

pet.add(InversaoOnusProva())

pet.add(PropagandaEnganosa(prometido="plano de internet sem corte de dados",
                          real="plano de celular com corte de dados ao fim da franquia",
                          valor=1000,
                          docs="fotos e panfletos da operadora",
                          dano_ocorrido="usar o GPS na volta do trabalho, para não se atrasar para buscar o amigo",
                          deseja_prometido=True))

pet.add(CobrancaIndevida(tarifas_cobradas=["Dados a mais"],
                         valor=2000,
                         docs=["contas"]))

pet.add(RegistroSerasa(divida_registrada="Conta do celular (11) - 99999-8888",
                       valor=2000,
                        docs=["Conta do mês de setembro"]))

pet.add(ImpossivelCancelar(dano_moral=3000,
                           docs=["Pedido de cancelamento e email"]))

pet.add(DanoMoral(2000))