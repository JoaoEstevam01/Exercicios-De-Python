while True:
    print('-' *20)
    n1 = int(input('Digite um número para ver a sua tabuada: '))
    print('-' *20)
    if n1 < 0:
        break
    for c in range(1,11):
        print('{} x {} = {}' .format(n1, c, n1*c))
print('PROGRAMA ENCERRADO! NÃO ACEITAMOS NÚMERO NEGATIVOS!')
