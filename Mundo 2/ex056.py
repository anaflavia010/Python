somaidade = media = homem_velho = nome_velho = mulher20 = 0
for i in range(1, 5):
    print('===== {i}ª PESSOA =====')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        homem_velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > homem_velho:
        homem_velho = idade
        nome_velho = nome
    if sexo in 'Fm' and idade < 20:
        mulher20 += 1
media = somaidade/4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {homem_velho} anos e se chama {nome_velho}')
print(f'Ao todo são {mulher20} mullheres com menos de 20 anos')