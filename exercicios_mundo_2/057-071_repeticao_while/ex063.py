"""

Escreva um programa que leia um numero n inteiro qualquer e
mostre na tela os n primeiros elementos de uma sequencia de
fibonacci.
Ex:
0-1-1-2-3-5-8

                                                        """
print('-=' * 11)
print('Sequencia de Fibonacci')
print('-=' * 11)
n_termos = int(input('Quantos termos vc quer mostrar? '))
print('~~' * 11)
fibonacci_1 = 0
fibonacci_2 = 1
fibonacci_3 = 1
print('{} - {} - '.format(fibonacci_1, fibonacci_2), end='')
c = 3
while c <= n_termos:
    fibonacci_3 = fibonacci_1 + fibonacci_2
    print(fibonacci_3, '-', end=' ')
    fibonacci_1 = fibonacci_2
    fibonacci_2 = fibonacci_3
    c = c + 1
print('FIM')
