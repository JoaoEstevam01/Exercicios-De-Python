'''co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = float(ca**2 + co**2) ** (1/2)
print('O valor do comprimento dessa hipotenusa é de {:.2f}' .format(h))'''

#or
from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
print('O valor do comprimento dessa hipotenusa é de {:.2f}' .format(hypot(ca,co)))

