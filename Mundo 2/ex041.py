from datetime import date
ano_nascimento = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - ano_nascimento
print('O atleta tem {idade} anos.')
if idade <= 9:
    print(f'Classificação: MIRIM.')
elif idade <= 14:
    print(f'Classificação: INFANTIL.')
elif idade <= 19:
    print(f'Classificação: JÚNIOR.')
elif idade <= 25:
    print(f'Classificação: SÊNIOR.')
else:
    print(f'Classificação: MASTER.')
