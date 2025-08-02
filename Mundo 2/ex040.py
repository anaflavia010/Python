num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
media = (num1 + num2) / 2
print(f'Tirando {num1} e {num2}, a média do aluno é: {media:.2f}')
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO!')
else:
    print('O aluno está APROVADO!')
