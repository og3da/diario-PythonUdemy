from vendas.formata import preco

def aumento(valor,percentual,formata=True):
    f= (valor + (valor * percentual/100))
    
    if formata:
        return preco.real(f)
    else:
        return f