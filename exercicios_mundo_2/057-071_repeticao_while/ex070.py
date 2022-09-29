"""

Crie um programa que leia o nome e o preco de varios produtos.
O programa deverá perguntar se o usuario vai continuar.
No final, mostre:

1 - Qual é o total gasto na compra.
2 - Quantos produtos custam mais de R$1000,00.
3 - Qual é o nome do produto mais barato

                                                           """
total_gasto = 0
n_produto_caros = 0
nome_produto_barato = ' '
valor_mais_barato = 0
print('-' * 25)
print('       LOJA BARATAO  ')
print('-' * 25)
while True:
    nome_produto = str(input('Nome do produto: '))
    valor_produto = float(input('Valor do produto: '))
    total_gasto = total_gasto + valor_produto
    if valor_produto > 1000:
        n_produto_caros = n_produto_caros + 1
    if valor_mais_barato == 0:
        valor_mais_barato = valor_produto
        nome_produto_barato = nome_produto
    else:
        if valor_produto < valor_mais_barato:
            valor_mais_barato = valor_produto
            nome_produto_barato = nome_produto

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()
    if escolha == 'N':
        break
print(f'Valor total da compra foi de {total_gasto:.2f}')
print(f'Ao todo foram {n_produto_caros} produtos acima de R$1000,00')
print(f'E o produto mais barato foi "{nome_produto_barato}"')
