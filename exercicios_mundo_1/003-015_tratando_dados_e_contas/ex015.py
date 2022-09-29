dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos km rodou com o carro? '))
vdias = dias * 60
vkm = km * 0.15
print('O total a pagar é de R${:.2f}'.format(vkm + vdias))
