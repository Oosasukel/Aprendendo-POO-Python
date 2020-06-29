from src.modelos.endereco import Endereco


class Usuario:
    def __init__(self, nome: str, idade: int, endereco: Endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
