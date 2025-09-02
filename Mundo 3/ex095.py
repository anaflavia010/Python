jogador = {}
campeonato = []
gols = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome: '))
    while True:
        p = input(f'Quantas partidas o {jogador["Nome"]} jogou? ')
        if p.isnumeric():
            break
        print('ERRO! Por favor, digite um valor válido!')
    partidas = int(p)
    gols.clear()
    for i in range(0, partidas):
        while True:
            gol = input(f'    Quantos gols na partida {i + 1}? ')
            if gol.isnumeric():
                break
            print('ERRO! Por favor, digite um valor válido!')
        gols.append(int(gol))
        jogador['Gols'] = gols[:]
        jogador['Total'] = sum(gols)
    campeonato.append(jogador.copy())
    while True:
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print(f'ERRO! Por favor, digite S ou N!')
    if continuar == 'N':
        break
print('=-' * 30)
print('cod ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('=' * 40)
for k, v in enumerate(campeonato):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    while True:
        print('=-' * 30)
        dados = input('Mostrar os dados de qual jogador? (999 interrompe): ')
        if dados.isnumeric():
            dados = int(dados)
            if 0 <= dados <= len(campeonato) - 1 or dados == 999:
                break
            print(f'ERRO! Não existe jogador com o código "{dados}"')
        else:
            print(f'ERRO! Não existe jogador com o código "{dados}"')
    if dados == 999:
        print('PROGRAMA FINALIZADO! VOLTE SEMPRE')
        break
    print(f'{" -- LEVANTAMENTO DO JOGADOR "} {campeonato[dados]["Nome"]}:')
    for pos, v in enumerate(campeonato[dados]['Gols']):
        print(f'    No jogo {pos + 1} fez {v} gols.')
