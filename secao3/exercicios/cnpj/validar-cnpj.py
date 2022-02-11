"""
MINHA SOLUÇÃO
EXERCICIO VALIDAR CNPJ
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segundo digito
"""
# variaveis
cnpj=input("Digite seu CNPJ: ")
print()
cnpj_to_confirm=[num for num in cnpj if num.isdigit()] # para confirmar posteriormente
cnpj_lista=[num for num in cnpj[0:-3] if num.isdigit()] # capturando numeros ate antes dos digitos
int_list_cnpj = list(map(int, cnpj_lista)) # convertendo para inteiro

# primeiro digito 
mult=[5,4,3,2,9,8,7,6,5,4,3,2] #mult=['5','4','3','2','9','8','7','6','5','4','3','2']
digito1=[int_list_cnpj[i]*mult[i] for i in range(len(int_list_cnpj))] # multiplicando cada valor do cnpj por 'mult' p/gerar digito1
soma=sum(digito1) # somando valores da lista
digito1= 11 - (soma % 11)
if digito1<=9:
    digito1=digito1
else:
    digito1=0
print(f'digito 1 = {digito1}')

# segundo digito 
int_list_cnpj.append(digito1)
mult=[6,5,4,3,2,9,8,7,6,5,4,3,2,digito1] 
digito2=[int_list_cnpj[i]*mult[i] for i in range(len(int_list_cnpj))] 
soma=sum(digito2) 
digito2= 11 - (soma % 11)
if digito2<=9:
    digito2=digito2
else:
    digito2=0
print(f'digito 2 = {digito2}')
int_list_cnpj.append(digito2)

# adicionando digitos a lista para comparar ao original 
cnpj_lista.append(str(digito1))
cnpj_lista.append(str(digito2))
cnpj_formatado=''.join(cnpj_lista)
print(f'CNPJ validado: {cnpj_formatado[0:2]}.{cnpj_formatado[2:5]}.{cnpj_formatado[5:8]}/{cnpj_formatado[8:12]}-{cnpj_formatado[12:]}')
print('-'*20)
if cnpj_lista==cnpj_to_confirm:
    print("CNPJ VALIDO")
else:
    print("CNPJ INVALIDO")