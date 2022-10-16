"""

Crie um programa que crie uma matriz de dimensao
3x3 e preencha com valores lidos pelo teclado

No final, mostre na tela, com a formatação correta

                                                """

matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        n = int(input(f'Digite o numero [{linha}:{coluna}]: '))
        matriz[linha].insert(coluna, n)

print('-=' * 30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
