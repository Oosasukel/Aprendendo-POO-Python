from src.modelos.endereco import Endereco
from src.modelos.conta import Conta
from src.modelos.usuario import Usuario

endereco_rodrigo = Endereco('Sao Joao', 'Capela', '28')

rodrigo = Usuario('Rodrigo', 21, endereco_rodrigo)

conta1 = Conta('1516-5', '4022-3', rodrigo)

endereco_carla = Endereco('emilio thome', 'ipero', '255')

carla = Usuario('Carla', 18, endereco_carla)

conta2 = Conta('3446-7', '5566-8', carla)

conta1.depositar(600)
conta1.sacar(200)

print(f'Saldo do {conta1.titular.nome} é {conta1.saldo}')
