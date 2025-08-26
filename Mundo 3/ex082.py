numeros = []
impar = []
par = []
while True:
    numeros.append(int(input('Digite um número: ')))
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
for valor in numeros:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'A lista completa é: {numeros}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')
