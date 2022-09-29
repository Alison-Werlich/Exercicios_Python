"""

Crie um programa que leia varios numeros inteiros pelo teclado.
O programa só vai parar quando o usuario digitar o valor 999, que
é a condição de parada. No final, mostre quantos numeros foram
digitados e qual foi a soma entre eles (desconsiderando o flag).

                                                               """
c = 0
n = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero inteiro: '))
    if n != 999:
        c = c + 1
        soma = soma + n
print('Voce digitou {} valores e a soma dos mesmo é igual a {}'.format(c, soma))
