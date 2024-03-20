'''tempo = int(input('Quantos anos tem seu carros? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')'''

#Mais fácil de escrever, porém difícil entender 
tempo = int(input('Qauntos anos tem seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('--FIM--')