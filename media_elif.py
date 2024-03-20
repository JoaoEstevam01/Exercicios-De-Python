nota1 = float(input('Qual foi a primeira nota? '))
nota2 = float(input('Qual foi a segunda nota? '))
media = (nota1 + nota2) / 2

if media <= 5.0:
    print('REPROVADO! Sua nota foi {}' .format(media))
elif 5.0 < media <= 6.9:
    print('RECUPERAÇÃO! Sua nota foi {}' .format(media))
else: 
    print('APROVADO! Sua nota foi {}' .format(media))