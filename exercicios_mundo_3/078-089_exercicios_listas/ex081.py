"""

Crie um programa que vai ler varios numeros e colocar em uma
lista. Depois disso, mostre:

1 - Quantos numeros foram digitados.
2 - A lista de valores em ordem decrescente.
3 - Se o valor 5 foi digitado e esta ou nao na lista.

                                                          """

lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    s_n = str(input('Quer continuar? "N" para parar ou outra letra para continuar: ')).strip().upper()[0]
    if s_n == 'N':
        break
print('-=' * 20)
print(f'Foram digitados {len(lista)} numeros.')
lista.sort(reverse=True)
print(f'os numeros em sequencia regressiva são: {lista}')
print(f'O numero 5 foi digitado {lista.count(5)} vezes')
