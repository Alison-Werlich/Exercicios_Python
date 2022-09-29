"""

Desenvolva um programa que leia o NOME, IDADE e
SEXO de 4 pessoas. No final do programa, mostre:
- A media de idade do grupo
- Qual é o nome do homen mais velho
- Quantas mulheres tem menos de 20 anos

                                              """
media = 0
nome_h_velho = ''
mulher = 0
idade_homen_velho = 0
for c in range(1, 5):
    print('----- {}° PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    media = media + idade
    if idade > idade_homen_velho and sexo.upper() == 'M':
        nome_h_velho = nome
        idade_homen_velho = idade
    if idade < 20 and sexo.upper() == 'F':
        mulher = mulher + 1
media_total = media / 4
print('A media de idade do grupo foi de {:.0f} anos'.format(media_total))
print('O homem mais velho foi o {}.'.format(nome_h_velho))
print('Ao todo foram {} mulher menores de 20 anos.'.format(mulher))
