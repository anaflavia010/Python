alunos = []
al = []
while True:
    al.append(str(input('Nome: ')).strip())
    al.append(float(input('Nota 1: ')))
    al.append(float(input('Nota 2: ')))
    alunos.append(al[:])
    al.clear()
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        print('=-' * 30)
        break
print(f'{"Nº":<5} {"NOME":<15} {"MÉDIA":<30}')
print('=' * 30)
for p, aluno in enumerate(alunos):
    print(f'{p:<5} {aluno[0]:<15} {((aluno[1] + aluno[2]) / 2):<30.2f}')
print('=' * 30)
while True:
    m = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if m == 999:
        print('=-' * 25)
        print('PROGRAMA FINALIZADO!')
        print('VOLTE SEMPRE!')
        break
    else:
        print(f'As notas de {alunos[m][0]} são {alunos[m][1:]}')
        print('=' * 50)

