""" 
FOR IN EM PYTHON
ITERANDO STRINGS COM PYTHON
FUNÇÃO RANGE (start=0, stop, step=1)
"""

texto='Python'
nova_frase=''

for letra in texto:
    if letra == 't':
        nova_frase += letra.upper()
    elif letra == 'o':
        nova_frase += letra.upper()
    else:
        nova_frase += letra
    print(f'frase: {nova_frase}') 

for numero in range(10): # iterando de 0 ate 9 passo 1; padrão: (start=0, stop, step=1)
    print(numero)

for i in range(1,21,2): # iterando de 1 ate 21 passo 2 (de 2 em 2 numeros)
    print(i)