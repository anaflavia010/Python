preço = float(input('Qual o preço do produto? R$'))
desconto = preço - (preço * 5 / 100)
print(f'O produto que custava R${preço:.2f}, na promoção com desconto de 5% vai custar R${desconto:.2f}')