"""
SISTEMA DE PERGUNTAS E RESPOSTAS COM DICIONARIO
"""
perguntas = {
    'pergunta 1': {
        'pergunta' : 'quanto é 2+2? ',
        'respostas' : {'a' : 4, 'b' : 8, 'c' : 10,},
        'resposta certa':'a',
    },
    'pergunta 2': {
        'pergunta' : 'quanto é 2+20? ',
        'respostas' : {'a' : 20, 'b' : 22, 'c' : 202,},
        'resposta certa':'b',
    },
    'pergunta 3': {
        'pergunta' : 'quanto é 2*2? ',
        'respostas' : {'a' : 4, 'b' : 8, 'c' : 10,},
        'resposta certa':'a',
    },
}
acertos=0
for pk, pv in perguntas.items(): # pergunta-key, pergunta-value
    print(f'{pk}: {pv["pergunta"]}')
    print("Escolha uma das opções abaixo: ")

    for rk, rv in pv['respostas'].items(): # resposta-key, resposta-value
        print(f'{rk}: {rv}') # exibe todas respostas possiveis
    resposta_user=input("Digite sua resposta: ")

    if resposta_user == pv['resposta certa']: 
        print("Parabens vc acertou!")
        acertos+=1
    else:
        print("Você errou")
    print()

print(f'acertos= {acertos}')