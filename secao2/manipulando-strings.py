"""
-- MANIPULANDO STRINGS --
* indices das strings
* fatiamento de strings [inicio:fim:passo]
* funções built-in len, abs, type, print...
Essas funções podem ser usadas diretamente em cada tipo

"""
# EXEMPLOS DE INDICE
#positivos  [012345678]
texto=      'Python s2'
#negativos -[987654321]
print(texto[1]) #dessa forma acessamos o elemento de indice 1 da variavel (o caractere 'y')
print(texto[-1]) #dessa forma acessamos o elemento de indice -1 da variavel (o caractere '2')

# EXEMPLOS DE FATIAMENTO
print(texto[0:6]) # imprime a palavra Python
print(texto[-3:]) # imprime a palavra s2
print(texto[0:8:2]) # [inicio:fim:passo]