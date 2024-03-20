print('-'*20)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))

while True:
    print('-'*20)
    print('''          [1] SOMAR
          [2] MULTIPLICAR
          [3] MAIOR
          [4] NOVOS NÚMEROS
          [5] SAIR DO PROGRAMA''')
    opção = int(input('Sua opção: '))

    if opção == 1:
        print(f'O valor de {n1} + {n2} = {n1+n2}')
    elif opção == 2:
        print(f'O valor da multiplicação {n1} * {n2} = {n1*n2}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}')
    elif opção == 4:
        print('Informe os número novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opção == 5:
        print('Encerrando...')
        break
print('Fim do Programa')
