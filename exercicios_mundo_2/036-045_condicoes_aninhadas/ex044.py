"""

Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condiçoes de pagamento:
- a vista dinheiro ou cheque: 10% de desconto
- a vista no cartao : 5% de desconto
- em ate 2x no cartao: preco normal
- em 3x ou mais no cartao: 20% de juros

                                                              """
print('{:^28}'.format(" LOJAS GUANABARA "))
prod = float(input('Digite o valor do produto: R$'))
print('''Escolha uma das opçoes abaixo
[1] Para pagamento a vista (10% de desconto)
[2] Para a vista no cartao (5% de desconto)
[3] 2x no cartao (Valor da etiqueta)
[4] 3x ou mais no cartao (20% de acrescimo)''')
escolha = int(input(''))
if escolha == 1:
    valor = prod - (prod * 10 / 100)
    print('O valor a vista no dinheiro ou cheque fica RS{:.2f}'.format(valor))
elif escolha == 2:
    valor = prod - (prod * 5 / 100)
    print('O valor a vista no cartao fica RS{:.2f}'.format(valor))
elif escolha == 3:
    valor = prod
    print('O valor em 2x no cartao fica R${:.2f}, sendo 2x de R${:.2F}'.format(valor, valor / 2))
elif escolha == 4:
    valor = prod + (prod * 20 / 100)
    np = int(input('Em quantas vezes deseja parcelar sua compra? '))
    print('''O valor de sua compra parcelada fica RS{:.2f}, em {}x de RS{:.2f}'''.format(valor, np, valor / np))
else:
    print('Opção invalida')
