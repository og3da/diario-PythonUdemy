"""
FUNÇÃO UTILIZADA PARA REDUZIR A UM UNICO VALOR 
- no exemplo abaixo vamos utilizar a função para somar a idade de todas pessoas, logo em seguida fazendo a media
"""
from dados import * # importando informações do arquivo 'dados'
from functools import reduce # para utilizar a função reduce

soma_idade = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print("media de idade: ",soma_idade / len(pessoas))