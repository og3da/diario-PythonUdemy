"""
Crie um programa que recebe uma lista de inteiros e um valor que deve ser buscado. 
O programa deve retornar o índice onde o valor foi encontrado, ou -1, caso não encontre o valor.
"""
lista=[]
adicionar=1

while True:
    while adicionar==1:
        inserir=int(input("Digite um valor para adicionar a lista: "))
        lista.append(inserir)
        adicionar=int(input("Digite 1 para continuar ou 2 para parar: "))
        if adicionar!=1:
            numero= int(input("Digite o valor a buscar: "))
            for i in lista:
                if numero in lista:
                    print(f"O valor '{numero}' se encontra no indice '{i}' da lista")
                    adicionar=int(input("Digite 1 para continuar ou 2 para parar: "))
                    if adicionar!=1:
                        break
                    else:
                        continue
                elif i>len(lista):
                    print("Valor nao encontrado")
                    break
                else:
                    continue