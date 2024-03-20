from random import randint

print('-'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar... ( ͡° ͜ʖ ͡°)')
print('-'*20)

while True:
    computador = randint(0, 5)
    jogador = int(input('Em que número eu pensei? '))

    if jogador == computador:
        print('Parabéns! Você acertou!')
    else:
        print('Não foi dessa vez...')

    tentar_dnv = input('Deseja tentar novamente [S/N]? ')

    if tentar_dnv.lower() == 'n':
        print('Obrigado por jogar!')
        break