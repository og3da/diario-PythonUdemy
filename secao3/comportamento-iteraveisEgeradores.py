# list, tuples, str -> iteraveis
nome='Raphael Ogeda'
iterador=iter(nome)
gerador=(letra for letra in nome)

# gerador
print(next(gerador)) # R
print(next(gerador)) # A
print(next(gerador)) # P
print(next(gerador)) # H
print(next(gerador)) # A
print(next(gerador)) # E
print(next(gerador)) # L

print("For")
for letra in gerador:
    print(letra)

print("Outro for") # mesmo fazendo o laço de novo, nao ira aparecer as letras pois o iterador esgotou
for letra in gerador:
    print(letra)

# nesse caso no iterador apos ser esgotado o .next() nao iria aparecer mais nada mesmo no laço for.
try:
    print(next(iterador)) # R
    print(next(iterador)) # A
    print(next(iterador)) # P
    print(next(iterador)) # H
    print(next(iterador)) # A
    print(next(iterador)) # E
    print(next(iterador)) # L
    print(next(iterador)) #  
    print(next(iterador)) # O
    print(next(iterador)) # G
    print(next(iterador)) # E
    print(next(iterador)) # D
    print(next(iterador)) # A
except:
    pass 

print("CONTINUANDO") 
# este for ira exibir as letras restantes do iterador
for letra in iterador:
    print(letra)