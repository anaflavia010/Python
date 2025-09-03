def leiaInt(texto):
    num = input(texto)
    if num.isdecimal():
        return num
    else:
        print(f'\033[31mERRO! Digite um número inteiro válido!\033[m')
        return leiaInt(texto)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
