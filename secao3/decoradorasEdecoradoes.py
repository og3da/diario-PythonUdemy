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

@master # decorador
def fala_oi():
    print('Oi')

fala_oi()