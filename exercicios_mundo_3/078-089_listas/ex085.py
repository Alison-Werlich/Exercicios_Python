"""

Crie um programa onde o usuario possa digitar sete valores
numericos e cadastre-os em uma lista unica que mantenha
separados os valores pares e impares. No final, mostre os
valores pares e impares em ordem crescente.

                                                        """

lista_num = [[], []]

for cont in range(0, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        lista_num[0].append(num)
    else:
        lista_num[1].append(num)

lista_num[0].sort()
lista_num[1].sort()

print(f'Os numeros pares digitados foram {lista_num[0]}')
print(f'Os numeros impares digitados foram {lista_num[1]}')
