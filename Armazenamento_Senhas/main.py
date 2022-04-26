import FunctionsAS
import Colors

print(f"O que você deseja realizar?\n[ 1 ] Armazenar senha\n[ 2 ] Editar senha armazenada\n[ 3 ] Deletar senha armazenada\n[ 4 ] Visualizar senha armazenada\n[ 5 ] Para {Colors.corVermelho()}fechar{Colors.limpar()} o programa")

Acao = FunctionsAS.inteiro(f"\nDigite a ação desejada[{Colors.corVerde()}1-5{Colors.limpar()}]: ")
while Acao > 5 or Acao < 1:
   Acao = FunctionsAS.inteiro(f"\nDigite a ação desejada[{Colors.corVerde()}1-5{Colors.limpar()}]: ") 

while True:
    if Acao == 1:
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
        
        else:
            print(f"Já há um arquivo com nome '{Colors.corAmarelo()}{Nome_Arquivo}{Colors.limpar()}'.")
            ArquivoExistenteEdit = FunctionsAS.inteiro("[ 1 ] Editar login e senha\n[ 2 ] Ver login e senha\nDigite a ação desejada: ")

            while ArquivoExistenteEdit < 1 or ArquivoExistenteEdit > 2:
                ArquivoExistenteEdit = FunctionsAS.inteiro("[ 1 ] Editar login e senha\n[ 2 ] Ver login e senha\nDigite a ação desejada: ")

            if ArquivoExistenteEdit == 1:
                Acao = 2
                continue
            
            else:
                Acao = 4        # Ver senha
                continue


    elif Acao == 2:
        titulo = "Editar senha armazenada"
        FunctionsAS.TabularTitulo(titulo)

        while True:
            Nome_Arquivo = str(input("Esta senha é referente a que? ")).upper().strip()

            if not FunctionsAS.ArquivoExiste(Nome_Arquivo):
                print(f"O arquivo referente a '{Colors.corAmarelo()}{Nome_Arquivo}{Colors.limpar()}' não existe...")
                ArquivoExistenteEdit = FunctionsAS.inteiro("\n[ 1 ] Digitar novamente\n[ 2 ] Criar login e senha\nDigite a ação desejada: ")

                while ArquivoExistenteEdit < 1 or ArquivoExistenteEdit > 2:
                    ArquivoExistenteEdit = FunctionsAS.inteiro("\n[ 1 ] Digitar novamente\n[ 2 ] Criar login e senha\nDigite a ação desejada: ")

                if ArquivoExistenteEdit == 1:
                    continue

                else:           # ArquivoExistenteEdit == 2
                    Acao = 1
                    break

            else:           # if FunctionsAS.ArquivoExiste == True
                break

        if Acao == 1:
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


    elif Acao == 3:
        titulo = "Deletar senha armazenada"
        FunctionsAS.TabularTitulo(titulo)

        while True:
            Nome_Arquivo = str(input("Esta senha é referente a que? ")).upper().strip()
            ArquivoExistenteDel = 0

            if not FunctionsAS.ArquivoExiste(Nome_Arquivo):
                print(f"O arquivo referente a '{Colors.corAmarelo()}{Nome_Arquivo}{Colors.limpar()}' não existe...")
                
                ArquivoExistenteDel = FunctionsAS.inteiro("\n[ 1 ] Digitar novamente\n[ 2 ] Sair\nDigite a ação desejada: ")

                while ArquivoExistenteDel < 1 or ArquivoExistenteDel > 2:
                    ArquivoExistenteDel = FunctionsAS.inteiro("\n[ 1 ] Digitar novamente\n[ 2 ] Sair\nDigite a ação desejada: ")

                if ArquivoExistenteDel == 1:
                    continue
                
                else:
                    break
                    
            else:       # if FunctionsAS.ArquivoExiste == True
                break


        if ArquivoExistenteDel == 2:
            break

        VerificacaoDeletar = FunctionsAS.verificacaoSN(f"Tem certeza que deseja {Colors.corVermelho()}excluir{Colors.limpar()}[{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")

        if VerificacaoDeletar in "S":
            import os
            os.remove(Nome_Arquivo + ".txt")

            print(f"Arquivo '{Colors.corAmarelo()}{Nome_Arquivo}{Colors.limpar()}' {Colors.corVermelho()}exclúido{Colors.limpar()} com sucesso!")
            break


    elif Acao == 4:
        titulo = "Visualizar Senha"
        FunctionsAS.TabularTitulo(titulo)

        while True:
            Nome_Arquivo = str(input("Esta senha é referente a que? ")).upper().strip()
            ArquivoExistenteDel = 0

            if not FunctionsAS.ArquivoExiste(Nome_Arquivo):
                print(f"O arquivo referente a '{Colors.corAmarelo()}{Nome_Arquivo}{Colors.limpar()}' não existe...")
            
                ArquivoExistenteDel = FunctionsAS.inteiro("\n[ 1 ] Digitar novamente\n[ 2 ] Armazenar senha\nDigite a ação desejada: ")

                while ArquivoExistenteDel < 1 or ArquivoExistenteDel > 2:
                    ArquivoExistenteDel = FunctionsAS.inteiro("\n[ 1 ] Digitar novamente\n[ 2 ] Armazenar senha\nDigite a ação desejada: ")

                if ArquivoExistenteDel == 1:
                    continue
                
                else:
                    break
            
            else:
                if ArquivoExistenteDel == 2:
                    Acao = 1
                    break

                FunctionsAS.LerArquivo(Nome_Arquivo)
                break

        if Acao == 1:
            continue


    elif Acao == 5:
        import time

        print("Finalizando", end="")
        for c in range(0, 5):
            print(".", end="", flush=True)
            time.sleep(0.5)

        break
    
    print("")
    print(f"{Colors.corVioleta()}~" * 50 + f"{Colors.limpar()}")
    print(f"O que você deseja realizar?\n[ 1 ] Armazenar senha\n[ 2 ] Editar senha armazenada\n[ 3 ] Deletar senha armazenada\n[ 4 ] Visualizar senha armazenada\n[ 5 ] Para {Colors.corVermelho()}fechar{Colors.limpar()} o programa")

    Acao = FunctionsAS.inteiro(f"\nDigite a ação desejada[{Colors.corVerde()}1-5{Colors.limpar()}]: ")
    while Acao > 5 or Acao < 1:
        Acao = FunctionsAS.inteiro(f"\nDigite a ação desejada[{Colors.corVerde()}1-5{Colors.limpar()}]: ") 

print(f"\n\nO programa acabou e todas as tarefas foram executadas corretamente.{Colors.corVioleta()}Vejo você em breve! :D{Colors.limpar()}\n\n")