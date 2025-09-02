def area(l, c):
    print(f'A área de um terreno {l}x{c} é de {l * c:.1f}m².')


titulo = 'Controle de Terrenos'
print(titulo)
print('-' * len(titulo))
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
