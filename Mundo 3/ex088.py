from random import randint
from time import sleep
print('='*30)
print(f'{" JOGA NA MEGA SENA ":^30}')
print('='*30)
jogos = []
sorteio = []
j = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0, j):
    while len(sorteio) < 6:
        n = randint(1, 60)
        if n not in sorteio:
            sorteio.append(n)
    jogos.append(sorteio[:])
    sorteio.clear()
print('=-' * 3, f' SORTEANDO {j} JOGOS ', '=-' * 3)
for i in range(0, len(jogos)):
    sleep(1)
    print(f'Jogo {i + 1}: {sorted(jogos[i])}')
sleep(1)
print('=-' * 3, ' < BOA SORTE! > ', '=-' * 3)