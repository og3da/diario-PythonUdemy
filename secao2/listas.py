"""
LISTAS EM PYTHON
fatiamento
funções: append, insert, pop, del, clear, extend...
min, max
range
"""
palavra='arroba'
#          0   1   2   3   4
alfabeto=['a','b','c','d','e']

# a diferença entre uma lista e uma variavel é que a lista pode conter varios valores individuais a variavel apenas um
print(palavra[0])
print(alfabeto[0])

# podemos exibir todos elementos da lista da seguinte forma
print(alfabeto) #exibindo a lista
print(alfabeto[::-1]) #exibindo ao contrario
print(alfabeto[1::]) #exibindo a partir do indice 1 ate o final
print(alfabeto[1:4]) #exibindo apenas do 1-3
print(alfabeto[::2]) #exibindo de 2 em 2 elementos (passo 2)
