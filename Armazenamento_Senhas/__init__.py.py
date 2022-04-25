import FunctionsAS
import Colors


Nome_Arquivo = str(input("Esta senha é referente a que? ")).upper().strip()

if not(FunctionsAS.ArquivoExiste(Nome_Arquivo)):
    FunctionsAS.CriaArquivo(Nome_Arquivo)

    login = str(input("Digite aqui o seu login: "))
    FunctionsAS.SalvaDado(Nome_Arquivo, "Login: ", login)

    senha = str(input("Digite aqui sua senha: "))
    FunctionsAS.SalvaDado(Nome_Arquivo, "\nSenha: ", senha)

    print(f"{Colors.corVerde()}Seu login e senha foram armazenados com sucesso! {Colors.limpar()}")

else:
    edit = FunctionsAS.verificacaoSN(f"\nDeseja editar seu login e senha [{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")

    if edit in "S":
        # Deleta os dados armazenados
        FunctionsAS.DeletaDado(Nome_Arquivo)    

        login = str(input("\nDigite aqui o seu novo login: "))
        FunctionsAS.SalvaDado(Nome_Arquivo, "Login: ", login)

        # Geração de senha
        quest_gerar = FunctionsAS.verificacaoSN(f"\nDeseja gerar uma senha[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")

        if quest_gerar in "S":
            import random

            letras = 'abcdefghijklmnopqrstuvwxyz' 
            letrasM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            num = '1234567890'
            simbolos = '~`!@#$%^&*()_-+={]|\:;<,>.?/'

            digitos = ""

            tamanho = int(input(f"Digite o tamanho da senha {Colors.corVermelho()}(min: 8){Colors.limpar()}: "))
            conferenciaTamanho = FunctionsAS.conferirTamanho(tamanho)

            ## Inclusão de letras na senha
            incluirLetras = FunctionsAS.verificacaoSN(f"Incluir letras[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")
            if incluirLetras in "S":
                digitos += FunctionsAS.randomizar(letras, conferenciaTamanho)


            ## Inclusão de letras maiúsculas na senha
            incluirLetrasM = FunctionsAS.verificacaoSN(f"Incluir letras maiúsculas[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")
            if incluirLetrasM in "S":
                digitos += FunctionsAS.randomizar(letrasM, conferenciaTamanho)


            ## Inclusão de números na senha
            incluirNumeros = FunctionsAS.verificacaoSN(f"Incluir números[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")
            if incluirNumeros in "S":
                digitos += FunctionsAS.randomizar(num, conferenciaTamanho)


            ## Inclusão de símbolos na senha
            incluirSimbolos = FunctionsAS.verificacaoSN(f"Incluir símbolos[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")
            if incluirSimbolos in "S":
                digitos += FunctionsAS.randomizar(simbolos, conferenciaTamanho)

            ## Embaralhar a senha
            digitos = random.sample(digitos, conferenciaTamanho)   # Gera uma *lista* embaralhada

            print("Sua senha gerada é: ", end="")
            
            senha = ""

            Colors.corVerde()       # Define a cor verde
            for c in digitos:
                print(f"{Colors.corVerde()}{c}{Colors.limpar()}", end="") 
                senha += c

            print(f"{Colors.corVerde()}\n\nSeu login e senha foram alterados e armazenados com sucesso! {Colors.limpar()}")

            FunctionsAS.SalvaDado(Nome_Arquivo, "\nSenha: ", senha)

        else:
            senha = str(input("Digite aqui sua nova senha: "))
            FunctionsAS.SalvaDado(Nome_Arquivo, "\nSenha: ", senha)

            print(f"{Colors.corVerde()}Seu login e senha foram alterados e armazenados com sucesso! {Colors.limpar()}")
