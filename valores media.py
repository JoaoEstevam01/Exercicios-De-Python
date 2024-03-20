valor = soma = 0
while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor != 999:
        soma += valor
    else:
        break