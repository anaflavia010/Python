km = float(input('Qual a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de {km}Km.')
if km > 200:
    valor = float(km * 0.45)
    print(f'O preço da viagem será: R${valor:.2f} ')
else:
    valor = float(km * 0.50)
    print(f'O preço da viagem será: R${valor:.2f}')
