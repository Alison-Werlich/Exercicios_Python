

""" Escreva um programa que pergunte o salario de um fucionario e
calcule o valor do seu aumento.
Para salarios superiores a R$1.250,00 calcule um aumento de 10%
Para inferiores ou iguais, o aumento sera de 15%. """

sal = float(input('Qual o valor do seu salario atual? '))
if sal <= 1250:
    print('Voce ir ganhar um aumento de 15%')
    print('Seu novo salario sera de R${:.2f}'.format(sal + (sal * 15 / 100)))
else:
    print('Voce ira ganhar um aumento de 10%')
    print('Seu novo salario sera de R${:.2f}.'.format(sal + (sal * 10 / 100)))
