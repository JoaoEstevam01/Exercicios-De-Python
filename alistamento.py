from datetime import date
nascimento = int(input('Digite o seu ano de nascimento: '))
calculo = date.today().year - nascimento

if calculo <= 17:
    print('Ainda falta um pouco para chegar a sua vez de se alistar!')

elif 18 == calculo:
    print('Já é hora de se alistar!')

else:
    print('Já passou do tempo de se alistar')