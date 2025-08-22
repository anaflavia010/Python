print('='*30)
print(f'{"BANO CEV":^30}')
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
cedula50 = valor // 50
valor %=  50
cedula20 = valor // 20
valor %= 20
cedula5 = valor // 5
valor %= 5
cedula10 = valor // 10
valor %= 10
cedula1 = valor // 1
if cedula50 >= 1:
    print(f'Total de {cedula50} cédulas de R$50')
if cedula20 >= 1:
    print(f'Total de {cedula20} cédulas de R$20')
if cedula10 >= 1:
    print(f'Total de {cedula10} cédulas de R$10')
if cedula5 >= 1: 
    print(f'Total de {cedula5} cédulas de R$5')
if cedula1 >= 1:
    print(f'Total de {cedula1} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha uma bom!')