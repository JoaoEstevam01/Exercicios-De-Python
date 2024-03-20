n1 = int(input('Digite um número para ver a sua tabuada: '))
print('-' *20)
for c in range(1,11):
    print('{} x {} = {}' .format(n1, c, n1*c))
print('-' *20)