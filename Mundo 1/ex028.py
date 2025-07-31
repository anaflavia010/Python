from random import randint
from time import sleep

print('\033[0;33m-=\033[m' * 30)
print('\033[0;34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[0;33m-=\033[m' * 30)
computador = randint(0, 5)
jogador = int(input('Em que número eu pensei? '))
print('\033[0;35mPROCESSANDO...\033[m')
sleep(2)
if jogador == computador:
    print('\033[0;32mPARABÉNS! Você conseguiu me vencer!\033[m')
elif jogador > 5 or jogador < 0:
    if jogador > 5:
        print(f'\033[0;31mGANHEI! Você pensou em um número maior que o 5\033[m')
        print(f'\033[0;31mEu pensei no número {computador}!\033[m')
    else:
        print(f'\033[0;31mGANHEI! Você pensou em um número menor que o 0\033[m')
        print(f'\033[0;31mEu pensei no número {computador}!\033[m')
else:
    print(f'\033[0;31mGANHEI! Eu pensei no número {computador} e não no {jogador}!\033[m')
