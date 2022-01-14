# ITERANDO STRINGS COM WHILE
# ITERAR -> PERCORRER
# ÍNDICES
#        0123456789........................33
frase=  'o rato roeu a roupa do rei de roma' # iterarável
tamanho_frase= len(frase)
contador=0
nova_frase=''

# Iterando
while contador<tamanho_frase:
    letra=frase[contador]
    if letra=='r':
        nova_frase=letra.upper()
    else:
        nova_frase=letra
    contador += 1
    print(nova_frase)