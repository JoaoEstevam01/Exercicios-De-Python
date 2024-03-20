nome = input('Digite o seu nome: ')
peso = int(input('Quanto você pesa em Kg? '))
altura = float(input('Qual é a sua altura em metros? '))
calculo = peso / (altura * altura)

if calculo < 18.5:
    print('{} está ABAIXO DO PESO e com IMC de {:.2f}' .format(nome, calculo))
elif 18.5 <= calculo <= 25:
    print('{} está no PESO IDEAL e com IMC de {:.2f}' .format(nome, calculo))
elif 25 < calculo <= 30:
    print('{} está com SOBREPESO e com IMC de {:.2f}' .format(nome, calculo))
elif 30 < calculo <= 40:
    print('{} está com OBESIDADE e com IMC de {:.2f}' .format(nome, calculo))
else:
    print('{} está com OBESIDADE MÓRBIDA e com IMC de {:.2f}' .format(nome, calculo))