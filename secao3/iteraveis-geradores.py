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