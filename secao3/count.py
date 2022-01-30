"""
.count() - Itertools
- pode fazer a contagem de qualquer coisa
- prestar atenção em seu uso pois pode gerar loop infinito

parâmetros aprendidos:
start='' - define um valor para iniciar a contagem
step='' - passo da contagem (ex: de 2 em 2, podendo ser -1 regressiva)

funções aprendidas:
.round() - arredonda valores
"""
from itertools import count

# .count()
contador = count(start=1,step=2)
for valor in contador:
    print(valor)
    if valor ==21:
        break

# .round()
v1=10.3
v2=10.6 
print('v1 arredondado: ',round(v1),'v2 arredondado: ',round(v2))

# colocar um indice em cada valor de uma lista usando count
contador = count(start=1)
lista=['Ogeda','Vitor','Matheus','Gui']
lista = zip(contador, lista)
print(list(lista))