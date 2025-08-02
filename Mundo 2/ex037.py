num = int(input('Digite um número inteiro: '))
print('''Converter para: 
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opção = int(input('Diga sua opção: '))
if opção == 1:
    print(f'O número {num} convertido para BINÁRIO é: {bin(num)[2:]}')
elif opção == 2:
    print(f'O número {num} convertido para OCTAL é: {oct(num)[2:]}')
elif opção == 3:
    print(f'O número {num} convertido para HEXADECIMAL é: {hex(num)[2:]}')
else:
    print('Opção inválida!')
