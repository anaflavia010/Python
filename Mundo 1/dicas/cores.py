'''Type
0 = None/Nada
1 = Bold/Negrito
4 = Underline/Sublilhado
7 = Negativo/Inverte

TEXT              FUNDO
30 =     Branco   = 40
31 =    Vermelho  = 41
32 =     Verde    = 42
33 =    Amarelo   = 43
34 =     Azul     = 44
35 =    Magenta   = 45
36 =     Ciano    = 46
37 =     Cinza    = 47

EXEMPLO:'''
#\033[m PADRÃO
#\033[m (coloca o tipo; texto; fundo)m (Coloca o texto que sera exibido)\033[m e tira a cor no final

print('\033[1;31;44mOlá Mundo!\033[m')