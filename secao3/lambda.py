"""
EXPRESSÕES LAMBDA
(FUNÇÃO ANONIMA)

funções aprendidas:
.sort() - ordena uma lista 
- a lambda nao precisa de return, ela sempre retorna o resultado! 
"""
# exemplo:
x = lambda x, y: x * y 
print(x(2,2))

lista=[
    ['P1',6],
    ['P2',61],
    ['P3',16],
    ['P4',90],
    ['P5',8],
]
print(sorted(lista, key=lambda i:i[1])) # ordenando a lista em ordem crescente do int