print('='*40)
vdolar = float(3.27)
print('Cotação do dolar hoje é ${}'.format(vdolar))
print('='*40)
vreal = float(input('Quantos reais deseja trocar por dolar? '))
print('A quantia de R${:.2f} em dolar é US${:.2f}'.format(vreal, (vreal/vdolar)))
