"""

Desenvolva um programa que leia quatro valores pelo teclado e
guarde-o em uma tupla. No final mostre:

1 - Quantas vezes apareceu o numero 9
2 - Em que posição o 3 aparece primeiro
3 - Quais foram os numeros pares

                                                        """
num = (int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')))
print(f'O numero 9 foi digitado {num.count(9)} vezes.')
if num.count(3) > 0:
    print(f'O numero 3 aparece primeiro na posição {num.index(3)+1}ª.')
else:
    print('o numero 3 nao esta dentro da tupla.')
print('Os numero pares digitados foram: ')

for numero in num:
    if numero % 2 == 0:
        print(f'{numero}', end='  ')
