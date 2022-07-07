tupla = (int(input('Digite um número inteiro: ')),  
         int(input('Digite mais um número inteiro: ')),  
         int(input('Digite outro número inteiro: ')),  
         int(input('Digite o último número inteiro: ')))
print(f'Os números digitados foram: {tupla}')
if 9 in tupla:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes')
else:
    print('O valor 9 não foi digitado. ')
if 3 in tupla:
    print(f'O valor 3 foi digitado a primeira vez na {tupla.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado. ')
print('Os valores pares digitados foram: ', end = '')
for n in tupla:
    if n % 2 == 0:
        print(f'{n}', end = ' ')