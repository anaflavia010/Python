jogador = {}
gols = []
p = 1
jogador['Nome'] = input('Nome: ')
partidas = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
for i in range(0, partidas):
    gols.append(int(input(f'    Quantos gols na partida {i}? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for p, gol in enumerate(jogador['Gols']):
    print(f'    => Na parida {p}, fez {gol} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
