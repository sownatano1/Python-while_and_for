import os
import time

exit = 1
resposta = ""

def LimparTerminal():
    os.system('cls' if os.name == "nt" else 'clear')

while(exit != 0):
    
    LimparTerminal()
    print("Menu")
    print("Digite 'E' para entrar")
    print("Digite 'C' para acessar as configurações")
    print("Digite 'S' para sair")
    resposta = input()
        
    if (resposta == "E", "e"):
        LimparTerminal()
        print("Menu Principal")
        print("Digite 'M' para voltar para o Menu")
        resposta = input()
            
    elif (resposta == "C", "c"):
        LimparTerminal()
        print("Menu de Configurações")
        print("Digite 'M' para voltar para o Menu")
        resposta = input()
        
    elif (resposta == "S", "s"):
        LimparTerminal()
        print("Você saiu do Menu")
        exit = 0

    else:
        LimparTerminal()
        print("Menu incorreto")
        print("Digite denovo")
        time.sleep(2)