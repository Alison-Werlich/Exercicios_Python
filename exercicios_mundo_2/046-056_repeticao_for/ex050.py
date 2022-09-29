"""

Desenvolva um programa que leia seis
numeros inteiro e mostre a soma
apenas daqueles que forem pares. Se
o valor digitado for impar,
deconsidere-o.

                                 """
print('Digite seis numeros inteiros')
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('{}° numero: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('A soma dos {} numeros pares digitados é {}.'.format(cont, soma))
