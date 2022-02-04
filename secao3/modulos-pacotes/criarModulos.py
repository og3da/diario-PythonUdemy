"""
COMO CRIAR SEUS PROPRIOS MÓDULOS EM PYTHON
- vamos usar o arquivo 'myMod.py' como modulo para fazer calculos
- podemos usar o modulo para executar funções necessarias para o programa
- no arquivo do modulo por padrao o nome dele é '__main__' 
"""
import myMod
print(myMod.multiply(2,2))
print(myMod.div(2,2))
print(__name__)