"""

Crie um programa que leia o ano de
nascimento de sete pessoas. No
final, mostre quantas pessoas
ainda nao atingiram a maioridade e
quantas ja sao maiores.

                                """
from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoas nasceu? '.format(c)))
    if ano_atual - nasc < 18:
        menor = menor + 1
    else:
        maior = maior + 1
print('No ano atual, {} sao maiores de idade e {} sao menores'.format(maior, menor))
