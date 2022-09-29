"""

Crie um programa onde o usuario possa digitar varios valores
numericos e cadastre-os em uma lista. caso o numero ja exista
la dentro, ele nao sera adicionado. No final, serao exibidos todos
os valores unicos digitados, em ordem crescente.

                                                              """
lista_num = []
while True:
    num = int(input('Digite um valor numerico: '))
    if num not in lista_num:
        lista_num.append(num)
    else:
        print(f'O numero {num} já esta na lista e não sera adicionado.')
    s_n = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if s_n in 'Nn':
        break
lista_num.sort()
print(f'Os valores unicos digitados em ordem crescente são: {lista_num}')
