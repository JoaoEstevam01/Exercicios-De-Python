somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0

for c in range (1, 5):
    print(f'----------PESSOA {c}----------')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'SEXO [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo.lower() == 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if c == 1 and sexo.lower() == 'Ff' and idade > 20:
        totmulher20 += 1

mediaidade = somaidade/4
print('-'*20)
print(f'A média de idade do grupo é {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem}')
print(f'{totmulher20} mulheres têm menos de 20 anos')