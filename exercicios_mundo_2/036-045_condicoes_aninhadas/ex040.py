"""

Crie um programa que leia duas notas de um aluno e calcule sua media,
mostrando um mensagem no final, de acordo com a media atingida:
- Media abaixo de 5.0: Reprovado
- Media entre 5.0 e 6.9: Recuperação
- Media 7.0 ou superior: Aprovado

                                                                """
n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
media = (n1 + n2) / 2
if media < 5:
    print('Sua media foi de {:.1f}, voce esta REPROVADO.'.format(media))
elif media >= 7:
    print('Sua media foi de {:.1f}, voce esta APROVADO.'.format(media))
else:
    print('Sua media foi de {:.1f}, voce esta em RECUPERACAO.'.format(media))
