def fatorial(num, show=False):
    fat = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= i
    return fat


print(fatorial(5, show = True))
