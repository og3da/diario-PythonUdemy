"""
CRIANDO, LENDO, ESCREVENDO E APAGANDO ARQUIVOS EM PYTHON
"""
import os,json
file = open('ola.txt','w+') # abrindo arquivo ola.txt e dando permissao de leitura+escrita
 # escrevendo no arquivo
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')
# lendo todos os dados do arquivo
file.seek(0, 0)
print("lendo linhas:")
print(file.read())
...
print(file.readlines()) # este tambem le todas linhas do arquivo
print('-'*10)
# lendo linha por linha
file.seek(0, 0)
print("lendo linhas:")
print(file.readline(),end='') # linha1
print(file.readline(),end='') # linha2
print('-'*10)
# fechando o arquivo
file.close()

# gerenciador de contexto (faz com que nao precise fechar o arquivo apos utilizar):
with open('ola.txt', 'w+') as file:
    file.write('Linha1\n')
    file.write('Linha2\n')
    file.write('Linha3\n')

    file.seek(0)
    print("lendo linhas:")
    print(file.read())

# removendo arquivo
os.remove('ola.txt')

# convertendo para json
d1= {
    'Pessoa1': {
        'nome': 'Ogeda', 
        'idade': 19
    },
    'Pessoa2': {
        'nome': 'Vitao', 
        'idade': 18 
    },
}

d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('ola.json', 'w+') as file: # aqui estamos criando um arquivo com o mesmo conteudo do json
    file.write(d1_json)