media = 0
valores = []
continuar = True
while continuar:
    n = int(input('Digite um número: '))
    valores.append(n)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('\n\033[1;31mOpção inválida. Tente novamente!\033[m')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        continuar = False
media = sum(valores) / len(valores)
valores.sort()
print(f'Você digitou {len(valores)} e a média foi: {media}')
print(f'O maior valor é {valores[-1]} e o menor foi {valores[0]}')
