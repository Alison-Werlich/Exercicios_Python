"""

Crie um programa que tenha uma tupla totalmente preenchida
com os numero de zero a vinte.
Deu programa deverar ler um numero entre 0 e 20, e mostrar
ele por extenso.

                                                        """
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= n <= 20:
            break
    print(f'O numero que voce digitou em extenço fica {extenso[n]}')
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
