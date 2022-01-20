"""
3 - CRIE UMA FUNÇÃO QUE RECEBE UM VALOR E UM PERCENTUAL E RETORNE O PRIMEIRO VALOR SOMADO DO PERCENTUAL PASSADO
"""
def soma(valor,percentual):
    return valor + (valor*percentual)/100

valor=float(input("Digite um valor: "))
percentual=int(input("Digite um percentual a somar: ")) 
print("resultado:",soma(valor,percentual))