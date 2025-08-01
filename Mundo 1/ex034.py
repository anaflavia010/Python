salario = float(input('Qual é o salário do funcionário? '))

if salario <= 1250.00:
    aumento = (salario * 15 / 100) + salario
    print(f'Quem ganhava R${salario} passa a ganhar R${aumento:.2f}')

else:
    aumento = (salario * 10 / 100) + salario
    print(f'Quem ganhava R${salario} passa a ganhar R${aumento:.2f}')