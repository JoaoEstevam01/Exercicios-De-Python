valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
pagamento_em_anos = int(input('Digite em quantos anos deseja pagar essa casa: '))
prestação = valor / (pagamento_em_anos*12)
minimo = salario * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos' .format(valor, pagamento_em_anos), end='')
print(' a prestação será de R${:.2f}' .format(prestação))

if prestação <= minimo:
    print('Empréstimo poder ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')