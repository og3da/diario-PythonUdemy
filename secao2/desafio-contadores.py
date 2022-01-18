"""
DESAFIO: FAZER UM CONTADOR DE 0-8 E 10-2 NO MESMO LAÇO DE REPETIÇÃO
PODENDO USAR FOR / WHILE A PREFERENCIA
"""
# forma que eu fiz
crescente=-1
descrescente=11
while crescente<=7 and descrescente>=3:
    crescente+=1
    descrescente-=1
    print(f'crescente: {crescente}, decrescente: {descrescente}')

# resolução do video 
for p, r in enumerate(range(10,1,-1)):
    print(f'crescente: {p}, decrescente: {r}')