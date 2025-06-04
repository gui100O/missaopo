from produto import Produto as ProdutoBase
from produto import ProdutoNac
from produto import ProdutoImportado

print("=== PRODUTO COMUM ===")
produto_comum = ProdutoBase("Caderno", 15.00, 50)

produto_comum.exibirdetails()

print(f"Preço Final: R${produto_comum.preco_final():.2f}")

produto_comum.emitir_nota()

produto_comum.repor(20)   
produto_comum.vender(10)  
produto_comum.vender(100)  
produto_comum.repor(-5)  
produto_comum.vender(-3) 

print(f"Estoque final de {produto_comum.nome}: {produto_comum.estoque}")
print("\n")

print("=== PRODUTO NACIONAL ===")
produto_nacional = ProdutoNac("Feijão", 7.50, 200)

produto_nacional.exibirdetails()
print(f"Preço Final: R${produto_nacional.preco_final():.2f}")
produto_nacional.emitir_nota()

produto_nacional.repor(50)   
produto_nacional.vender(30)  

print(f"Estoque final de {produto_nacional.nome}: {produto_nacional.estoque}")
print("\n")

print("=== PRODUTO IMPORTADO ===")
produto_importado = ProdutoImportado("Notebook Gamer", 5000.00, 10, 0.20)

produto_importado.exibirdetails()
print(f"Preço Final: R${produto_importado.preco_final():.2f}")
produto_importado.emitir_nota()

produto_importado.repor(5) 
produto_importado.vender(3)   

print(f"Estoque final de {produto_importado.nome}: {produto_importado.estoque}")
print()
