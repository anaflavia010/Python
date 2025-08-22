maior18 = homem = mulher20 = 0
while True:
    print('=-' * 15)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('=-' * 15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('=-' * 15)
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        continue
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo tivemos {homem} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')