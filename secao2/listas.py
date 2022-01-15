"""
LISTAS EM PYTHON
fatiamento
funções: append, insert, pop, del, clear, extend...
min, max
range
"""
"""
palavra='arroba'
#          0        1   2   3   4
alfabeto=['arroba','b','c','d','e']

# a diferença entre uma lista e uma variavel é que a lista pode conter varios valores individuais a variavel apenas um
print(palavra[0])
print(alfabeto[0])

# podemos exibir todos elementos da lista da seguinte forma
print(alfabeto) #exibindo a lista
print(alfabeto[::-1]) #exibindo ao contrario
print(alfabeto[1::]) #exibindo a partir do indice 1 ate o final
print(alfabeto[1:4]) #exibindo apenas do 1-3
print(alfabeto[::2]) #exibindo de 2 em 2 elementos (passo 2)

"""
# manipulando listas
l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2 # concatenando listas l1+l2=l3
l4=['mao','pe']
l1.extend(l2) # l1 recebe valores de l2 (extende l2)
print(l4)
l4.append('braço') #insere na ultima posição o valor
print(l4)
l4.insert(0,'perna') #insere no indice 0 o valor
print(l4)
l4.pop() #apaga ultimo item da lista
print(l4)
del(l4[0]) #apaga indice desejado
print(l4)
del(l4[0:2]) #apagando indices desejado
print(l4)

# criando uma lista de 1-10 de forma facil
listaFacil= list(range(1,11))
print(listaFacil)