"""

Crie um programa que leia DOIS VALORES e mostre um MENU como o
menu abaixo:
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
Seu programa devera realizar a operação solicitada em cada caso

                                                             """
ESCOLHA = 0
while ESCOLHA != 5:
    ESCOLHA = 0
    print('-=-' * 20)
    N1 = int(input('Digite um numero inteiro: '))
    N2 = int(input('Digite outro numero inteiro: '))
    while ESCOLHA != 4 and ESCOLHA != 5:
        print('-=-' * 20)
        print('''O que deseja fazer com os numeros {} e {}? 
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do programa'''.format(N1,N2))
        print('-=-' * 20)
        ESCOLHA = int(input('Qual sua escolha? '))
        print('-=-' * 20)
        if ESCOLHA == 1:
            print('A soma dos valores {} e {} é {}.'.format(N1, N2, N1 + N2))
        elif ESCOLHA == 2:
            print('A multiplicação de {} e {} é {}.'.format(N1, N2, N1 * N2))
        elif ESCOLHA == 3:
            MAIOR = N1
            if N2 > N1:
                MAIOR = N2
            print('O Maior numero digitado foi {}.'.format(MAIOR))
print('SAINDO DO PROGRAMA ...')
