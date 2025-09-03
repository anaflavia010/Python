def ficha(nomes='<desconhecido>', gols=0):
    return print(f'O jogador {nomes} fez {gols} gols no campeonato.')

print('=' * 3)
nome = str(input('Nome do jogador: ')).strip()
gol = str(input('Número de gols: ')).strip()
if nome != '' and not gol.isnumeric():
    ficha(nome)
elif gol.isnumeric() and nome == '':
    ficha(gols=int(gol))
elif nome == '' and not gol.isnumeric():
    ficha()
else:
    ficha(nome, int(gol))
