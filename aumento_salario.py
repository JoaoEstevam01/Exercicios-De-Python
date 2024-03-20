
salario = int(input('Digite o salário do funcionário: R$ '))
aumento1 = salario + (salario * 0.10)
aumento2 = salario + (salario * 0.15)

if salario >= 1250:
    print('O salário agora será:   R${}' .format(aumento1))
else:
    print('O salário agora será: R${}' .format(aumento2))