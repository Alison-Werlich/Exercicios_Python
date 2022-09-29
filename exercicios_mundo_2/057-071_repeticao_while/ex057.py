"""

Faça um programa que leia o SEXO de uma pessoa, mas só aceite
os valores 'M' e 'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto.

                                                         """
sexo = str(input('Qual seu sexo: [M/F]')).upper().strip()
#
# while sexo not in 'MmFf':
#
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados invalidos, digite seu sexo: [M/F]')).upper().strip()
print('Cadastro efetuado com sucesso!')

