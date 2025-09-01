from random import randint
from time import sleep
jogadores = {}
p = 1
print('Valores sorteados:')
for i in range(0, 4):
    dado = int(randint(1, 6))
    jogadores[i + 1] = dado
for i in range(1, 5):
    print(f'O jogador{i} tirou {jogadores[i]} no dado.')
    sleep(0.8)
print('=-' * 17)
print(f'   {"=" * 2} {" RANK DOS JOGADORES ":^4} {"=" * 2}')
for i in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'    {p}º lugar: Jogador{i} com {jogadores[i]}')
    sleep(0.8)
    p += 1
