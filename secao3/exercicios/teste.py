lista_de_listas_de_inteiros = [
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

valores=[] # lista para iterar valores e verificar duplicado
duplicado=False

def verificarValorDuplicado(v):
    global duplicado
    if v in valores:
        duplicado=True
        print(f'valor {v} duplicado')
    elif len(valores) != 0 and str(valor) == str(lista[-1]) and duplicado == False:
        if str(valores[-1]) == str(lista[-2]): 
            print("sem valores duplicados: -1")
        else:
            pass
    
for lista in lista_de_listas_de_inteiros:
    print()
    valores.clear()
    print(f'lista: {lista}')
    for valor in lista:
        verificarValorDuplicado(str(valor))
        valores.append(str(valor)) # adicionando valor para a lista 'valores' p/verificação