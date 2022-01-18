# JOGO ADIVINHE A PALAVRA FEITO NA AULA 38 SEÇÃO 2

secreta='python'
letras_digitadas=[]
chances=3

print("--- SEJA BEM VINDO ---")
print("-- JOGO ADIVINHE A PALAVRA --")
while True:
    if chances == 0:
        print("VOCE PERDEU.")
        break
    else:
        letra=input("Digite uma letra: ")
        if (len(letra)>1):
            print("Pilantra, digita so 1 letra!")
            continue
        else:
            letras_digitadas.append(letra)
            if letra not in secreta:
                print(f"voce errou a letra: {letra}")
                letras_digitadas.pop()
                chances -= 1
            else: #se a letra esta na palavra secreta 
                print(f"parabens, vc acertou a letra {letra}")

            secreta_temp=''
            for letra_secreta in secreta:
                if letra_secreta in letras_digitadas:
                    secreta_temp += letra_secreta
                else:
                    secreta_temp += '*'
            
            if secreta_temp==secreta:
                print(f"Parabens vc ganho, palavra acertada: {secreta_temp}")
                break
            else:
                print(f"A palavra esta assim: {secreta_temp}")

            print(f'Você ainda tem {chances} chances.')
            print()