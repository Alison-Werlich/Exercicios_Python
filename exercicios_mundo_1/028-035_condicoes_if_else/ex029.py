

""" Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite"""



vel = float(input('Qual a sua velocidade atual? '))
if vel > 80:
    print('Voce escedeu o limite para esta via que era de 80Km\h')
    multa = (vel - 80) * 7
    print('E foi multado no valor de R${:.2f}'.format(multa))
print()
print('Dirija com seguranca !!!')


