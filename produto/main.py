from produto import Produto as pop
from produto import Produtonac as pronac
from produto import ProdutoImport as proimp

p = pop("Teclado", 100.0, 20)
p.exibirdetails()
p = proimp("Celular", 2000.0, 5, 0.15)
p.exibirdetails()

