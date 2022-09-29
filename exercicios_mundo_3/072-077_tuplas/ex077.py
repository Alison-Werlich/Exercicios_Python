"""

Crie um programa que tenha uma tupla com varias palavras
(nao usar acento). Depois disso, voce deve mostrar, para cada palavra,
quais sao as suas vogais

                                                                  """
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR',
            'FUTURO')

for palavra in palavras:
    tamanho = len(palavra)
    print(f'\nA palavra {palavra} tem as seguintes vogais : ', end='')
    for cont in range(0, tamanho):
        if palavra[cont] in 'AEIOU':
            print(palavra[cont], end=' ')
