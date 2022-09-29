"""

Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao sevico militar,
se é a hora de se alistar ou se ja passou do tempo do alistamento.
Seu programa tambem devera mostrar o tempo que falta ou que ja passou do prazo.

                                                                           """
from datetime import date

nasc = int(input('Qual o ano do seu nascimento: [XXXX] - '))
ano = date.today().year
if ano - nasc == 18:
    print('Parabens voce ja tem 18 anos e deve se alistar este ano.')
elif ano - nasc < 18:
    print('Voce ainda nao tem idade para se alistar')
    print('Voce podera se alistar no ano de {}'.format(nasc + 18))
else:
    print('O ano do seu alistamento ja passou')
    print('Voce deveria ter se alistado no ano de {}.'.format(nasc + 18))
