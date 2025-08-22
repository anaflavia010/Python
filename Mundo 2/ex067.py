print('=-' * 15)
print(f'{"TABUADA":^30}')
print('=-' * 15)
while True:
    n = int(input('Deseja ver a tabuada de qual número? '))
    print('=' * 20)
    if n >= 0:
        print(f'TABUADA DE {n}: ')
        print('=' * 20)
        for i in range(1, 11):
            print(f'{n} x {i} = {i * n}')
        print('=' * 20)
    else:
        break
print('Programa finalizado!')
print('Volte sempre!')
