import Colors

def ArquivoExiste(nome_arquivo):
    try:
        arquivo = open(nome_arquivo + ".txt", "rt")
    except:
        return False
    else:
        return True


def CriaArquivo(nome_arquivo):
    try: 
        arquivo = open(nome_arquivo + ".txt", "wt+")
    except Exception as error:
        print(f"Houve um erro para criar o arquivo: {Colors.corVermelho()}{error}{Colors.limpar()}")
    else:
        print(f"{Colors.corVerde()}Sucesso na criação do arquivo '{nome_arquivo}.txt'!{Colors.limpar()}\n") 
        arquivo.close()


def SalvaDado(nome_arquivo, tipo_dado, dado):
    try:
        arquivo = open(nome_arquivo + ".txt", "at+")
    except Exception as error:
        print(f"Houve um erro para salvar o dado: {Colors.corVermelho()}{error}{Colors.limpar()}")
    else:
        arquivo.write(tipo_dado + dado)
        arquivo.close()


def DeletaDado(nome_arquivo):
    try:
        arquivo = open(nome_arquivo + ".txt", "w+")
    except Exception as error:
        print(f"Erro: {error}")
    else:
        arquivo.write("")

def conferirTamanho(tam):
    try:
        import Colors
        while tam < 8:
            print(f"Senha {Colors.corVermelho()}fraca{Colors.limpar()} demais!")
            tam = int(input(f"Digite o tamanho da senha {Colors.corVermelho()}(min: 8){Colors.limpar()}: "))
    
    except Exception as error:
        print(f"Houve um erro em conferir o tamanho: {error.__class__}")
    
    else:
        if tam >= 8 and tam < 10:
            print(f"{Colors.corAmarelo()}Tamanho OK!{Colors.limpar()}\n")
        else:
            print(f"{Colors.corVerde()}Tamanho excelente!{Colors.limpar()}\n")
        return tam


def randomizar(variavel, tam=8):
    try:
        import random

        gerado = ""
        for c in range(0, tam):
            gerado += random.choice(variavel)
    except Exception as error:
        print(f"Erro: {error}")
    else:
        return gerado


def verificacaoSN(pergunta=""):
    try:
        verf = str(input(pergunta)).strip().upper()[0]
        
        while verf not in "SN":
            print("Digite novamente...")
            verf = str(input(pergunta)).strip().upper()[0]
    except Exception as error:
        print(f"Erro para verificar: {error}")
    else:
        return verf

def GerarSenha(nome_arquivo):
    import random

    letras = 'abcdefghijklmnopqrstuvwxyz' 
    letrasM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '1234567890'
    simbolos = '~`!@#$%^&*()_-+={]|\:;<,>.?/'

    digitos = ""

    tamanho = int(input(f"Digite o tamanho da senha {Colors.corVermelho()}(min: 8){Colors.limpar()}: "))
    conferenciaTamanho = conferirTamanho(tamanho)

    ## Inclusão de letras na senha
    incluirLetras = verificacaoSN(f"Incluir letras[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")
    if incluirLetras in "S":
        digitos += randomizar(letras, conferenciaTamanho)


    ## Inclusão de letras maiúsculas na senha
    incluirLetrasM = verificacaoSN(f"Incluir letras maiúsculas[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")
    if incluirLetrasM in "S":
        digitos += randomizar(letrasM, conferenciaTamanho)


    ## Inclusão de números na senha
    incluirNumeros = verificacaoSN(f"Incluir números[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")
    if incluirNumeros in "S":
        digitos += randomizar(num, conferenciaTamanho)


    ## Inclusão de símbolos na senha
    incluirSimbolos = verificacaoSN(f"Incluir símbolos[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")
    if incluirSimbolos in "S":
        digitos += randomizar(simbolos, conferenciaTamanho)

    ## Embaralhar a senha
    digitos = random.sample(digitos, conferenciaTamanho)   # Gera uma *lista* embaralhada

    print("Sua senha gerada é: ", end="")
    
    senha = ""

    Colors.corVerde()       # Define a cor verde
    for c in digitos:
        print(f"{Colors.corVerde()}{c}{Colors.limpar()}", end="") 
        senha += c

    SalvaDado(nome_arquivo, "\nSenha: ", senha)