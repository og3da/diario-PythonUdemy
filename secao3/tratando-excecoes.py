"""
TRATAMENTO DE EXCEÇÕES COM 
TRY e EXCEPT

- quando tratamos erros com try e except podemos prosseguir com o codigo normalmente
- tratando erros é importante especificar qual está sendo tratado no bloco except (ex: except NameError)
- se for usado apenas (except Exception:) qualquer tipo de erro sera tratado no bloco except
- podemos tratar mais de um erro no mesmo except
"""
try:
    print(a)
except NameError: # tratando um erro especifico
    print(f"um erro ocorreu durante a execução.")
except (KeyError, IndexError): # podemos tratar mais de um erro no mesmo except
    print("Erro de indice ou chave")
except Exception: # nesse caso qualquer erro diferente do NameError ira retornar o codigo abaixo
    print("Erro inesperado")
else: # caso nao ocorra um erro esse bloco sera executado tambem
    print("codigo executado com sucesso")
finally: # sera executado caso tenha erro ou nao
    print('finalmente')

print('prosseguindo...')