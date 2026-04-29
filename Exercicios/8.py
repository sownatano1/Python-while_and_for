numero = int(input("Digite um numero: "))
n1, n2 = 0, 1

for n in range(numero):
    n1, n2 = n2, n1+n2
    print(n1)