import random
import Functions
import Colors

letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letrasM = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
simbolos = '~`!@#$%^&*()_-+={]|\:;<,>.?/'

digitos = ""

## Definição de tamanho
tamanho = int(input(f"Digite o tamanho da senha {Colors.corVermelho()}(min: 8){Colors.limpar()}: "))
conferenciaTamanho = Functions.conferirTamanho(tamanho)

## Inclusão de letras na senha
incluirLetras = Functions.verificacaoSN("Incluir letras[S/N]? ")
if incluirLetras in "S":
    digitos += Functions.randomizar(letras, conferenciaTamanho)


## Inclusão de letras maiúsculas na senha
incluirLetrasM = Functions.verificacaoSN("Incluir letras maiúsculas[S/N]? ")
if incluirLetrasM in "S":
    digitos += Functions.randomizar(letrasM, conferenciaTamanho)


## Inclusão de números na senha
incluirNumeros = Functions.verificacaoSN("Incluir números[S/N]? ")
if incluirNumeros in "S":
    digitos += Functions.randomizar(num, conferenciaTamanho)


## Inclusão de símbolos na senha
incluirSimbolos = Functions.verificacaoSN("Incluir símbolos[S/N]? ")
if incluirSimbolos in "S":
    digitos += Functions.randomizar(simbolos, conferenciaTamanho)


## Embaralhar a senha
digitos = random.sample(digitos, conferenciaTamanho)   # Gera uma *lista* embaralhada

print("\nSua senha gerada é: ", end="")
for c in digitos:
    print(f"{Colors.corVerde()}{c}", end="")

## Limpar Cores
print(f"{Colors.limpar()}")
