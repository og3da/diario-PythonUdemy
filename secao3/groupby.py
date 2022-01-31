"""
GROUPBY - AGRUPANDO VALORES
- groupby é usado para dividir um objeto em grupos. Exemplo usado: grupo de alunos que tiraram a nota x
- para agrupar valores usando groupby é necessario que estejam em ordem 

supondo uma sala de aula, criamos uma lista de dicionarios com aluno e nota, usamos a função sort para ordenar os alunos de acordo com a nota 
e a função groupby para agrupar os alunos por nota. No exemplo abaixo podemos ver cada grupo de alunos que tiraram a nota x: 
"""
from itertools import * 
# lista de alunos/notas
alunos = [
    {'nome': 'Ogeda', 'nota': 10},
    {'nome': 'Luis', 'nota': 7},
    {'nome': 'Carlos', 'nota': 10},
    {'nome': 'Laura', 'nota': 5},
    {'nome': 'Luana', 'nota': 7},
    {'nome': 'Lucas', 'nota': 10},
    {'nome': 'Lulu', 'nota': 5},
    {'nome': 'Carlin', 'nota': 5},
    {'nome': 'Lau', 'nota': 5},
    {'nome': 'Lua', 'nota': 7},
]

# aqui vamos ordenar por nota decrescente usando a função lambda 
ordena = key=lambda item: item['nota'] # função lambda para ordenar os alunos por nota
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena) # agrupando os alunos por nota

# exibindo resultados
for agrupamento, valores_agrupados in alunos_agrupados:
    print()
    print(f'NOTA: {agrupamento}')

    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')

"""
outro cenário para entendimento de quando usar groupby:

imagine que eu tenha um grupo de pessoas com idades variadas, porém, algumas delas tem exatamente a mesma idade. 
Suponha que eu queira escrever um programa para separar as pessoas de mesma idade em seus próprios grupos... 
Pessoas de 20 anos, pessoas de 30 anos, todos com a mesma idade em agrupados em grupos menores...

Esse é o cenário exato para usar groupby (vamos agrupar por idade).
"""