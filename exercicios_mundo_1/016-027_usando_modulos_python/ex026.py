
""" Faça um programa que leia uma frase pelo teclado e mostre:
        > Quantas vezes aparece a letra A
        > Em que posição ela aparece a primeira vez
        > Em que posição ela aparece a ultima vez. """


frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "A" aparece {} vezes em sua frase.'.format(frase.count('a')))
print('A primeira vez que a letra "A" aparece é na posição {}.'.format(frase.find('a')+1))
print('A ultima vez que a letra "A" aparece é na posição {}'.format(frase.rfind('a')+1))
