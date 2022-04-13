import random
tamanho = 8     # 8 caracteres
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letrasM = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
simbolos = '~`! @#$%^&*()_-+={]|\:;<,>.?/'
digitos = letras + letrasM + num + simbolos
senha = ''
for c in range(tamanho):
    senha += random.choice(digitos)     # Randomiza os digitos
random.sample(senha, len(senha))    # Embaralha a senha gerada acima
print(f'Sua senha é: {senha} ')
