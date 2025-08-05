maior = menor = 0
for i in range(1, 6):
    peso = float(input(f'Peso da {i}º pessoa: '))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é: {maior}Kg')
print(f'O menor peso é: {menor}Kg')
