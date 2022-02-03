"""
USANDO TRY E EXCEPT COMO CONDICIONAL
"""
def converteNumero(valor): # como condicionais 
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except:
            pass

numero = converteNumero(input("Digite um numero: "))
if numero is None:
    print("Digite um numero!")
else:
    print(numero * 2)