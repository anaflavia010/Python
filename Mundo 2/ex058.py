from random import randint
computador = randint(0, 10)
jogador = -1
cont = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
while jogador != computador:
    jogador = int(input('Qual é o seu palpite? '))
    cont += 1
    if jogador != computador:
      if jogador > computador:
        print('Menos... Tente mais uma vez')
      else:
        print('Mais... Tente mais uma vez')
    else:
        print(f'\033[36mAcertou o número com {cont} tentativas. Parabéns!\033[m')
