aluno = {}
aluno['Nome'] = input('Nome: ').strip()
aluno['Média'] = float(input(f'Média de {aluno['Nome']}: '))
if aluno['Média'] >= 7.0:
    aluno['Situação'] = 'Aprovado'
elif 5.0 <= aluno['Média'] < 7.0:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('=-' * 15)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
