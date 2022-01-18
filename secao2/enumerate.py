# FUNÇÃO ENUMERATE - enumerar elementos de uma lista # list
# a função enumerate retorna uma tupla com cada lista enumerado

lista= [
#      1        2         3
    ['Oge','Largato','Neguinho'], # indice 0
    ['Guilherme','Lucas','Felipe'], # 1
    ['Jorge','Jose','Matheus']  # 2
]

print('nome: ',lista[1][0]) # indice 0 da lista 1 dentro de 'lista'

print("")
for valor in enumerate(lista): 
    print(valor)