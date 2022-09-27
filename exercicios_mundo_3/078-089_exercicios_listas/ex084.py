"""

Faça um programa que leia NOME e PESO de varias pessoas,
guardando tudo em uma lista. No final mostre:

1 - Quantas pessoas foram cadastradas.
2 - Uma listagem com as pessoas mais pesadas.
3 - Uma listagem com as pessoas mais leves.

                                                      """
import os
lista_final = []
resp = ''
peso_maior = 0
peso_menor = 0

while True:
    lista = []
    lista.append(str(input('Digite seu nome: ')))
    lista.append(float(input('Digite seu peso: ')))
    lista_final.append(lista)
    while resp != 'S' or 'N':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp == 'S' or 'N':
            break
    if resp == 'N':
        break

print(f'Ao todo foram cadastradas {len(lista_final)} pessoas.')

for pessoa in lista_final:
    if peso_menor == 0 and peso_maior == 0:
        peso_maior = pessoa[1]
        peso_menor = pessoa[1]
    if pessoa[1] > peso_maior:
        peso_maior = pessoa[1]
    if pessoa[1] < peso_menor:
        peso_menor = pessoa[1]

lista_maior = []
lista_menor = []

for pessoa in lista_final:
    if pessoa[1] == peso_maior:
        lista_maior.append(pessoa[0])
    if pessoa[1] == peso_menor:
        lista_menor.append(pessoa[0])

print(f'As pessoas com o maior peso foram {lista_maior} com {peso_maior}kg ')
print(f'As pessoas com o menor peso foram {lista_menor} com {peso_menor}kg ')
