matriz = [[], [], []]
soma_pares = soma_coluna3 = maior_linha2 = 0
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i].append(n)
for i in range(0, 3):
    soma_coluna3 += matriz[i][2]
maior_linha2 = max(matriz[1])
print('=-' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna3}.')
print(f'O maior valor da segunda linha é {maior_linha2}.')
