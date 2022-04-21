from Gerador_Senha import Colors

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
        print(f"Houve um erro para criar o arquivo: {Colors.corVermelho}{error}{Colors.limpar()}")
    else:
        print("{Colors.corVerde()}Sucesso na criação do arquivo!{Colors.limpar()}")