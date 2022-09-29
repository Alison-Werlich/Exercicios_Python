"""

Crie um programa que vai gerar cinco numeros aleatorios e
colocar em uma tupla. Depois disso, mostre a listagem de
numero gerados e tambem indique o menor e o maior valor que
estao na tupla

                                                         """
from random import randint

lista = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print(lista)
print(f'O maior numero foi o {sorted(lista)[-1]}')
print(f'O menor numero foi o {sorted(lista)[0]}')