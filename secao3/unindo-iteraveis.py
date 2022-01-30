"""
UNINDO ITERAVEIS COM
ZIP - UNINDO ITERAVEIS
ZIP_LONGEST - ITERTOOLS

funções aprendidas:
.zip() - junta iteraveis e descarta o restante 

.zip_longest() - junta iteraveis e retorna None para itens restantes que nao foram iterados
    fillvalue=" " - parametro para zip_longest que define valor pardao para retornos None
"""
from itertools import zip_longest # para usar o zip_longest é necessario importar o modulo

cidades=['Sao Paulo','Belo Horizonte','Salvador','Monte Belo','Outra']
estados=['SP','MG','BA'] # os dados devem estar na ordem

# .zip() - juntando as listas, retorna iterador. As cidades que nao foram preenchidas em 'estados' serao descartadas
cidades_estados = zip(estados, cidades)
print("zip> ",list(cidades_estados))

# .zip_longest() - juntando as listas, retorna None para as cidades que nao foram preenchidas em 'estados' ou um valor padrao em fillvalue
cidades_estados = zip_longest(estados, cidades, fillvalue="Estado")
print("zip_longest> ",list(cidades_estados))