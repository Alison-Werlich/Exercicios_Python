"""

Crie um programa onde o usuario digite uma expressão
qualquer que use parenteses. Seu aplicativo devera analizar
se a expressão passada está com os parênteses abertos e
fechados na ordem correta.

                                                       """

n = str(input('Digite uma expressão matematica usando parenteses: '))

lista = []

for carac in expr:
    if carac == '(':
        lista.append('(')
    elif carac == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Sua expressão esta válida.')
else:
    print('Sua expressão está invalida.')
