from random import randint
cont = soma = 0
while True:
    computador = randint(0, 10)
    jogador = -1
    tipo = ' '
    while jogador not in range(0, 10):
        jogador = int(input('Diga um valor: '))
        soma = jogador + computador
    while tipo not in 'IP':
        tipo = input('PAR ou ÍMPAR: ').strip().upper()[0]
        print(f'Você jogou {jogador} e o computador {computador}. A soma foi: {soma}')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if tipo in 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    elif tipo in 'ÍI':
        if soma % 2 == 1:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {cont} vezes.')
