fra = str(input('Digite uma frase: ')).upper()
print('A letra A apareceu {} vezes na frase' .format(fra.count('A')))
print('A primeira letra A apareceu na posição {}' .format(fra.count('A')+1))
print('A última letra A apareceu na posição {}' .format(fra.rfind('A')+1))
