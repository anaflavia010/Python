largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura
qtda_tinta = area / 2
print(f'Sua parede tem a dimensão de {largura}X{altura} e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisa de {qtda_tinta}l de tinta')