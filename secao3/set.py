"""
SETS EM PYTHON (COLEÇÕES)
- o diferencial do set é que cada elemento neste é único, nao permitindo duplicidade
- criamos um set utilizando {} chaves 

funções de um SET 
.add() - adiciona um elemento
.update() - atualiza um elemento

.union() - une 2 sets ( utilizamos .union() ou | )
.intersection() - retorna todos elementos presentes nos 2 sets ( intersecção, utilizamos & )
.difference() - retorna a diferença apenas dos elementos do set a esquerda ( utilizamos - )
.symettric_difference() - retorna elementos diferentes em ambos sets ( utilizamos ^ )
"""
# no exemplo abaixo ao printar o set ele exibe o int '1' apenas 1x
set1 = {1,1,2,3,5}
print("set1: ",set1)

# adicionar elemento
set1.add('Python')
print(set1)

# .update(), esta itera cada caractere no set (em ordem aleatoria)
set1.update('Python')
print(set1)

# .union(), unindo 2 sets
set2 = {1,2,3,4}
print("set2: ",set2)
set3 = set1 | set2 
...
set3 = set1.union(set2)
print(set3)

# .intersection(), apresenta a intersecção dos sets 
set3 = set1 & set2
print("intersecção set1 & set2: ",set3)

# .difference(), apresenta diferença dos elementos do set a esquerda
set3 = set1 - set2
print("elementos diferentes no set1: ",set3)
...
set3 = set2 - set1 
print("elementos diferentes no set2: ",set3)

# .symettric_difference(), apresenta apenas os elementos diferentes em cada set 
set3 = set1 ^ set2
print("elementos diferentes em ambos set: ",set3)