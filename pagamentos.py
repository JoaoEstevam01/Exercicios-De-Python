print('-'*5, 'CASAS BAHIANA', '-'*5)

preço = float(input('Digite o valor da compra: R$'))
juros = preço + (preço /3)
print('-'*20)


print('''FORMAS DE PAGAMENTO
    [1] à vista dinheiro/cheque
    [2] à vista cartão
    [3] 2x no cartão
    [4] 3x ou mais no cartão''')
opção = int(input('Sua opção: '))
print('-'*20)

if opção == 1:
    print('Sua compra no valor de R${:.1f} possui um desconto de 10% \nO novo valor será de R${:.1f}' .format(preço, preço - (preço *0.10)))
    print('-'*20)
elif opção == 2:
    print('Sua compra no valor de R${:.1f} possui um desconto de 5% \nO novo valor será de R${:.1f}' .format(preço, preço - (preço *0.05)))
    print('-'*20)
elif opção == 3:
    print('Sua compra no valor de R${:.1f} não possui desconto. \nO valor final é 2x R${:.1f}' .format(preço, preço / 2))
    print('-'*20)
elif opção == 4:
    print('Sua compra no valor de R${:.1f} em 3x ou mais no cartão possui 20% de juros, ou seja, \nSerá 3x R${:.1f} \nNo valor total de R${:.1f}' .format(preço, preço /3, juros))
    print('-'*20)

continuar = input('Deseja finalizar a compra [S/N]? ')
if continuar.lower() == 's':
    print('Pedido realizado com sucesso!')
elif continuar.lower() == 'n':
    print('Pedido cancelado com sucesso!')