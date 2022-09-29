"""

Faça um programa que mostre a tabuada de varios numeros,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado
for negativo.

                                                     """
while True:
    print('-=' * 17)
    n = int(input('Quer ver a tabuada de qual numero? '))
    print('-=' * 17)
    if n < 0:
        print('Programa tabuada encerrado!!! Volte sempre.')
        break
    for c in range(1, 11):
        print(f'{n} x {c:<2} = {n * c}')
