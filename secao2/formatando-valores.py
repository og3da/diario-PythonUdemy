"""
-- FORMATANDO VALORES COM MODIFICADORES --
podemos utilizar a função .format()
ou
"f strings": print(f'{variavel:format}')

:s - Texto (string)
:d  - Inteiro (int)
:f - Numeros de ponto flutuante (float)
:.(NUMERO)f - QUANTIDADE DE CASAS DECIMAIS A EXIBIR (float) :.2f
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - MOV. ESQUERDA
< - MOV. DIREITA
^ - MOV. CENTRO 

.lower() - converte em minusculas
.upper() - converte em maiusculas
.title() - primeiras letras em maiusculas (titulo)

"""
# formatando String
nome= input("Digite seu nome: ")
print(f'{nome:s}')

# formatando Inteiro
numero= 1
print(f'{numero:d}')

# formatando Float
numero= 15
print(f'{numero:.2f}') #aqui formatamos para exibirem 2 casas decimais apos o 15 (:.2f)

# formatando para exibirem 6# antes e depois da palavra MENU 
# FORMA F STRING
palavra= "MENU"
print(f'{palavra:#>10}') #(aparecem 6# a esquerda pois a palavra tambem conta 6+4=10)
print(f'{palavra:#<10}')
print(f'{palavra:#^10}') 

# FORMA DE FORMATAÇÃO SEPARADA
print('{:#^10}'.format(palavra))

print(palavra.lower())
print(palavra.upper())
print(palavra.title())