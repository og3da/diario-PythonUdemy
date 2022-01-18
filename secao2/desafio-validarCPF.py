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
""" from operator import mul
def calculoDigito(i):
    digito = 11 - (i % 11)
    if digito>9:
        digito=0
    else:
        digito=digito
    print(f'valor do digito: {digito}')  """

cpf=input("Digite seu CPF: ")
cpf_temp=[]
# aqui estou separando individualmente cada valor digitado em cpf na lista cpf_temp
for valor in cpf:
    cpf_temp+=valor

# aqui estou multiplicando cada valor pelo multiplicador e concatenando os resultados para chegar ao 1º digito
multiplicador=11
for i in cpf_temp:
    i=int(i)
    i = (i*multiplicador)
    multiplicador-=1
    print(f'valor de i: {i},valor de multiplicador {multiplicador}')
    if multiplicador<=2:
        break
    else:
        continue
print("")
i=int(i)
digito1 = 11 - (i % 11)
if digito1>9:
    digito1=0
else:
    digito1=digito1
print(f'valor do digito: {digito1}')  
