""" 
FUNÇÕES SPLIT, JOIN E ENUMERATE
* Split - dividir uma string # str 
* Join - juntar uma lista # str 
* Enumerate - Enumerar elementos de uma lista # list

funções aprendidas: 
.count() - conta quantas vezes houve uma ocorrencia
.strip() - remove o espaço do inicio e do fim de uma string
.capitalize() - deixa a primeira letra da frase maiuscula
"""

# Split - dividindo strings
string="O Brasil é o pais do futebol, o Brasil é penta"
lista_1= string.split(' ') # a divisão da string sera o espaço, no caso cada palavra sera um valor diferente na lista_1
lista_2= string.split(',') # a divisão da string sera a ',' no caso a lista_2 tera como valor as 2 frases separadas por ,

# .count() - contando quantas vezes cada palavra apareceu na frase da lista_1
for valor in lista_1:
    print(f'a palavra {valor} apareceu "{lista_1.count(valor)}"x na frase')

# .strip(), .capitalize() - removendo o espaço do inicio e do valor [1] da lista_2, deixando a primeira letra maiuscula
for valor in lista_2:
    print(valor.strip().capitalize())

# Join - transformar uma lista em uma string
string1="O Brasil é penta" # aqui criamos a string
lista= string1.split(' ') # aqui separamos cada valor dividido pelo espaço em uma lista
string2= ' '.join(lista) # aqui criamos uma string identica a original da lista (string1) que junta todos valores da lista dividindo cada um por espaço

print(string1)
print(lista)
print(string2)

# Enumerate - enumera elementos de uma lista, no caso retorna o indice e valor de uma respectiva lista
print("")
for indice, valor in enumerate(lista):
    print(f'indice: {indice}, valor: {valor}') 