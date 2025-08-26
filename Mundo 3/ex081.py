numeros = []
while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')
