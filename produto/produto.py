class Produto():
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def exibirdetails(self):
        print(f"Produto: {self.nome} Preço: {self.preco} Estoque: {self.estoque} unidades.")