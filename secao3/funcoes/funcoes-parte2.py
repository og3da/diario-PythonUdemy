"""
FUNÇÕES EM PYTHON - def (parte2)
- explicando função com passagem de parametros e 'return'
"""
def divisao(n1,n2):
    if (n1 or n2) == 0:
        return 'Digite um numero != de 0'
    return n1 / n2

print(divisao(10,2))