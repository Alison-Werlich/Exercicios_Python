
""" Faça um programa que leia  um angulo qualquer e
mostre na tela o valor do seno, cosseno e
tangente desse angulo."""

import math
ang = float(input('Digite um angulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Para o angulo de {}° o valor do seno é {:.2f}, do cosseno é {:.2f} e ta tangente é {:.2f}'.format(ang, seno, cos, tan))
