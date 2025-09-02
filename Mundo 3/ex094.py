pessoa = {}
grupo = []
mulheres = []
a_media = []
soma_idade = 0
while True:
    nome = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'MF':
            break
        print(f'ERRO! Por favor, digite apenas M ou F.')
    while True:
        idade = input('Idade: ')
        if idade.isnumeric():
                break
        print(f'ERRO! Por favor, digite uma idade válida.')
    pessoa['Nome'] = nome
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = int(idade)
    grupo.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print(f'ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
for individuo in grupo:
    for k, v in individuo.items():
        if k == 'Idade':
            soma_idade += v
media = soma_idade / len(grupo)
for individuo in grupo:
    for k, v in individuo.items():
        if k == 'Sexo' and v == 'F':
            mulheres.append(individuo.get('Nome'))
for individuo in grupo:
    for k, v in individuo.items():
        if k == 'Idade' and v > media:
            a_media.append(individuo.copy())
print('=-' * 30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
print(f'B) Média de idade é de {media:.1f} anos')
if len(mulheres) == 0:
    print('C) Nenhuma mulher foi cadastrada!')
else:
    print(f'C) As mulheres cadastradas foram {mulheres}')
print('D) Lista das pessoas que estão acima da média: ')
for i in grupo:
    if i['Idade'] >= media:
        print('   ', end='')
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')