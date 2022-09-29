"""

Crie um programa que leia a idade e o sexo de varias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:

1 - quantas pessoas tem mais de 18 anos.
2 - quantos homens foram cadastrados.
3 - quantas mulheres tem menos de 20 anos.

                                                          """
pessoas_maiores = 0
n_homens = 0
mulheres_menor_20 = 0

while True:
    print('-'*25)
    print('   CADASTRE UMA PESSOA   ')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if idade >= 18:
        pessoas_maiores = pessoas_maiores + 1
    if sexo == 'M':
        n_homens = n_homens + 1
    if sexo == 'F' and idade < 20:
        mulheres_menor_20 = mulheres_menor_20 + 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()
    if escolha == 'N':
        break
print('-' * 25)
print('    Fim dos cadastros')
print('-' * 25)
print(f'Foram cadastradas {pessoas_maiores} pessoas maiores de idade,')
print(f'{n_homens} homens e {mulheres_menor_20} mulheres menores de 20 anos.')
