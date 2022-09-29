
""" Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome separadamente. """


nome = str(input('Qual seu nome completo? '))
lista = nome.split()
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu ultimo nome é {}'.format(lista[-1]))
