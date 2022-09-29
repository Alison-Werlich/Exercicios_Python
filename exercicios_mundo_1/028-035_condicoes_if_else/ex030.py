

""" Crie um programa que leia um numero inteiro
e mostre a tela se ele é PAR ou IMPAR. """

n = int(input('Escolha um numero inteiro: '))
if n % 2 == 1:
    print('O numero {} é IMPAR.'.format(n))
else:
    print('O numero {} é PAR'.format(n))
