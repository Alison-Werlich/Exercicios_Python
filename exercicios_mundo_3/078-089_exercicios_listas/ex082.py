"""

Crie um programa que vai ler varios numeros e colocar em uma lista. Depois
disso, crie duas listas extras que vao conter apenas os valores pares e os
valores impares digitados, respectivamente. Ao final, mostre o conteudo das
tres listas geradas.

                                                                        """
tot_lista = []
par_lista = []
impar_lista = []

while True:
    n = int(input('Digite um numero: '))
    tot_lista.append(n)
    if n % 2 == 0:
        par_lista.append(n)
    else:
        impar_lista.append(n)
    while True:
        s_n = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if s_n in 'N':
            break
        elif s_n in 'S':
            print('-=' * 20)
            break
        else:
            print('Caractere Invalido')
    if s_n in 'N':
        break
print('-=' * 20)
print(f'A lista digitada foi : {tot_lista}')
print(f'A lista de pares foi : {par_lista}')
print(f'A lista de impar foi : {impar_lista}')
