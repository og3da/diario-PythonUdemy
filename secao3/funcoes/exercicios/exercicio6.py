"""
6 - CRIE UMA FUNÇÃO1 QUE RECEBE UMA FUNÇÃO2 COMO PARAMETRO E RETORNE O VALOR DA FUNÇÃO2 EXECUTADA.
FAZER A FUNÇÃO1 EXECUTAR DUAS FUNÇÕES QUE RECEBA UM NUMERO DIFERENTE DE ARGUMENTOS
"""

def funcao1(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def funcao2(nome):
    return f'Ola {nome}'

def funcao3(sobrenome,saudacao):
    return f'{saudacao} {sobrenome}'

executando=funcao1(funcao2,'raphael')
executando1=funcao1(funcao3,'og3da','Fala, querido')
print(executando)
print(executando1)