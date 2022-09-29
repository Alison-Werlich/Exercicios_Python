"""

Faça um programa que leia o peso de
cinco pessoas. No final, mostre qual foi
o maior peso e qual foi o menor peso lidos.

                                        """
maior_peso = 0
menor_peso = 999
for c in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa? '.format(c)))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print('O maior peso foi de {}kg'.format(maior_peso))
print('O menor peso foi de {}kg'.format(menor_peso))