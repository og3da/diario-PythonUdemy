"""
FUNÇÃO UTILIZADA PARA FILTRAR 
- no exemplo abaixo vamos utilizar a função para filtrar as listas
"""
from dados import * # importando informações do arquivo 'dados'

# filtrando valores acima de 5 em 'lista'
nova_lista = filter(lambda x: x> 5, lista)
print(list(nova_lista))

# filtrando pessoas acima de 18 anos na lista pessoas
nova_pessoas = filter(lambda i: i['idade'] >= 18, pessoas)
print(list(nova_pessoas))