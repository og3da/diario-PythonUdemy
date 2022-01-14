# OPERADORES LOGICOS
# AND, OR, NOT, IN, NOT IN
a=1
b=-1

print(a and b > 0) #retorna falso pois o valor verdade de "and" é V & V (ambas devem ser verdadeiras)
print(a or b > 0) #retorna true pois "or" apenas uma deve ser verdadeira 
#not retorna o resultado oposto

# operador 'in'
nome="Ogeda"
if 'ge' in nome:
    print(f'a palavra procurada esta dentro do nome {nome}') #vai retornar o print pois 'ge' esta dentro da variavel nome

# operador 'not in'
print("")
if 'geada' not in nome:
    print(f'a palavra procurada nao esta dentro do nome {nome}') #vai retornar o print pois 'geada' nao esta dentro da variavel nome

# EXERCICIO DURANTE A AULA
# CRIANDO SISTEMA DE LOGIN
print("")
print("--- EXERCICIO ---")
usuario = input("Digite o user: ")
senha = input("Digite a senha: ")

usr="oge"
senh="oge"

if usuario==usr and senha==senh:
    print("Login efetuado")
else:
    print("Login incorreto")