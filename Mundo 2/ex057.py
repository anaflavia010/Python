sexo = str(input('Infome seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ')
print(f'Sexo {sexo} registrado com sucesso')