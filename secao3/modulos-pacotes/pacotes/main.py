import vendas.calcPreco
import vendas.formata
...
from vendas.calcPreco import aumento 
from vendas.formata.preco import real as formata 

# utilizando o pacote vendas, arquivo calcPreco
preco=50
preco_aumentado= vendas.calcPreco.aumento(valor=preco, percentual=10) 
print(preco_aumentado)

# utilizando o pacote vendas>formata, arquivo preco função real
preco=60 
print(vendas.formata.preco.real(preco))
...
print(formata(preco))