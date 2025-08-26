frase = str(input('Digite uma expressão: '))
if (frase.count('(') - frase.count(')')) == 0:
    print('Sua expressão está VÁLIDA!')  
else:
    print('Sua expressão NÃO está VÁLIDA!')
