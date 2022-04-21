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