import FunctionsAS
import Colors

## Último edit: linha 17


Nome_Arquivo = str(input("Esta senha é referente a que? ")).upper().strip()

if not(FunctionsAS.ArquivoExiste(Nome_Arquivo)):
    FunctionsAS.CriaArquivo(Nome_Arquivo)

else:
    edit = str(input(f"Deseja editar seu login e senha [{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")).upper().strip()[0]
    while edit not in "SN":
        edit = str(input(f"Deseja editar seu login e senha [{Colors.corVerde()}S{Colors.limpar()}/{Colors.corVermelho()}N{Colors.limpar()}]? ")).upper().strip()[0]
    if edit in "S":
        FunctionsAS.DeletaDado(Nome_Arquivo)    
        login = str(input("Digite aqui o seu novo login: "))
        FunctionsAS.EditaDado(Nome_Arquivo, "Login: ", login)

        senha = str(input("Digite aqui sua nova senha: "))
        FunctionsAS.EditaDado(Nome_Arquivo, "\nSenha: ", senha)



login = str(input("Digite aqui o seu login: "))
FunctionsAS.SalvaDado(Nome_Arquivo, "Login: ", login)

senha = str(input("Digite aqui sua senha: "))
FunctionsAS.SalvaDado(Nome_Arquivo, "\nSenha: ", senha)