

""" Faça um programa que leia um numero de 0 a 9999 e mostre na
tela cada um dos digitos separados em unidade, dezena, centena
e milhar."""


# n = str(input('Digite um numero de 0 a 9999: ').strip())
# print('unidade {:>1}'.format(n[-1]))
# print('Dezena {:>1}'.format(n[-2]))
# print('Centena {:>1}'.format(n[-3]))
# print('Milhar {:>1}'.format(n[-4]))

n = int(input('Informe um numero: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
