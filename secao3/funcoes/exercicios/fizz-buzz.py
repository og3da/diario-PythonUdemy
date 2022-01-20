"""
4 - FIZZ BUZZ - SE O PARAMETRO DA FUNÇÃO FOR DIVISIVEL POR 3 RETORNE FIZZ, SE FOR POR 5 RETORNE BUZZ. SE FOR POR 5/3 
RETORNE FIZZ BUZZ. CASO CONTRARIO RETORNE O NUMERO ENVIADO
"""
def soma(valor):
    if (valor % 3) == 0 and (valor % 5) == 0:
        return("FIZZ BUZZ")
    elif (valor % 3) == 0:
        return("FIZZ")
    elif (valor % 5) == 0:
        return("BUZZ")
    return(valor)

valor=int(input("Digite um valor: "))
print(soma(valor))