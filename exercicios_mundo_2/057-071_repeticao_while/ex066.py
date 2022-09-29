"""

Crie um programa que leia varios numeros inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos numeros foram
digitados e qual foi a soma entre eles ( desconsiderando o flag )

                                                               """
cont = 0
soma = 0
while True:
    numero = int(input('Digite um numero: (para parar digite 999) '))
    if numero == 999:
        break
    cont = cont + 1
    soma = soma + numero
print(f'No total foram digitados {cont} numeros, e a soma entre eles foi de {soma}.')
