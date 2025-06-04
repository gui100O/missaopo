from funcionario import FuncionarioCLT, FuncionarioPJ
from produto import ProdutoNac, ProdutoImportado

def cadastrar_produtos():
    produtos = []
    produtos.append(ProdutoNac("Notebook", 3000, 10))
    produtos.append(ProdutoImportado("Celular", 2500, 5, 0.2))
    produtos.append(ProdutoNac("Cadeira", 500, 20))
    produtos.append(ProdutoImportado("Tablet", 1500, 8, 0.15))
    return produtos

def exibir_produtos(produtos):
    print("\n--- Produtos Cadastrados ---")
    for p in produtos:
        p.exibirdetails()
        print(f"Preço final: R$ {p.preco_final():.2f}")
        p.emitir_nota()
        print()

def calcular_pagamentos():
    funcionarios = [
        FuncionarioCLT("Carlos", 3000),
        FuncionarioPJ("Ana", 160, 25)
    ]
    print("\n--- Pagamento dos Funcionários ---")
    for f in funcionarios:
        print(f"{f.nome}: R$ {f.calcular_pagamento():.2f}")

def simular_venda(produtos):
    print("\n--- Simulação de Venda ---")
    produto = produtos[0]
    print(f"Vendendo 1 unidade de: {produto.nome}")
    produto.vender(1)

def simular_reposicao(produtos):
    print("\n--- Simulação de Reposição ---")
    produto = produtos[1]
    print(f"Repondo 5 unidades de: {produto.nome}")
    produto.repor(5)

if __name__ == "__main__":
    produtos = cadastrar_produtos()
    exibir_produtos(produtos)
    calcular_pagamentos()
    simular_venda(produtos)
    simular_reposicao(produtos)
