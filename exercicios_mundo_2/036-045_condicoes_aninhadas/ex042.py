"""

Refaça o desafio 35 do triangulos, acrescentado o recurso de
mostrar que tipo de triangulo sera formado:
- Equilatero: todos os lados iguais
- Isosceles: dois lados iguais
- Escaleno: todos lados diferentes

                                                            """
m1 = int(input('Primeira medida: '))
m2 = int(input('Segunda medida: '))
m3 = int(input('Terceira medida: '))
if m1 + m2 > m3 and m1 + m3 > m2 and m2 + m3 > m1:
    if m1 == m2 and m1 == m3:
        print('Essas medidas formam um triangulo EQUILATERO.')
    elif m1 != m2 and m1 != m3 and m2 != m3:
        print('Essas medidas formam um triangulo ESCALENO.')
    else:
        print('Essas medidas formam um triangulo ISOSCELES.')
else:
    print('Essas medidas nao formam um triagulo.')
