"""

Melhore o jogo do DESAFIO 028 onde o computador vai
"pensar" em um numero entre 0 e 10. Só que agora o
jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessarios para
vencer.

                                                 """
from random import randint

N_PC = randint(0, 10)
N_USUARIO = int(input('Digite um numero inteiro entre 0 e 10: '))
PALPITES = 1
while N_PC != N_USUARIO:
    if N_USUARIO < N_PC:
        N_USUARIO = int(input('Tente um numero mais alto: '))
    else:
        N_USUARIO = int(input('Tente um numero mais baixo: '))
    PALPITES = PALPITES + 1
print('Parabens o numero {} foi o numero escolhido pelo Computador.'.format(N_USUARIO))
print('E voce precisou de {} tentativas para acertar.'.format(PALPITES))
