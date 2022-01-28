"""
EXERCÍCIO: FAZER A SOMA DO VALOR DE CADA PRODUTO EM CARRINHO USANDO LIST COMPREHENSIONS
"""
carrinho=[
    ('produto1',10),
    ('produto2',20),
    ('produto3',100),
]
# minha solução
total=[carrinho[i][1] for i in range(len(carrinho))] # carrinho[0][1]+carrinho[1][1]+carrinho[2][1]
soma=[sum(total)]
print("minha solução: ",soma)

# solução do professor
total= sum([float(y) for x,y in carrinho])
print("solução do professor: ",total)