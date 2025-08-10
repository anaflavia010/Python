num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('=-'*15)
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opção = int(input('>>> Qual é a sua opção? '))
    if opção == 1:
        print(f'A soma entre {num1} + {num2} é {num1 + num2}')
    elif opção == 2:
        print(f'O resultado de {num1} x {num2} é {num1 * num2}')
    elif opção == 3:
        if num1 != num2:
            if num1 > num2:
                maior = num1
            else:
                maior = num2
            print(f'Entre {num1} e {num2}, o maior número é {maior}')
        else:
            print('Os dois números são IGUAIS')
    elif opção == 4:
        print('Informe os números novamentes:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Saindo do programa...')
        print('=-'*15)
        break
    else:
        print('Por favor, informe uma opção válida entre 1 e 5')
print('Volte sempre!')
