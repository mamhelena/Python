import time
import random

nome = input("Digite seu nome: ")
print("Olá, " +nome, " esse é o jogo da Forca")
time.sleep(1)
print("Começando...")
time.sleep(1)

listaPalavras = ("estudos", "python", "programação", "desenvolvimento")


numeroRandomico = random.randint(0, len(listaPalavras) - 1)
palavraEscolhida = listaPalavras[numeroRandomico]

palavra = palavraEscolhida
escolhas = ''
turnos = 10

while turnos > 0:
    falha = 0

    for char in palavra:
        if(char in escolhas):
            print(char),
        else:
            print("_"),
            falha+=1
            
    if falha==0:
        print("\n Você venceu!")
        break
    print

    escolha = input("Escolha uma letra: ")

    escolhas +=escolha

    if escolha not in palavra:
        turnos-=1
        print("Deu ruim\n")
        print("Você tem mais ", turnos, " de chances")


        if turnos==0:
            print("Suas chances acabaram - você perdeu!!!")
            
