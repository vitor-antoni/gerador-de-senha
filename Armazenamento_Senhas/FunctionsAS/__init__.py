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
        print(f"{Colors.corVermelho()}Sucesso na criação do arquivo!{Colors.limpar()}")
        arquivo.close()