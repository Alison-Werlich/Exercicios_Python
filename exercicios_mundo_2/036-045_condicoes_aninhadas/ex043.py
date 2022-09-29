"""

Desenvolva uma logica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- abaixo de 18,5: abaixo do peso
- entre 18,5 e 25: peso normal
- 25 ate 30: sobrepeso
- 30 ate 40: obesidade
- acima de 40: obesidade morbida

                                                                """
peso = float(input('Digite seu peso: (kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / altura ** 2
if imc <= 18.5:
    print('Seu IMC é de {:.1f} e voce esta classificado como ABAIXO DO PESO'.format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.1f} e voce esta classificado como PESO NORMAL'.format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.1f} e voce esta classificado como SOBREPESO'.format(imc))
elif imc <= 40:
    print('Seu IMC é de {:.1f} e voce esta classificado como OBESIDADE'.format(imc))
else:
    print('Seu IMC é de {:.1f} e voce esta classificado como OBESIDADE MORBIDA'.format(imc))
