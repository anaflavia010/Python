km_H = int(input('Qual é a velocidade atual do carro: '))
if km_H > 80:
    multa = float((km_H - 80) * 7)
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de \033[33mR${multa:.2f}!\033[m')
print('\033[0;32mTenha um bom dia! Dirija com segurança!\033[m')
