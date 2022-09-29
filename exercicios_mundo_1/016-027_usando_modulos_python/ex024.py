

""" Crie um programa que leia o nome da cidade que voçê nasceu
e diga de ela começa ou não com o nome SANTO. """

cidade = str(input('Digite o nome da cidade onde nasceu: ').strip())
cidade = cidade.lower()
lista = cidade.split()
print('santo' in lista[0])
