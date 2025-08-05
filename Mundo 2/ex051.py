print('-='*10)
print('10 termos de uma PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for i in range(primeiro, decimo + razão, razão):
    print(i, end=' -> ')
print('ACABOU')
