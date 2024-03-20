#or from math import trunc
import math
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(num, math.trunc(num)))

#or too
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(num, int(num)))