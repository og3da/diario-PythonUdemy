"""
FUNÇÕES EM PYTHON - def (parte1)
- em python podemos criar nossa propria função, usando -> def nome_funcao():
- uma função com passagem de parametros sempre deve receber os valores ao ser chamada. Exemplo:

def funcao(msg,nome):
    print(msg, nome)

funcao('Eai mano','og3da')

- tambem podemos criar um valor de resposta padrao para caso nao sejam passados os parametros

def funcao(msg='Ola', nome='usuario'):
    print(msg, nome)

funcao()

função .replace():
- esta substitui o valor definido por outro. 
"""
def funcao():
    print("Ola mundo")

funcao()

# função com passagem de parametros
def funcao1(msg='Ola', nome='usuario'): #<- podemos usar ='' apos a variavel para estabelecer um valor padrao caso nao seja passado o parametro
    print(msg, nome)

funcao1()
funcao1('Eai meu caro', 'ogeda')

# função .replace()
def funcao3(msg):
    msg= msg.lower().replace('e','3')
    print(msg)

funcao3('Eai meu caro ogeda')