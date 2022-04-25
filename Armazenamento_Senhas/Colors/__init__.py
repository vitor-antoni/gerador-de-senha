def corVermelho():
    cor = {"vermelho":"\033[1;31m"}
    return f"{cor['vermelho']}"

def corVerde():
    cor = {"verde": "\033[1;32m"}
    return f"{cor['verde']}"

def corAmarelo():
    cor = {"amarelo": "\033[1;33m"}
    return f"{cor['amarelo']}"

def corVioleta():
    cor = {"violeta": "\033[1;35m"}
    return f"{cor['violeta']}"


def limpar():
    clean = {"limpar": "\033[m"}
    return f"{clean['limpar']}"
