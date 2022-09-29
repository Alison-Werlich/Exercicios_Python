"""

Faça um programa que jogue par ou impar com o computador.
O jogo só sera interrompido quando o jogador PERDER,
mostrando o total de vitorias consecutivas que ele conquistou
no final do jogo.

                                                          """
from random import randint

cont_vit = 0
while True:
    titulo = ' VAMOS JOGAR PAR OU IMPAR '
    print('-=' * 20)
    print(f'{titulo:^40}')
    print('-=' * 20)
    n_pc = randint(0, 10)
    n_jo = int(input('Diga um valor: '))
    esc_jogador = ' '
    while esc_jogador not in 'PI':
        esc_jogador = str(input('Par ou Impar [P/I]')).strip().upper()
    print(f'Voce jogou {n_jo} e o computador {n_pc}.', end=' ')
    if (n_jo + n_pc) % 2 == 0:
        if esc_jogador == 'P':
            print(f'Total deu {n_jo + n_pc} DEU PAR')
            print('Voce Ganhou'.upper())
            cont_vit = cont_vit + 1
        else:
            print(f'Total deu {n_jo + n_pc} DEU PAR')
            print('Voce perdeu.'.upper())
            break
    else:
        if esc_jogador == 'I':
            print(f'Total deu {n_jo + n_pc} DEU IMPAR')
            print('Voce Ganhou'.upper())
            cont_vit = cont_vit + 1
        else:
            print(f'Total deu {n_jo + n_pc} DEU IMPAR')
            print('Voce perdeu.'.upper())
            break
print(f'GAME OVER!!!  Voce venceu {cont_vit} vezes seguidas.')
