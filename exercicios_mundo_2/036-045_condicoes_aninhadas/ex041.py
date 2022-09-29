"""

A Confederação nacional de natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de
acordo com a idade:
- ate 09 anos : MIRIM
- ate 14 anos : INFANTIL
- ate 19 anos : JUNIOR
- ate 25 anos : SENIOR
- acima : MASTER

                                                              """
from datetime import date

nasc = int(input('Em que ano voce nasceu? '))
idade = date.today().year - nasc
cat = ''
if idade <= 9:
    cat = 'MIRIM'
elif 9 < idade <= 14:
    cat = 'INFANTIL'
elif 14 < idade <= 19:
    cat = 'JUNIOR'
elif 19 < idade <= 25:
    cat = 'SENIOR'
elif 25 < idade:
    cat = 'MASTER'
print('Atletas nascidos em {}, tem atualmente {} anos'.format(nasc, idade))
print('E competem na categoria: {}'.format(cat))
