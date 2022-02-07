"""
FUNÇÕES DECORADORAS E DECORADORES EM PYTHON 
- utilizada para adicionar um recurso nas funções
"""
# função decoradora
def master(funcao):
    def slave():
        print("Agora estou decorada")
        funcao()
    return slave

def fala_oi():
    print('Oi')

fala_oi = master(fala_oi) # funcao decorada

@master # decorador, nesse caso nao vai mais haver a necessidade de criar uma variavel como a 'fala_oi = master(fala_oi)' pois ja estamos 
# informando o decorador!!!
def fala_oi():
    print('Oi')

fala_oi()

# EXEMPLO MAIS CLARO
"""
Funções decoradoras recebem uma função como parâmetro e decoram/modificam
ela retornando uma nova a ser usada no lugar.
"""
 
def decorar(funcao):
    
    # Geralmente, ao decorar uma função, deseja-se substituí-la por outra.
    # E esta abaixo irá substituir a recebida como parâmetro acima
    def funcao_decorada():
        print('############')
        funcao()
        print('############')
 
    return funcao_decorada
 
def printar():
    for i in range(3):
        print(i)
 
nova_printar = decorar(printar)
 
nova_printar()
# Saída:
# ############
# 0
# 1
# 2
# ############
# 
# Ou seja, fizemos uma decoração/modificação na função printar().
# Ao colocar o @decorador em cima de uma função X, o que o
# interpretador do Python faz é X = decorador(X).