"""
LEVANTANDO EXCEÇÕES USANDO 'RAISE' COM PYTHON
- usando raise ValueError("mensagem") podemos criar nossa propria exceção, passando a mensagem desejada
- no caso raise vai fazer com que a mensagem padrao de resposta da exceção seja a que for definida na função
"""
def dividir(n1,n2):
    if n2 == 0:
        raise ValueError("Digite um numero diferente de 0!") # essa mensagem sera retornada ao inves da msg padrao de erro 
    else:
        return n1 / n2

try:
    print(dividir(1,0))
except ValueError as error:
    print(error) # aqui estamos printando a mensagem de erro