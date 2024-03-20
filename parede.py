lag= float(input('Largura da parede: '))
alt= float(input('Altura da parede: '))
print('Sua parede tem dimensão de {}m x {}m e a sua área é de {:.2f}m².' .format (lag, alt, (lag*alt)))
print('Para pintar a sua parede é necessário {:.2f}L de tinta.' .format((lag*alt) /2 ))