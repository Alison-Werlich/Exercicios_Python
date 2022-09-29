"""

Faca um programa que leia um numero inteiro qualquer
e de acordo aom a escolha do usuario, mostre como esse numero
ficaria em BINARIO, OCTAL e HEXADECIMAL.

                                                          """
n = int(input('Digite um numero inteiro: '))
print()
print('-=-'*8)
print('Escolha uma das opções de conversao.')
print('-=-'*8)
print('[1] Para Binario')
print('[2] Para Octal')
print('[3] Para Hexadecimal')
escolha = int(input())
if escolha < 1 or escolha > 3:
    print('Escolha invalida.')
elif escolha == 1:
    print('O numero {} em binario fica {}.'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('O numero {} em octal fica {}.'.format(n, oct(n)[2:]))
else:
    print('O numero {} em Hexadecimal fica {}.'.format(n, hex(n)[2:]))
