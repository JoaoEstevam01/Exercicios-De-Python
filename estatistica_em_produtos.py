total_gasto = 0
produtos_mais_de_1000 = 0
preco_mais_barato = None
nome_mais_barato = None

while True:
    print('-'*20)
    print('BEMAIS')
    print('-'*20)
    produto = str(input('Nome do produto: '))
    valor_prod = float(input('Preço: R$'))

    total_gasto += valor_prod

    if valor_prod > 1000:
        produtos_mais_de_1000 += 1

    if preco_mais_barato is None or valor_prod < preco_mais_barato:
        preco_mais_barato = valor_prod
        nome_mais_barato = produto

    continuar = str(input('Deseja continuar [S/N]? '))
    if continuar.upper() != 'S':
        break

print('-'*20)
print('RESUMO DA COMPRA:')
print('-'*20)
print(f'Total gasto na compra: R${total_gasto:.2f}')
print(f'Quantidade de produtos acima de R$1000: {produtos_mais_de_1000}')
print(f'Nome do produto mais barato: {nome_mais_barato} (R${preco_mais_barato:.2f})')

