"""

Crie um programa que verifique se
uma frase é um PALINDROMO.

                              """
# APOS A SOPA
#
frase = str(input('Digite uma frase: ').strip().upper())
lista_de_palavras = frase.split()
junto = ''.join(lista_de_palavras)
inverso = junto[::-1]
print('({}) -- ({})'.format(junto, inverso))
if junto == inverso:
    print('Temos um palindromo')
else:
    print('Nao temos um palindromo')
