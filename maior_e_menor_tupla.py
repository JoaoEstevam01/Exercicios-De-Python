listanum = []
maior = 0
menor = 0
for c in range (0,6 ):
    lanche = listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            mai = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('-'*20)
print(f'Você digitou os valores {listanum}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
