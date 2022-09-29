"""

Crie um programa onde o usuario possa digitar cinco valores
numericos e cadastre-os em uma lista, ja na posição correta
de inserção ( sem usar o sort() ). No final, mostre a lista
ordenada na tela.

                                                         """
lista_num = []
for c in range(0, 5):
    num = int(input(f'Digite o {c + 1}ª numero: '))
    if len(lista_num) == 0:
        print(f'O numero {num} foi o primeiro item adicionado a lista')
        lista_num.append(num)
    elif num < lista_num[0]:
        print(f'O numero {num} agora é o primeiro item da lista')
        lista_num.insert(0, num)
    elif num > lista_num[-1]:
        print(f'O numero {num} foi adicionado na ultima posição.')
        lista_num.append(num)
    else:
        cc = 0
        while cc < len(lista_num):
            if num <= lista_num[cc]:
                lista_num.insert(cc, num)
                print(f'O numero {num} foi adicionado a lista na posição {cc + 1}.')
                break
            cc = cc + 1
print(lista_num)
