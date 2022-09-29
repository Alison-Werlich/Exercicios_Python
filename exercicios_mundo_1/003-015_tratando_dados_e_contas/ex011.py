alt = float(input('Qual a altura da sua parede? '))
larg = float(input('Qual a largura da sua parede? '))
m2 = alt*larg
print('Uma parede de {:.2f} x {:.2f} tem {:.2f} M²'.format(alt, larg, m2))
print('E são nescessarios {:.2f} litros de tinta para pintala'.format(m2/2))