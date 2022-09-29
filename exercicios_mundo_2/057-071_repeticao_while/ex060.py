"""

Faça um programa que leia um numero
qualquer e mostre o seu fatorial.
ex.
5! = 5x4x3x2x1 = 120

                                 """
n = int(input('Digite um numero inteiro: '))
c = n
fat = n
print('{}! = {}'.format(n, n), end='')
while c != 1:
    fat = fat * (c - 1)
    c = c - 1
    print('x{}'.format(c), end='')
print(' = {}'.format(fat))
