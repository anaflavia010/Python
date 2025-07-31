nome = input('Digite seu nome completo: ').strip()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é: {nome.split()[0].title()}')
print(f'Seu último nome é: {nome.split()[-1].title()}')
