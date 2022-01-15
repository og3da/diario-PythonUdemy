# JOGO ADIVINHE A LETRA FEITO NA AULA 38 SEÇÃO 2

secreta='python'
letras_acertadas=[]
chances=3

print("--- SEJA BEM VINDO ---")
print("-- JOGO ADIVINHE A PALAVRA --")
while True:
    if chances == 0:
        print("VOCE PERDEU.")
        break
    else:
        letra=input("Digite uma letra: ")
        if letra in secreta:
            letras_acertadas.append(letra)
            print(letras_acertadas)
        else:
            print("voce errou a letra")
            chances -= 1
            
