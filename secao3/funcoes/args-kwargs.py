"""
FUNÇÕES EM PYTHON - def (parte3)

Use args e kwargs quando uma função precisar receber um número indefinido de parâmetros.
A diferença entre args e kwargs é simplesmente se o parâmetro é ou não nomeado. 
Se não for um parâmetro nomeado, cai em args, se for nomeado cai em kwargs.
args é uma tupla de elementos com todos os argumentos. Kwargs é um dicionário.

- *args <- quando nao sabemos quantos argumentos iremos usar na função podemos utilizar este. Retorna tupla
- **kwargs <- palavras-chave como (nome='og3da',idade=19) sao passados apenas para **kwargs. Retorna dicionario
- sep='' <- usamos como separador entre os caracteres
"""
lista=[1,2,3,4,5]

def funcao(*args, **kwargs):
    print(args)
    print(kwargs)

print(*lista, sep='-') # desempacotado os valores e os separando por '-'
funcao(*lista) # quando usamos o '*' antes de passar um objeto do tipo lista, cada valor é desempacotado, ou seja, passado individualmente
funcao(lista) # quando passamos a lista inteira, esta é passada por completo no indice 0 da tupla
funcao(nome='og3da',idade=19) # valores desse tipo sao passados para **kwargs