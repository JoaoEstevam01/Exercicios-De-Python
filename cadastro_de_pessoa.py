total_pessoas = 0
total_homens = 0
total_mulheres = 0

while True:
    print('-'*20)
    print('CADASTRO DE PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    if idade >= 18:
        total_pessoas += 1

    elif idade < 20:
        total_mulheres += 1

    if sexo.upper() == 'M':
        total_homens += 1

    continuar = str(input('Deseja continuar [S/N]? '))
    if continuar.upper() == 'N':
        break

print('-'*20)
print(f'Total de pessoas com mais de 18 anos: {total_pessoas}')
print(f'Ao todo temos {total_homens} homens cadastrados')
print(f'E temos {total_mulheres} mulheres com menos de 20 anos')
print('-'*20)