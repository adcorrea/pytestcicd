from .produto import Produto

class Estoque:
    def __init__(self) -> None:
        self.produtos = {}


    def adicionar_produto(self, produto):
        if not isinstance(produto, Produto):
            raise TypeError('Classe não é Produto')
        
        if produto.nome not in self.produtos:
            self.produtos[produto.nome] = produto.quantidade
        else:
            self.produtos[produto.nome] += produto.quantidade


    def verifica_quantidade(self, nome_produto):
        return self.produtos.get(nome_produto, 0)



    