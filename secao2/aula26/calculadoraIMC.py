# CALCULADORA DE IMC 
nome=str(input("digite seu nome: "))
idade=int(input("digite sua idade: "))
altura=float(input("digite sua altura: "))
peso=float(input("digite seu peso: "))
imc=peso/(altura*altura)

print(f'ola {nome}, com {idade} anos você tem imc igual a: {imc:.2f}') # a expressão ":.2f" é para exibir duas casas decimais apos o ponto