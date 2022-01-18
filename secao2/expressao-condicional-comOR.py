# ENCURTANDO CONDICIONAIS COM O OPERADOR 'OR' 
# formato original
nome=input("Digite seu nome: ")
if nome:
    print(nome)
else:
    print("Digite algo")

# formato encurtado
nome= input("Digite seu nome: ")
print(nome or 'Digite algo!') # <- dessa forma encurtamos a digitação de uma estrutura condicional