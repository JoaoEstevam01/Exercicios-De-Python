print('-'*20)
print('BANCO ITAÚ')
print('-'*20)
saque = int(input('Qual valor você deseja sacar? '))
total = saque
céd = 50
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd += 1

    else:
        print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
    