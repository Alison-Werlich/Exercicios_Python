"""

Crie uma tupla preenchida com os 20 primeiros colocados
da tabela do Campeonato Brasileiros de Futebol, na ordem
de colocação. Depois mostre:

1- os 5 primeiros
2- os ultimos 4
3- times em ordem alfabetica
4- em que posição esta o time da chapecoense

                                         """
times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atletico', 'Botafogo',
         'Atletico-PR', 'Bahia', 'Sao Paulo', 'Fluminense', 'Sport',
         'Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')

print('=' * 80)
print('Os cinco primeiros classificados sao:')
print(times[0:5])
print('=' * 80)
print('Os quartro ultimos classificados sao:')
print(times[-4:])
print('=' * 80)
print('Times em ordem alfabetica:')
print(sorted(times))
print('=' * 80)
chap = (times.index('Chapecoense')) + 1
print(f'A Chapecoence esta na posição {chap}.')