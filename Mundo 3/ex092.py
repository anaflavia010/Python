from datetime import date
funcionário = {}
funcionário['Nome'] = input('Nome: ').strip()
nascimento = int(input('Ano de nascimento: '))
funcionário['Idade'] = date.today().year - nascimento
funcionário['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if funcionário['CTPS'] != 0:
    funcionário['Ano Contratação'] = int(input('Ano de contratação: '))
    funcionário['Salário'] = float(input('Salário: R$'))
    funcionário['Aposentadoria'] = (funcionário['Ano Contratação'] + 35) - nascimento
print('=-' * 30)
for k, v in funcionário.items():
    print(f'    - {k} tem o valor {v}')
