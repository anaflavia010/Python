principal = []
pessoa = []
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')).strip())
    pessoa.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        elif pessoa[1] < menor:
            menor = pessoa[1]
    principal.append(pessoa[:])
    pessoa.clear()
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
print('=-' * 30)
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for i in principal:
    if i[1] == maior:
        print(i[0], end=', ')
print(f'\nO menor peso foi de {menor}Kg. Peso de', end=' ')
for i in principal:
    if i[1] == menor:
        print(i[0], end=', ')
        