total = mais_mil = produto_barato = 0
cont = 1
valor_barato = ''
print('-' * 30)
print(f'{"LOJA SUPER BARATÃO":^30}')
while True:
    nome = input('Nome do produto: ').strip()
    preço = float(input('Preço: R$'))
    total += preço
    if preço > 1000:
        mais_mil += 1
    if cont == 1 or preço < produto_barato:
        produto_barato = preço
        valor_barato = nome
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{" FIM DO PROGRAMA ":=^40}')
print(f'Total da compra foi: R${total:.2f}')
print(f'Temos {mais_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {valor_barato} que custa R${produto_barato:.2f}')
