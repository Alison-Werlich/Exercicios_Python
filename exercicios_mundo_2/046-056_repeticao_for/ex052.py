"""

Faça um programa que leia um
numero inteiro e diga se ele é
ou nao um numero primo.

                           """
num = int(input('Digite um numero: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont = cont + 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='-')
print('\033[m FIM')
if cont == 2:
    print('O numero {} é PRIMO.'.format(num))
else:
    print('O numero {} NÃO é PRIMO.'.format(num))
