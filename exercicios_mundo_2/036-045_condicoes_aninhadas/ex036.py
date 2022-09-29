"""

Escreva um programa para aprovar o emprestimo bancario para a
compra de uma casa. Pergunte o VALOR DA CASA, o SALARIO DO COMPRADOR
e em QUANTOS ANOS  ele vai pagar.
A prestação mensal não pode exceder 30% do salario ou entao o
emprestimo sera negado.

                                                                  """
vcasa = float(input('Qual o valor da casa que ira financiar? R$'))
salario = float(input('Quanto é seu salario mensal? R$'))
anos = int(input('Em quantos anos quer financiar? '))
print('Para um emprestimo no valor de R${:.2f} em {:.0f}x, o valor da '
      'prestação ficara R${:.2f} por mes'.format(vcasa, (anos * 12), (vcasa / (anos * 12))))
if vcasa / (anos * 12) > salario * 30 / 100:
    print('Devido ao valor mensal das parcelas comprometer mais de 30% do seu salario, seu emprestimo sera NEGADO.')
else:
    print('Seu emprestimo foi APROVADO.')
