"""
MÓDULOS EM PYTHON
- módulos são arquivos .py que contém funcionalidades para usar em nossos programas
- podemos usar módulos padrao do python ou instalar modulos externos
- é recomendado ler a documentação do módulo antes de usa-lo
- podemos instalar módulos usando o 'pip install nome_modulo' na linha de comando
- também podemos criar nossos proprios módulos e pacotes!

https://docs.python.org/3/py-modindex.html - documentação de módulos
"""
import sys # importando o módulo por inteiro
from sys import platform # importando apenas a funcionalidade
from random import random, randint # podemos importar duas funcionalidades na mesma linha 

print(sys.platform)
print(platform)