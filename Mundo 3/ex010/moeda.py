def aumentar(preço = 0, taxa = 0, show = False):
    res = preço + (preço * taxa / 100)
    return res if show is False else moeda(res)


def diminuir(preço = 0, taxa = 0, show = False):
    res = preço - (preço * taxa / 100)
    return res if show is False else moeda(res)


def dobro(preço = 0, show = False):
    res = preço * 2
    return res if show is False else moeda(res)


def metade(preço = 0, show = False):
    res = preço / 2
    return res if show is False else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço = 0, aum = 0, dim = 0):
    print('=' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('=' * 40)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{moeda(dobro(preço))}')
    print(f'Metade do preço: \t{moeda(metade(preço))}')
    print(f'{aum}% do aumento: \t{moeda(aumentar(preço, aum))}')
    print(f'{dim}% de redução: \t{moeda(diminuir(preço, dim))}')
    print('=' * 40)