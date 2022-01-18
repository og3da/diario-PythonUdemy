""" 
VALIDAR UM CPF USANDO Python
(validando os 2 ultimos digitos)
CALCULO: 
- Pegue os 9 primeiros numeros do cpf e multiplique de 10-2 de forma decrescente (partindo do primeiro numero do cpf)
resultado = 11 - (resultado % 11)
se for > que 9, digito sera = 0
acima conseguimos o primeiro digito do cpf

- Agora novamente com os 9 primeiros numeros do cpf multiplicamos de 11-2 de forma decrescente (a ultima multiplicação sera digito1*2)
resultado = 11 - (resultado % 11)
se for > que 9, digito sera = 0
acima conseguimos o segundo digito do cpf
"""

cpf=input("Digite seu CPF: ")
cpf_temp=[]
# aqui estou separando individualmente cada valor digitado em cpf na lista cpf_temp
for valor in cpf:
    cpf_temp+=valor

# aqui estou multiplicando cada valor pelo multiplicador e concatenando os resultados (soma+= int(i) *multiplicador) para chegar ao 1º digito
soma=0
multiplicador=10
for i in cpf_temp:
    soma+= int(i) *multiplicador
    multiplicador-=1
    if multiplicador==1:
        break
    else:
        continue

print("")
digito1 = 11 - (soma % 11)
if digito1>9:
    digito1=0
else:
    digito1=digito1
print(f'valor do digito 1: {digito1}')  

#  para chegar ao 2º digito
soma=0
multiplicador=11
for i in cpf_temp:
    soma+= int(i) *multiplicador
    multiplicador-=1
    if multiplicador==1:
        break
    else:
        continue

digito2 = 11 - (soma % 11)
if digito2>9:
    digito2=0
else:
    digito2=digito2
print(f'valor do digito 2: {digito2}')  

# validando o cpf
print("")
if (digito1==int(cpf_temp[9])) and (digito2==int(cpf_temp[10])):
    print("CPF VÁLIDO!")
    print("--- created by og3da ---")
else:
    print("CPF INVÁLIDO!")
    print("--- created by og3da ---")