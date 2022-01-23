"""
DICIONARIOS EM PYTHON
- formato de um dicionário
dicionario = {'chave':'valor'} <- as chaves são únicas. 

- suas diferenças com uma lista
- como adicionar, modificar e apagar valores
- como verificar chave/valor
- iterando
- conversão
- concatenar
"""
# criando um dicionário
dicionario={1:100,'nome':'valmax','valor-v':False}
print(dicionario['nome']) 

# adicionando um valor
dicionario['sobrenome'] = 'juniors'
print(dicionario['nome'],dicionario['sobrenome'])
...
dicionario.update({'nova-chave':'novo valor'})

# mudar valor
dicionario['sobrenome'] = 'juniors janeiro'
print(dicionario['nome'],dicionario['sobrenome'])

# apagar valor
del dicionario[1]
print(dicionario)
...
#dicionario.pop(1)

# verificar chave/valor
print('nome' in dicionario)
print('nome' in dicionario.keys())
print('juniors janeiro' in dicionario.values())

# iterando chave/valor e ambos 
for chave in dicionario.keys():
    print(f'chave: {chave}')

for valor in dicionario.values():
    print(f'valor: {valor}')

for chave,valor in dicionario.items():
    print(f'chave: {chave}, valor: {valor}')

# convertendo para dicionario - função dict()
lista = [
    ['c1',1],
    ['c2',5],
    ['c3',10],
]

dicionario1 = dict(lista)
print(dicionario1)

# concatenar
dicionario.update(dicionario1) # concatenando dicionario + dicionario1
print(dicionario) 