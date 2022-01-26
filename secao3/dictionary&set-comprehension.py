"""
DICTIONARY COMPREHENSION É UMA FORMA COMPRIMIDA DE ESCREVER UMA LISTA
- sua diferença com a lista é que
"""
# aqui estamos usando comprehension de dicionario referente a lista
lista=[
    ('chave','valor'),
    ('chave2','valor2'),
]

# dicionario comprehension 
ex1={x: y for x, y in lista}
print(ex1)

# set
ex2={x for x in range(5)}
print(ex2)