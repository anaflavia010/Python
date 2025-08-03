peso = float(input('Qual é o seu peso (Kg): '))
altura = float(input('Qual é a sua altura (m): '))
imc = peso / (altura ** 2)
print(f'Seu IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print(f'Você está ABAIXO DO PESO normal!')
elif 18.5 <= imc < 25:
    print(f'PARABÉNS! Você esta na faixa de PESO NORMAL!')
elif 25 <= imc < 30:
    print(f'Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print(f'Você está em OBESIDADE!')
else:
    print(f'Você está em OBSIDADE MÓRBIDA, cuidado!')
