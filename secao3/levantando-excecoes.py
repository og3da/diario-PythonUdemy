"""
LEVANTANDO EXCEÇÕES USANDO 'RAISE' COM PYTHON
- usando raise ValueError("mensagem") podemos criar nossa propria exceção, passando a mensagem desejada
"""
def dividir(n1,n2):
    if n2 == 0:
        raise ValueError("Digite um numero diferente de 0!")
    else:
        return n1 / n2

print(dividir(1,0))