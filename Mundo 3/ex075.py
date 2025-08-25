tupla = tuple(int(input(f'Digite o {i}º número: ')) for i in range(1, 5))
par = [0]
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado e nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
