"""

 Escreva um programa que leia dois numeros inteiros e compare-os
 mostrando na tela um mensagem:
 - O primeiro valor é maior
 - O segundo valor é maior
 - Os dois valores sao iguais

                                                              """
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O primeiro numero é o maior.')
elif n2 > n1:
    print('O segundo numero é o maior.')
else:
    print('Os valores sao iguais.')
