from random import randint
from time import sleep
jogo = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
pc = randint(0,2)
jogador = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*15)
print(f'Jogador escolheu {jogo[jogador]}')
print(f'Computador escolheu {jogo[pc]}')
print('-='*15)
if pc == jogador:
    print('EMPATE')
elif pc == 0:
    if jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2:
    if jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 0:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
