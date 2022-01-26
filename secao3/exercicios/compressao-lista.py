"""
O EXERCICIO É RETORNAR OS VALORES DA VARIAVEL STRING SEPARADOS E DEPOIS DIVIDIDOS POR '.'
"""
string='01234567890123456789012345678901234567890123456789'
# é necessário fazer o fatiamento da string
n=10
lista=[string[i:i + n] for i in range(0, len(string), n)]
# separando cada parte da lista por '.'
retorno= '.'.join(lista)
print(lista)
print(retorno)