"""

Refaça o DESAFIO 051, lendo o primeiro
termo e a razao de uma PA, mostrando
os 10 primeiros termos da progressão
usando a estrutura while

                                    """
print('-=' * 10)
print('    Gerador de PA')
print('-=' * 10)
pt = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
print('-=' * 10)
c = 0
while c < 10:
    print(pt, '-', end=' ')
    pt = pt + rz
    c = c + 1
print('FIM')
