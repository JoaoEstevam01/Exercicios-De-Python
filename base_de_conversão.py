print('-'*20)
num = int(input('Digite um número inteiro: '))
print('-'*20)

while True:
    print('''Escolha uma das bases para conversão:
    [1] Converter para BINÁRIO
    [2] Converter para OCTAL
    [3] Converter para HEXADECIMAL''')

    opção = int(input('Sua opção: '))
    print('-'*20)

    if opção == 1:
        print('{} convertido para BÍNARIO é igual a {}' .format(num, bin(num) [2:]))
    elif opção == 2:
        print('{} convertido para OCTAL é igual a {}' .format(num, oct(num) [2:]))
    elif opção == 3:
        print('{} convertido para HEXADECIMAL é igual a {}' .format(num, hex(num) [2:]))
    else:
        print('Obrigado por jogar')
        print('-'*20)

    tentar = input('Deseja tentar novamente [S/N]? ')
    print('-'*20)

    if tentar.lower() != 's':
        break
