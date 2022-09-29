"""

Faça um programa que calcule a soma
entre todos os numeros impares que são
multiplos de 3 e que se encontram no
intervalo de 1 ate 500.

                                 """
soma = 0
numero = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        numero = numero + 1
        soma = soma + c
print('A soma dos {} numero foi {}.'.format(numero, soma))
