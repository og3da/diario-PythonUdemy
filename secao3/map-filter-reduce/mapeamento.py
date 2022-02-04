"""
FUNÇÃO MAP
- recebe uma função como primeiro argumento 
- .map() aplica uma função para cada item de um iteravel 
"""
from dados import * # importando informações do arquivo 'dados'

# multiplicando cada valor da lista por 2 para exemplo da função map()
nova_lista = map(lambda x: x * 2, lista) # usando list comprehensions: nova_lista = [x * 2 for x in lista]
print(lista)
print(list(nova_lista))

# pegando o preço de cada produto  
def aumenta_preco(p):
    p['preço'] = round(p['preço'] * 1.05, 2) # aumentando 5% do valor
    return p 

novos_produtos = map(aumenta_preco, produtos)
for produto in novos_produtos:
    print(produto)

# pegando o nome de cada pessoa
nova_pessoas = map(lambda p: p['nome'], pessoas)
for pessoa in nova_pessoas:
    print(pessoa)