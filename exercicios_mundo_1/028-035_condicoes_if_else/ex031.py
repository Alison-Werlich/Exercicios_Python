
""" Desenvolva um programa que pergunte a distancia de uma viagem
em Km. Calcule o preco da passagem, cobrando R$0,50 por Km para
viagens de ate 200km e R$0,45 para viagens mais longe. """

km = float(input('Quantos Km tera sua viagem? '))
if km <= 200:
    passagem = km * 0.50
else:
    passagem = km * 0.45
print('O valor da sua viagem ficara em R${:.2f}'.format(passagem))
