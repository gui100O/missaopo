class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibirdetails(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque} unidades.")

    def preco_final(self):
        return self.preco

    def emitir_nota(self):
        print(f"Nota gerada para {self.nome}.")


class ProdutoNac(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, estoque)

    def preco_final(self):
        return self.preco

    def emitir_nota(self):
        print(f"Nota fiscal nacional para {self.nome}.")


class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_de_importacao):
        super().__init__(nome, preco, estoque)
        self.taxa_de_importacao = taxa_de_importacao

    def exibirdetails(self):
        super().exibirdetails()
        print(f"Taxa de Importação: {self.taxa_de_importacao * 100:.1f}%")

    def preco_final(self):
        return self.preco + (self.preco * self.taxa_de_importacao)

    def emitir_nota(self):
        print(f"Nota de importação para {self.nome} com taxa aplicada.")
