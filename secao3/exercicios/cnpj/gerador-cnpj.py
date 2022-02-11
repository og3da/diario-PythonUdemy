from random import randint
def validar_digito(soma):
    digito= 11 - (soma % 11)
    if digito<=9:
            digito=digito
    else:
        digito=0
    return digito

def gerar(cnpj1):
        # variaveis
        cnpj=[x for x in cnpj1]
        int_cnpj = list(map(int, cnpj)) # convertendo para inteiro
        mult1=[5,4,3,2,9,8,7,6,5,4,3,2] 
        mult=[6,5,4,3,2,9,8,7,6,5,4,3,2] 

        # primeiro digito 
        digito1=[int_cnpj[i]*mult1[i] for i in range(len(int_cnpj))] # multiplicando cada valor do cnpj por 'mult' p/gerar digito1
        soma=sum(digito1) # somando valores da lista
        digito1 = validar_digito(soma)

        # segundo digito 
        int_cnpj.append(digito1)
        mult.append(digito1)
        digito2=[int_cnpj[i]*mult[i] for i in range(len(int_cnpj))] 
        soma=sum(digito2) 
        digito2 = validar_digito(soma)

        # adicionando digitos ao cnpj gerado
        cnpj.append(str(digito1))
        cnpj.append(str(digito2))
        cnpj_formatado=''.join(cnpj)
        print(f'CNPJ gerado: {cnpj_formatado[0:2]}.{cnpj_formatado[2:5]}.{cnpj_formatado[5:8]}/{cnpj_formatado[8:12]}-{cnpj_formatado[12:]}')
    
numeros_iniciais = str(randint(100000000000, 999999999999)) # gerando os numeros iniciais do CNPJ sem os digitos
gerar(numeros_iniciais)
