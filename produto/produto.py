class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibirdetails(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque} unidades.")

class Produtonac(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, estoque)

class ProdutoImport(Produto):
    def __init__(self, nome, preco, estoque, taxa_de_import):
        super().__init__(nome, preco, estoque)
        self.taxa_de_import = taxa_de_import

    def exibirdetails(self):
        super().exibirdetails()
        print(f"Taxa de Importação: {self.taxa_de_import * 100:.1f}%")
