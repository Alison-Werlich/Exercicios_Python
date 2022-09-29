

""" Crie um programa que leia 3 medidas e valide se
as medidas podem formar um triangulo retangulo. """

m1 = int(input('Qual a primeira medida: '))
m2 = int(input('Qual a segunda medida: '))
m3 = int(input('Qual a terceira medida'))
if m1 + m2 > m3 and m1 + m3 > m2 and m2 + m3 > m1:
    print('Com essas medidas é possivel formar um triangulo retangulo.')
else:
    print('Com essas medidas nao é possivel formar um triangulo retangulo.')
