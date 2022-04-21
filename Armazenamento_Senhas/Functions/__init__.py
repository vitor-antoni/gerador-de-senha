def ArquivoExiste(nome_arquivo):
    try:
        arquivo = open(nome_arquivo + ".txt", "rt")
    except Exception as error:
        return False
    else:
        return True