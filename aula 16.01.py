campeonato = ('Palmeiras', 'Athletico-PR', 'Atlético-MG', 'Corinthians')
campeonato += ('Internacional', 'Fluminense', 'São Paulo', 'Flamengo')
campeonato += ('Botafogo', 'Santos', 'Avaí', 'Coritiba', 'América-MG')
campeonato += ('Bragantino', 'Ceará', 'Atlético-GO', 'Goiás', 'Cuiabá')
campeonato += ('Juventude', 'Fortaleza')
print('Os 5 primeiros colocados são: ')
for c in range(0, 5):
    print(campeonato[c])
print('Os 4 últimos colocados são: ')
for c in range(16, 20):
    print(campeonato[c])
print('A ordem alfabética dos times do campeonato brasileiro série A é:')
print(sorted(campeonato))
print('O time do {} está na posição 7! '.format(campeonato[6]))

