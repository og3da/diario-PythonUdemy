from random import randint

def gerar(cn):
        while True:
            # variaveis
            cnpj=[x for x in cn]
            int_cnpj = list(map(int, cnpj)) # convertendo para inteiro

            # primeiro digito 
            mult=[5,4,3,2,9,8,7,6,5,4,3,2] #mult=['5','4','3','2','9','8','7','6','5','4','3','2']
            digito1=[int_cnpj[i]*mult[i] for i in range(len(int_cnpj))] # multiplicando cada valor do cnpj por 'mult' p/gerar digito1
            soma=sum(digito1) # somando valores da lista
            digito1= 11 - (soma % 11)
            if digito1<=9:
                digito1=digito1
            else:
                digito1=0

            # segundo digito 
            int_cnpj.append(digito1)
            mult=[6,5,4,3,2,9,8,7,6,5,4,3,2,digito1] 
            digito2=[int_cnpj[i]*mult[i] for i in range(len(int_cnpj))] 
            soma=sum(digito2) 
            digito2= 11 - (soma % 11)
            if digito2<=9:
                digito2=digito2
            else:
                digito2=0

            # adicionando digitos a lista para comparar ao original 
            cnpj.append(str(digito1))
            cnpj.append(str(digito2))
            cnpj_formatado=''.join(cnpj)
            print(f'CNPJ gerado: {cnpj_formatado[0:2]}.{cnpj_formatado[2:5]}.{cnpj_formatado[5:8]}/{cnpj_formatado[8:12]}-{cnpj_formatado[12:]}')
            break

numero = str(randint(100000000000, 999999999999))
gerar(numero)