from datetime import date
ano_nascimento = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - ano_nascimento
print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano}.')
if idade < 18:
    if 18 - idade == 1:
        print(f'Ainda falta 1 ano para o alistamento.')
    else:
        print(f'Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {ano_nascimento + 18}.')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    if idade == 19:
        print('Você ja deveria ter se alisatado há 1 ano')
    else:
        print(f'Você ja deveria ter se alisatado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {ano_nascimento + 18}')
