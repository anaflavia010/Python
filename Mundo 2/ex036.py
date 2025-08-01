valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestação = valor / (anos * 12)
minino = salario * 30 / 100
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos, a prestação será de {prestação:.2f}')
if prestação <= minino:
    print('Empréstimo pode ser CONCEDIDO!')
else: 
    print('Empréstimo NEGADO!')
    