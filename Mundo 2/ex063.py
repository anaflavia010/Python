print('=-' * 15)
print('SEQUÊNCIA DE FIBONACCI')
print('=-' * 15)
n = int(input('Quantos termos você deseja mostrar? '))
cont = 1
prim = 0
segu = 1
prox = 0
if n == 1:
    print(f'{prim}', end='')
while cont < n:
    if cont == 1:
        print(f'{prim} → {segu}', end='')
        prox = prim + segu
    else:
        print(f' → {prox}', end='')
        prim = segu
        segu = prox
        prox = prim + segu
    cont += 1
print(' → ', end='FIM')
