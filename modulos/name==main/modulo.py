"""
if __name__ == '__main__': 
- no caso do arquivo de modulo conter a expressão acima, ele ira executar o conteudo de if apenas no arquivo do modulo
- conforme exemplo abaixo 
"""
# isso podera ser executado no import normalmente
def soma(n1: float,n2: float): 
    return n1+n2

print('executando dentro e fora do arquivo de modulo')

if __name__ == '__main__': 
    print('estamos dentro do arquivo de modulo. Executando...')
    print('tudo ok')