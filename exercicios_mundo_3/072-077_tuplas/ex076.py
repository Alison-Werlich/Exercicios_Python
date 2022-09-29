"""

Crie um programa que tenha uma tupla unica com nomes de
produtos e seus respectivos precos, na sequencia. No final,
mostre uma listagem de preco, organizando os dados em
forma de tabela.

                                                      """
lista = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('=' * 60)
print(f'{" LISTAGEM DE PRECOS ":^60}')
print('=' * 60)
for cont in range(0, len(lista), 2):
    print(f'{lista[cont]:.<50}R$ {lista[cont+1]:>7}')
