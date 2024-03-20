s1= float(input('Qual é o salário do funcionário? R$'))
print('O funcionário com o salário de R${} com o aumento de 15%, vai passar a receber R${:.2f}'
      .format(s1, s1 + (s1*0.15)))