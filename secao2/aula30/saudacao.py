# EXERCICIO 2: FAZER SAUDAÇÃO AO USUARIO BASEADO NO HORARIO INFORMADO. BOM DIA 00-11, BOA TARDE 12-17, BOA NOITE 18-23
hora=int(input("Digite a hora atual: "))
if (hora >=0 and hora<=11):
    print("Bom dia!")
elif (hora>=12 and hora<=17):
    print("Boa tarde!")
elif (hora>=18 and hora<=23):
    print("Boa noite!")
else:
    print("Digite um horario entre 0 e 23!")
