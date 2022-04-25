import FunctionsAS
import Colors

print(f"""O que você deseja realizar? 
[ 1 ] Armazenar senha
[ 2 ] Editar senha armazenada
[ 3 ] Deletar senha armazenada
[ 4 ] Visualizar senha armazenada
[ 5 ] Para {Colors.corVermelho()}fechar{Colors.limpar()} o programa""")

acao = int(input(f"\nDigite a ação desejada[{Colors.corVerde()}1-5{Colors.limpar()}]: "))
while acao > 5 or acao < 1:
   acao = int(input(f"Digite a ação desejada[{Colors.corVerde()}1-5{Colors.limpar()}]: ")) 

if acao == 1:
    Nome_Arquivo = str(input("\nEsta senha é referente a que? ")).upper().strip()

    if not(FunctionsAS.ArquivoExiste(Nome_Arquivo)):
        FunctionsAS.CriaArquivo(Nome_Arquivo)

        login = str(input("Digite aqui o seu login: "))
        FunctionsAS.SalvaDado(Nome_Arquivo, "Login: ", login)

        # Geração de senha
        quest_gerar = FunctionsAS.verificacaoSN(f"\nDeseja gerar uma senha[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")

        if quest_gerar in "S":
            FunctionsAS.gerarSenha(Nome_Arquivo)

        else:
            senha = str(input("Digite aqui sua senha: "))
            FunctionsAS.SalvaDado(Nome_Arquivo, "\nSenha: ", senha)

        print(f"{Colors.corVerde()}Seu login e senha foram armazenados com sucesso! {Colors.limpar()}")

if acao == 2:
    Nome_Arquivo = str(input("\nEsta senha é referente a que? ")).upper().strip()

    while not FunctionsAS.ArquivoExiste:
        print(f"O arquivo referente a '{Nome_Arquivo}' não existe...")
        # Apagar as informações do arquivo antigo
        FunctionsAS.DeletaDado(Nome_Arquivo)    

        login = str(input("\nDigite aqui o seu novo login: "))
        FunctionsAS.SalvaDado(Nome_Arquivo, "Login: ", login)

        # Geração de senha
        quest_gerar = FunctionsAS.verificacaoSN(f"\nDeseja gerar uma senha[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")

        if quest_gerar in "S":
            FunctionsAS.GerarSenha(Nome_Arquivo)

        else:
            senha = str(input("Digite aqui sua nova senha: "))
            FunctionsAS.SalvaDado(Nome_Arquivo, "\nSenha: ", senha)

        print(f"{Colors.corVerde()}\n\nSeu login e senha foram alterados e armazenados com sucesso! {Colors.limpar()}")

