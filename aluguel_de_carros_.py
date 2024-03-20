d= int(input('Quantos dias alugados? '))
km= int(input('Quantos km percorridos? '))
print('De acordo com quantos dias o carro foi alugado {} e quantos km foram percorridos {} a taxa a pagar será de R${:.2f}'
      .format(d, km, (d*60) + (km*0.15)))