from random import randint
numero = str(randint(10000000000000, 99999999999999))

def validar(cn):
    try:
        while True:
            # variaveis
            cnpj=cn
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
            if cnpj_lista==cnpj_to_confirm:
                #print(f'CNPJ validado: {cnpj_formatado[0:3]}.{cnpj_formatado[2:5]}.{cnpj_formatado[5:8]}/{cnpj_formatado[8:12]}-{cnpj_formatado[12::]}')
                return cnpj_formatado
            else:
                pass
    except:
        print("ocorreu um erro inesperado")

print(validar(numero))