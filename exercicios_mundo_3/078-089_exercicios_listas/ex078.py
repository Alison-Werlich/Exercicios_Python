"""

Faça um programa que leia 5 valores numericos e guarde-os em
uma lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.

                                                         """
lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if maior == menor == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('-=' * 20)
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {maior}, nas posições - ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor}, nas posições - ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print()