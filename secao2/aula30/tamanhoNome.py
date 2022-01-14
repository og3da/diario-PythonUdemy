# EXERCICIO 3: MEDIR TAMANHO DO NOME E INFORMAR DE ACORDO COM O TAMANHO:
# ATE 4 CARACTERES: "SEU NOME É CURTO"; ENTRE 5-6: "SEU NOME É NORMAL"; 7> "SEU NOME É GRANDE"
nome=input("Digite seu nome: ")
verify=len(nome)
if(verify<=4):
    print("SEU NOME É CURTO")
elif(verify<=6):
    print("SEU NOME É NORMAL")
elif(verify>=7):
    print("SEU NOME É GRANDE")