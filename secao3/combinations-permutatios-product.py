"""
COMBINATIONS, PERMUTATIONS E PRODUCT - ITERTOOLS
Combinação - ordem nao importa  
Permutação - ordem importa
Ambos nao repetem valores unicos
Produto - ordem importa e repete valores unicos
"""
from itertools import *

pessoas = ['Ogeda','Vitor','Matheus','Gui','Jose','Vilma']
# combinations
print()
for grupo in combinations(pessoas, 2): # aqui estamos apresentando os possiveis grupos de 2 sem importar a ordem 
    print('combinations: ',grupo)

# permutations
print()
for grupo in permutations(pessoas, 2): # aqui estamos apresentando os possiveis grupos de 2 importando a ordem
    print('permutations: ',grupo)

# product
print()
for grupo in product(pessoas, repeat=2): # aqui estamos apresentando os possiveis grupos de 2 importando a ordem e podendo repetir o mesmo valor
    print('product: ',grupo)