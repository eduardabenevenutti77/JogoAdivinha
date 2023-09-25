#Faça um programa em que o computador pense num número de 0 a 10, e o jogador vai adivinhar até acertar.
#Mostre na tela a quantidade de palpites gastos para vencer o desafio

palpite = 0
from random import randint

pensaNumero = randint(0,100)

#sorteio = random.choice(pensaNumero)
c = False
while not c:
    numUsuario = int(input("\n Informe um valor que esteja em 0 à 100 => "))
    palpite += 1
    if numUsuario == pensaNumero:
        c = True
    else:
        if numUsuario < pensaNumero:
            print(" O valor é maior, tente novamente....")
        elif numUsuario > pensaNumero:
            print(" O valor é menor, tente novamente....")
print("\n Foram necessário {} palpites para acertar o número escolhido pelo computador!!".format(palpite))
