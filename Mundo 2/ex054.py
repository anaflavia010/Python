from datetime import date
maior = menor = 0
atual = date.today().year
for i in range(1, 8):
    nascimento = int(input(f'Em que ano a {i}º pessoa nasceu: '))
    idade = atual - nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
