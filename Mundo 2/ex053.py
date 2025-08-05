frase = input('Digite uma frase: ').strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
print(f'A frase {frase} invertida é {inverso}')
if inverso == junto:
    print(f'É UM PALINDROMO.')
else:
    print(f'NÃO É UM PALINDROMO.')
