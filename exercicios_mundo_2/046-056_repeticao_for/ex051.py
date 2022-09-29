"""

Desenvolva um programa que leia o
primeiro termo e a razao de uma PA.
No final, mostre os 10 primeiros
termos dessa progressão.

                                """
print('=' * 20)
print('{:^20}'.format('TERMO DE UMA PA'))
print('=' * 20)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for c in range(termo, (10 * razao) + 1, razao):
    print('{}'.format(c), end=' -> ')
print('FIM')
