"""

Melhore o DESAFIO 061, perguntando para o usuario
se ele quer mostrar mais alguns termos. O programa
encerra quando ele dizer que quer mostrar '0' termos.

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
print('PAUSA')
mais = 1
while mais != 0:
    mais = c + int(input('Quantos termos vc quer mostrar a mais? '))
    if mais != (c + 0):
        while c < mais:
            print(pt, '-', end=' ')
            pt = pt + rz
            c = c + 1
        print('PAUSA')
    else:
        print('Progressao finalizada com {} termos mostrados'.format(mais))
