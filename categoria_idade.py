from datetime import date
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
calculo = date.today().year - ano_nascimento

if calculo <= 9:
    print('ATLETA MIRIM')
elif 14 == calculo:
    print('ATLETA INFANTIL')
elif 19 == calculo:
    print('ATLETA JUNIOR')
elif 20 == calculo:
    print('ATLETA SÊNIOR')
else:
    print('ATLETA MASTER')