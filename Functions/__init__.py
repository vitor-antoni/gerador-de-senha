def conferirTamanho(tam):
    try:
        import Colors
        while tam < 8:
            print(f"Senha {Colors.corVermelho()}fraca{Colors.limpar()} demais!")
            tam = int(input(f"Digite o tamanho da senha {Colors.corVermelho()}(mín: 8){Colors.limpar()}: "))
    
    except Exception as error:
        print(f"Houve um erro em conferir o tamanho: {error.__class__}")
    
    else:
        if tam >= 8 and tam < 10:
            print(f"{Colors.corAmarelo()}Tamanho OK!{Colors.limpar()}\n")
        else:
            print(f"{Colors.corVerde()}Tamanho excelente!{Colors.limpar()}\n")
        return tam


def randomizar(variavel, tam=8):
    import random

    gerado = ""
    for c in range(0, tam):
        gerado += random.choice(variavel)
    return gerado


def verificacaoSN(pergunta=""):
    verf = str(input(pergunta)).strip().upper()[0]
    
    while verf not in "SN":
        print("Digite novamente...")
        verf = str(input(pergunta)).strip().upper()[0]
    return verf