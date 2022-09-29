"""

Crie um programa que faça o
computador jogar JOKENPO
com voce

                           """
import random
import time

print('''Suas opções: 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA ''')
user = int(input('Qual é a sua jogada? '))
time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
itens = (' ', 'PEDRA', 'PAPEL', 'TESOURA' )
user = (itens[user])
comp = random.randint(1, 3)
comp = (itens[comp])
print('-=--=--=--=--=--=--=--=--=--=--=--=-')
print('Computador jogou {}'.format(comp))
print('Jogador jogou {}'.format(user))
print('-=--=--=--=--=--=--=--=--=--=--=--=-')
if user == 'PEDRA':
    if comp == 'PAPEL':
        print('Computador venceu')
    elif comp == 'TESOURA':
        print('Jogador venceu')
    else:
        print('Empate')
elif user == 'PAPEL':
    if comp == 'PEDRA':
        print('Jogador venceu')
    elif comp == 'TESOURA':
        print('Computador venceu')
    else:
        print('Empate')
elif user == 'TESOURA':
    if comp == 'PEDRA':
        print('Computador venceu')
    elif comp == 'PAPEL':
        print('Jogador venceu')
    else:
        print('Empate')
else:
    print('Jogo Invalido')
