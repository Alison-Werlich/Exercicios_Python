
""" Faça um programa que leia o comprimento do
cateto oposto e do cateto adjacente de um
triangulo retangulo, calcule e mostre o
comprimento da hipotenusa."""

import math
adj = float(input('Qual o valor do cateto adjacente? '))
opo = float(input('Qual o valor do cateto oposto? '))
hip = math.hypot(adj, opo)
print("O valor da hipotenusa é {:.2f}".format(hip))
