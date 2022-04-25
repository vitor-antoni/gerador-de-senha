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

while True:
    if acao == 1:
        titulo = "Armazenar senha"
        FunctionsAS.TabularTitulo(titulo)

        Nome_Arquivo = str(input("Esta senha é referente a que? ")).upper().strip()

        if not(FunctionsAS.ArquivoExiste(Nome_Arquivo)):
            FunctionsAS.CriaArquivo(Nome_Arquivo)

            login = str(input("Digite aqui o seu login: "))
            FunctionsAS.SalvaDado(Nome_Arquivo, "Login: ", login)

            # Geração de senha
            quest_gerar = FunctionsAS.verificacaoSN(f"\nDeseja gerar uma senha[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")

            if quest_gerar in "S":
                FunctionsAS.GerarSenha(Nome_Arquivo)

            else:
                senha = str(input("Digite aqui sua senha: "))
                FunctionsAS.SalvaDado(Nome_Arquivo, "\nSenha: ", senha)

            print(f"\n\n{Colors.corVerde()}Seu login e senha foram armazenados com sucesso! {Colors.limpar()}")
            break
        
        else:
            print(f"Já há um arquivo com nome '{Colors.corAmarelo()}{Nome_Arquivo}{Colors.limpar()}'.")
            ArquivoExistenteEdit = int(input("""[ 1 ] Editar login e senha
[ 2 ] Ver login e senha
            \nDigite a ação desejada: """))

            while ArquivoExistenteEdit < 1 or ArquivoExistenteEdit > 2:
                ArquivoExistenteEdit = int(input("""[ 1 ] Editar login e senha
[ 2 ] Ver login e senha
            \nDigite a ação desejada: """))

            if ArquivoExistenteEdit == 1:
                acao = 2
                continue
            
            else:
                acao = 4        # Ver senha
                continue


    elif acao == 2:
        titulo = "Editar senha armazenada"
        FunctionsAS.TabularTitulo(titulo)

        while True:
            Nome_Arquivo = str(input("\nEsta senha é referente a que? ")).upper().strip()

            if not FunctionsAS.ArquivoExiste(Nome_Arquivo):
                print(f"O arquivo referente a '{Colors.corAmarelo()}{Nome_Arquivo}{Colors.limpar()}' não existe...")
                ArquivoExistenteEdit = int(input("""\n[ 1 ] Digitar novamente
[ 2 ] Criar login e senha
                \nDigite a ação desejada: """))

                while ArquivoExistenteEdit < 1 or ArquivoExistenteEdit > 2:
                    ArquivoExistenteEdit = int(input("""[ 1 ] Digitar novamente
[ 2 ] Criar login e senha
                \nDigite a ação desejada: """))

                if ArquivoExistenteEdit == 1:
                    continue

                else:           # ArquivoExistenteEdit == 2
                    acao = 1
                    break

            else:           # if FunctionsAS.ArquivoExiste == True
                break
       
        if acao == 1:
            continue


        # Apagar as informações do arquivo antigo
        FunctionsAS.DeletaDado(Nome_Arquivo)    

        login = str(input("Digite aqui o seu novo login: "))
        FunctionsAS.SalvaDado(Nome_Arquivo, "Login: ", login)

        # Geração de senha
        quest_gerar = FunctionsAS.verificacaoSN(f"\nDeseja gerar uma senha[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")

        if quest_gerar in "S":
            FunctionsAS.GerarSenha(Nome_Arquivo)

        else:
            senha = str(input("Digite aqui sua nova senha: "))
            FunctionsAS.SalvaDado(Nome_Arquivo, "\nSenha: ", senha)

        print(f"{Colors.corVerde()}\n\nSeu login e senha foram alterados e armazenados com sucesso! {Colors.limpar()}")

        break


    elif acao == 3:
        titulo = "Deletar senha armazenada"
        FunctionsAS.TabularTitulo(titulo)

        Nome_Arquivo = str(input("Esta senha é referente a que? ")).upper().strip()

        while not FunctionsAS.ArquivoExiste(Nome_Arquivo):
            print(f"O arquivo referente a '{Colors.corAmarelo()}{Nome_Arquivo}{Colors.limpar()}' não existe...")
            Nome_Arquivo = str(input("Esta senha é referente a que? ")).upper().strip()
