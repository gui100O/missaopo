from produto import Produto as ProdutoBase
from produto import ProdutoNac
from produto import ProdutoImportado

print("=== PRODUTO COMUM ===")
produto_comum = ProdutoBase("Caderno", 15.00, 50)
produto_comum.exibirdetails()
print(f"Preço Final: R${produto_comum.preco_final():.2f}")
produto_comum.emitir_nota()
print()

print("=== PRODUTO NACIONAL ===")
produto_nacional = ProdutoNac("Feijão", 7.50, 200)
produto_nacional.exibirdetails()
print(f"Preço Final: R${produto_nacional.preco_final():.2f}")
produto_nacional.emitir_nota()
print()

print("=== PRODUTO IMPORTADO ===")
produto_importado = ProdutoImportado("Notebook Gamer", 5000.00, 10, 0.20)
produto_importado.exibirdetails()
print(f"Preço Final: R${produto_importado.preco_final():.2f}")
produto_importado.emitir_nota()
print()
