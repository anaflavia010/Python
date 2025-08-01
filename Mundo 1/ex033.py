num1 = int(input('Primeio número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

menor = num1
maior = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')