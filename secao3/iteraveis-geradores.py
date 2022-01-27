"""
Iteraveis, iteradores e geradores em Python
- iteravel: qualquer objeto que é possivel percorrer por cada elemento
- iteradores: pode passar por cada elemento individualmente, usando a função .next()
- geradores: diferente da lista, este ocupa espaço em memoria de acordo com o utilizado. E pode mostrar a iteração em tempo real
"""
import time 
import sys

# iterando
def iterador():
    lista=[]
    for v in range(10):
        lista.append(v)
    return(lista)

i = iterador()
print(i)

# gerador que mostra em tempo real, iterando em cada valor
def gerador():
    for v in range(10):
        yield v 
        time.sleep(0.1)

g = gerador()
for v in g:
    print(v)
...

# utilizado yield e .next() para exibir um valor de cada vez em um gerador
def gerador():
    v = 'variavel1'
    yield v
    v = 'variavel2'
    yield v
    v = 'variavel3'
    yield v

g = gerador()
print(next(g)) # esta exibe um valor por vez
print(next(g))
print(next(g))
    
# espaço em memoria ocupado (no gerador é dinamicamente alocado)
print()
lista=[x for x in range(10000)]
gerador=(x for x in range(10000))
print(sys.getsizeof(lista))
print(sys.getsizeof(gerador))

"""
COMPREENSÃO DO Yield
Leia yield como "pausa e entrega o valor atual" que talvez entenderá melhor.
Um código comentado etapa por etapa para ajudar na compreensão:
"""
def entrega_numero(maximo):
    """ Uma função geradora que entrega números """
 
    # De onde vamos iniciar a entrega de números = 0
    numero_inicial = 0
 
    # Um loop - enquanto "maximo" for maior que o "numero_inicial"
    # as voltas do laço ocorreram (poderia ser for também, tanto faz)
    while maximo >= numero_inicial:
        # Leia yield como "pausa aqui e entrega o valor atual"
        yield numero_inicial
 
        # Garantimos que o nosso "numero_inicial" será incrementado
        # assim temos como parar o laço while
        numero_inicial += 1
 
 
# Aqui, estamos apenas usando o gerador para pegar números de 0 a 4
pega_numeros = entrega_numero(4)
 
# Obtendo os números
print(next(pega_numeros))  # 0
print(next(pega_numeros))  # 1
print(next(pega_numeros))  # 2
print(next(pega_numeros))  # 3
print(next(pega_numeros))  # 4

""" Note que nesse código, eu trabalho com números para simplificar as coisas, mas yield pode pausar e entregar qualquer coisa que você quiser. 
Exemplo: """

def pausa_e_entrega_texto():
    yield 'Texto 1'
    yield 'Texto 2'
    yield 'Texto 3'
 
 
for texto in pausa_e_entrega_texto():
    print(texto)
"""
Saída:
Texto 1
Texto 2
Texto 3
"""

"""
Cada yield vai ser executado na ordem que for chamado na função. No exemplo acima, vemos isso claramente. Na primeira iteração do laço for 
usando a função geradora, o gerador pausou e me entregou o valor do primeiro yield (Texto 1, nesse caso).
Depois, na sequência, Texto 2 e Texto 3.

Note que se você criar uma função geradora e entregar um valor com yield, o código da função não para de ser executado(como acontece com return)
mas o restante do código executado só será entregue no próximo yield.

Veja isso mais claramente:
"""
def fala_ola_mundo():
    ola_mundo = 'Olá'
    yield ola_mundo
    ola_mundo += ' Mundo'
    yield ola_mundo
 
 
fala = fala_ola_mundo()
print(next(fala))  # Olá
print(next(fala))  # Olá Mundo