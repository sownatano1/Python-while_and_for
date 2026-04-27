media = 0

for n in range(1, 6):
    numero = int(input("Digite um numero: "))
    
    if(numero > 0):
        print(f"{numero} é um numero positivo")
    elif(numero < 0):
        print(f"{numero} é um numero negativo")
    else:
        print(f"{numero} é um numero neutro")