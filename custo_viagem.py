viagem = int(input('Digite quantos Km tem a sua viagem: '))
custo1 = viagem * 0.5
custo2 = viagem * 0.45

if viagem <=200:
    print('Sua passagem vai custar: {:.2f}' .format(custo1))
else:
    print('Sua passagem vai custar: {:.2f}' .format(custo2))
print('Obrigado por comprar conosco!')