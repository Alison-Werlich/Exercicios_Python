"""

Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual sera o valor a ser sacado
(numero inteiro)  e o programa vai informar quantas cedulas de
cada valor serao entregues.

OBS. Considerando que o caixa possui cedulas de R$50, R$20 R$10 e R$1.

                                                                   """
import time

print('-' * 25)
print('   BANCO TABAJARA   ')
print('-' * 25)

saque = int(input('Digite o valor a ser sacado: '))
notas_50 = saque // 50
saque = saque % 50
notas_20 = saque // 20
saque = saque % 20
notas_10 = saque // 10
saque = saque % 10
notas_1 = saque // 1
print('-' * 25)
print('   CALCULANDO...   ')
print('-' * 25)
time.sleep(2)
print(f'''Segue a contagem de notas:
{notas_50:2} notas de R$50
{notas_20:2} notas de R$20
{notas_10:2} notas de R$10
{notas_1:2} notas de R$1''')
