# função para formatar o valor
def real(valor):
    return f'R${valor:.2f}'.replace('.',',')