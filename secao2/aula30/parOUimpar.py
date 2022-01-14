# EXERCICIO 1: PROGRAMA PARA VERIFICAR SE É PAR OU IMPAR, VALIDAR SE É NUMERO INTEIRO
try:
    numero=int(input("Digite um numero inteiro: "))
    if(numero%2==0):
        print("Par")
    else:
        print("Impar")
except:
    print("Digite um numero inteiro")
