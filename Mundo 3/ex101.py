def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    print(f'Com {idade} anos: ', end='')
    if 18 <= idade <= 70:
        return print('VOTO OBRIGATÓRIO!')
    elif 16 <= idade <= 17 or idade > 70:
        return print('VOTO OPCIONAL!')
    else:
        return print(f'NÃO VOTA!')

print('=' * 30)
voto(ano = int(input('Em que ano você nasceu? ')))
