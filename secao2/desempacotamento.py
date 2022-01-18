""" 
Desempacotamento de listas em python
"""
lista= ['joao','maria','jose',1,2,3,4,5,6,7,8,100]
# n1,n2,n3=lista

# contendo mais valores na lista que nao irao ser usados podemos criar uma terceira variavel antecedida de * para representar o resto 
n1,n2,n3, *outros_valores, ultimo_lista =lista

print(n2) # printa maria - lista[1]
print(outros_valores) # printa a lista criada para nao haver erros ao desempacotar. outros_valores
print(ultimo_lista) # printa o ultimo valor da lista criado nas variaveis apos a lista com *