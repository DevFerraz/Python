#lista = ('Lápis', 2, 'Caneta', 2.50, 'Caderno', 14, 'Livro de Matemática', 25, 
#        'Compasso', 8, 'Esquadro', 9, 'Estojo', 12.90, 'Mochila', 75)
#print('-' * 38)
#print('{:>25}'.format('LISTA DE PREÇOS'))
#print('-' * 38)
#for pos in range(0, len(lista)):
#    if pos % 2 == 0:
#        print(f'{lista[pos]:.<30}', end = ' ')
#    if pos % 2 == 1:
#        print(f'R${lista[pos]:.2f}')
lista = ('Lápis ', 'Caneta ', 'Caderno ', 'Livro de Matemática ', 
         'Compasso ', 'Esquadro ', 'Estojo ', 'Mochila ')
preco = (float(input('Digite o valor do produto "Lápis": ')), float(input('Digite o valor do produto "Caneta": ')),
         float(input('Digite o valor do produto "Caderno": ')), float(input('Digite o valor do produto "Livro de Matemática": ')),
         float(input('Digite o valor do produto "Compasso": ')), float(input('Digite o valor do produto "Esquadro": ')),
         float(input('Digite o valor do produto "Estojo": ')), float(input('Digite o valor do produto "Mochila": ')))
print('-' * 38)
print('{:>25}'.format('LISTA DE PREÇOS'))
print('-' * 38)
for pos in range(0, len(lista)):
        print(f'{lista[pos]:.<30}', end = ' ')
        print(f'R${preco[pos]:^.2f}')