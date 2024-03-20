nome = input('Digite o nome do aluno(a): ')
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
print('O aluno {} \n Teve sua nota no total de {:.2f} e média de {}' .format(nome, (n1 + n2), ((n1+n2) /2)))