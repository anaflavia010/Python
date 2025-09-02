from random import randint
from time import sleep
def maior(numeros):
    print('=' * 60)
    mValor = max(numeros)
    print('Analisando os valores passados...')
    for n in numeros:
        print(f'{n}', end=' ')
        sleep(1)
    print(f'Foram informados {len(numeros)} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {mValor}.')
    sleep(1)


valores = []
numero = []
for i in range(0, 5):
    tm = randint(1, 10)
    numero.clear()
    for j in range(0, tm):
        numero.append(randint(0, 10))
    valores.append(numero[:])
for i in range(0, len(valores)):
    maior(valores[i])
