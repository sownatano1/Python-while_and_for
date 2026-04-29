senha = ""

while(senha != 1234):
    senha = int(input("Digite um numero: "))
    print("Senha incorreta!")
    if(senha == 1234):
        print("Senha correta!")
