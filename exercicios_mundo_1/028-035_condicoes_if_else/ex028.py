""" Escreva em programa que faça o computador "pensar" em um
numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir
qual foi o numero escolhido pelo computador. O programa devera
escrever na tela se o usuario venceu ou perdeu. """

import random
from time import sleep

print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('_______________________________________________________')
npc = random.randint(0, 5)
n = int(input('Em que numero eu pensei? '))
print()
print('Processando...')
sleep(2)
print()
if npc == n:
    print('Parabens voçê acertou.')
else:
    print('Infelismente voce errou.')
    print('O numero que voce escolheu foi {}, e eu tinha escolhido o numero {}.'.format(n, npc))
