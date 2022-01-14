#  WHILE/ELSE COM ACUMULADORES

acumulador=1
contador=1

while contador<=10:
    print(f'acumulador: {acumulador},contador {contador}')
    if contador>5:
        break
    acumulador=acumulador+contador
    contador+=1
else:
    print("Cheguei no else") # no caso se a condição for parada pelo 'break' ira entrar no bloco else
print("Nao foi necessario")