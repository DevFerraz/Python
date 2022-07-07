tupla = (str(input('Digite a primeira palavra: ')), str(input('Digite a segunda palavra: ')), 
         str(input('Digite a terceira palavra: ')), str(input('Digite a quarta palavra: ')), 
         str(input('Digite a quinta palavra: ')), str(input('Digite a sexta palavra: ')), 
         str(input('Digite a sétima palavra: ')), str(input('Digite a oitava palavra: ')))
for n in tupla:
    print(f'\nNa palavra {n.upper()}, temos: ', end = '')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end = ' ')