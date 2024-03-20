velo = int(input('Digite a velocidade em Km do carro: '))
multa = int((velo - 80) * 7)
if velo >= 80:
    print('O seu carro foi MULTADO no valor de R${}' .format(multa))
else:
    print('O seu carro não foi multado.')