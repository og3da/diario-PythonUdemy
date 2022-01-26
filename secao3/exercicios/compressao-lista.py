"""
O EXERCICIO É RETORNAR OS VALORES DA VARIAVEL STRING SEPARADOS E DEPOIS DIVIDIDOS POR '.'
"""
from re import L


string='01234567890123456789012345678901234567890123456789'
# é necessário fazer o fatiamento da string
n=10
lista=[string[i:i + n] for i in range(0, len(string), n)]
retorno= '.'.join(lista)
print(lista)
print(retorno)