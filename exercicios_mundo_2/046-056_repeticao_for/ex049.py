"""

Refaça o DESAFIO 9, mostrando a
tabuada de um numero que o usuario
escolher, so que agora utilizando um
laço FOR.

                                 """
n = int(input('Digite qual tabuada deseja ver: '))
for c in range(1, 11):
    print('{} x {:<2} = {}'. format(n, c, c * n))
