"""
FAÇA UMA LISTA DE TAREFAS COM AS SEGUINTES OPÇÕES:
    - adicionar tarefas
    - listar tarefas
    - opção de desfazer (desfaz a ultima ação))
    - opção de refazer (refaz a ultima ação)
"""
lista=[]
lista_temp=[]
def opcoes():
    print("--- ESCOLHA UMA OPÇÃO ---")
    print("-- ADICIONAR TAREFA 1 --")
    print("-- LISTAR TAREFAS 2 --")
    print("-- DESFAZER 3 --")
    print("-- REFAZER 4 --")
    print("-- SAIR 5 --")
    
while True:
    print()
    opcoes()
    try:
        opcao=int(input("Digite uma opcao: "))
        print()
        if (opcao==1):
            tarefa=input("Digite a tarefa: ")
            lista.append(tarefa)
            lista_temp.append(tarefa)
            print("tarefa adicionada")
            print('-'*20)
        elif (opcao==2):
            print("tarefas: ")
            for tarefa in lista:
                print(f'{tarefa};')
            print('-'*20)
        elif (opcao==3):
            lista.pop()
            print("desfeito")
            print('-'*20)
        elif (opcao==4):
            lista.append(lista_temp[-1])
            lista_temp.pop()
            print("refeito")
            print('-'*20)
        elif (opcao==5):
            break
    except ValueError:
        print("Digite um valor válido!")
    except IndexError: 
        print("Nenhuma alteração a fazer!")
    except: 
        print("Ocorreu algum erro inseperado!")
    