"""

Crie em programa que leia varios numeros inteiros pelo teclado. No
final da execução, mostre a media entre todos os valores e qua
foi o maior e o menor valor lido. O programa deve perguntar ao
usuario se ele quer ou nao continuar a digitar valores.

                                                                """
soma = 0
media = 0
maior = 0
menor = 0
cont = 0
resp = 'S'
while resp == 'S':
    n = int(input('Digite um numero: '))
    soma += n
    if cont == 0:
        menor = maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    cont = cont + 1
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()
print(f'Foram digitados {cont} numeros, e a media entre eles é de {soma / cont:.2f}.')
print(f'O maior valor digitado foi {maior} e o menor valor foi {menor}.')
