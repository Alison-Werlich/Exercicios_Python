

""" Faca um programa que leia tres numeros e
mostre qual é o maior e qual é o menor. """


n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
maior = n1
menor = n1
if n2 > n1:
    maior = n2
if n3 > n1:
    maior = n3
if n2 < n1:
    menor = n2
if n3 < n1:
    menor = n3
print('O maior numero digitado foi {}'.format(maior))
print('O menor numero digitado foi {}'.format(menor))
