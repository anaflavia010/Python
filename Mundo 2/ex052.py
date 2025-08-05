print(f'{"Números Primos":=^40}\n')
num = int(input('Digite um número: '))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[1;33m', end=' ')
        cont += 1
    else:
        print('\033[1;31m', end=' ')
    print(i, end=' ')
print(f'\n\033[mO número {num} foi dividido {cont} vezes.')
if cont == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')