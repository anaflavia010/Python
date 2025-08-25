print('=' * 45)
print(f'{"LISTAGEM DE PREÇOS":^45}')
print('=' * 45)
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Trasferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<33} R${produtos[i + 1]:>7.2f}')
print('=' * 45)