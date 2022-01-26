"""
LIST COMPREHENSION É UMA FORMA COMPRIMIDA DE ESCREVER UMA LISTA
"""

lista=[1,2,3,4,5,6,7,8,9,10]
ex1=[variavel for variavel in lista] # aqui estamos iterando em cada elemento de 'lista' e passando para 'ex1' em uma unica linha
print(ex1)

# multiplicando cada valor da lista por 2
ex2=[v * 2 for v in lista]
print(ex2)

# usando 2 variaveis, printando sequencia
ex3=[(v1, v2) for v1 in lista for v2 in range(3)]
print(ex3)

# trocando 'a' por '@'
lista2=['Luiz','Josefa','Paulo']
ex4=[v.replace('a','@') for v in lista2]
print(ex4)

# trocando as variaveis
tupla=(
    ('chave','valor'),
    ('chave1','valor1'),
)
ex5= [(y, x) for x, y in tupla]
ex5= dict(ex5)
print(ex5)

# criando lista de 0 a 99 e impondo condições
lista3=list(range(100))
ex6=[ v for v in lista3 if v % 3 == 0 if v % 8 == 0 ]
print(ex6)

# condições com else
ex7=[v if v % 3 == 0 else 'nao é' for v in lista3]
print(ex7)