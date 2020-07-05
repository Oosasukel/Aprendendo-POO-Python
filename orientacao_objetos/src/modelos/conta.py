from src.modelos.usuario import Usuario


class Conta:
    def __init__(self, agencia: str, numero: str, usuario: Usuario):
        self.agencia = agencia
        self.numero = numero
        self.titular = usuario
        self.saldo = 0

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo = self.saldo + valor
            print(f'depositando {valor} reais.')
        else:
            if valor == 0:
                print('nao é possivel depositar valor 0')
            else:
                print('nao eh possivel depositar valores negativos')

    def sacar(self, valor: float):
        if valor > 0:
            #valor positivo aqui
            if valor <= self.saldo:
                self.saldo = self.saldo - valor
                print(f'sacando {valor} reais.')
            else:
                print('saldo insuficiente')

        else:
            #valor negativo ou 0 aqui

            if valor == 0:
                print('nao eh possivel sacar 0')
            else:
                print('nao da pra sacar valor negativo')



    def transferir(self, outra_conta, valor: float):
        if valor > 0:
            if valor <= self.saldo:
                self.sacar(valor)
                outra_conta.depositar(valor)
            else:
                print('nao tem saldo suficiente')
        else:

            if valor == 0:
                print('nao é possivel transferir valor 0')
            else:
                print('nao eh possivel transferir valores negativos')
