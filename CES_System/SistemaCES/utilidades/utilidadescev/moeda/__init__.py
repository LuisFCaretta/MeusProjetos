def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço*taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço*taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0,formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0,formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('_'*35)
    print(f'RESUMO DO VALOR'.center(35))
    print('_'*35)
    print(f'Preço analizado: \t\t{moeda(preço)}')
    print(f'O dobro do preço: \t\t{dobro(preço, True)}')
    print(f'A metade do preço: \t\t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t\t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de desconto: \t\t{diminuir(preço, taxar, True)}')
    print('_'*35)
