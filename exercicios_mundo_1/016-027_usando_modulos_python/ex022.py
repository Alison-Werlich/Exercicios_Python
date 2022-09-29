
"""  Crie um programa que leia o nome
completo de uma pessoa e mostre:

*  O nome com todas as letras maiusculas
*  O nome com todas as letras minusculas
*  Quantas letras tem (sem considerar espaço)
*  Quantas letras tem o primeiro nome  """


nome = input('Digite seu nome completo: ')
print('Seu nome com letras maiusculas fica assim:\n{}'.format(nome.upper()))
print('Seu nome com letras minusculas fica assim:\n{}'.format(nome.lower()))
esp = nome.count(" ")
print('Seu nome tem {} letras'.format(len(nome) - esp))
lista = nome.split()
print('O seu primeiro nome é {} e tem {} letras'.format(lista[0].capitalize(), len(lista[0])))
