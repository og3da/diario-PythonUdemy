"""
FUNÇÕES EM PYTHON - def (parte4)
- explicando variaveis de escopo local/global
- uma variavel de escopo local só existe e pode ser usada dentro da mesma função
- uma variavel global pode ser usada em todo o codigo
- nao podemos usar variaveis locais em outras funções/partes do codigo!
"""
nome='og3da'
def funcao(): # escopo global
    print(nome)

def funcao1(): # escopo local
    nome='outro'
    print(nome)

def funcao2(): # alterando var de escopo global
    global nome # devemos declarar a variavel global p/ alterações na função
    nome='outro og3da'
    print(nome)

funcao()
funcao1()
funcao2()