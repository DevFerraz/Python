import random
num = random.randint(1, 100)
t1 = num    
num = random.randint(1, 100)
t2 = num
num = random.randint(1, 100)
t3 = num
num = random.randint(1, 100)
t4 = num
num = random.randint(1, 100)
t5 = num
tupla = (t1, t2, t3, t4, t5)
print(tupla)
menor = 0
if t1 > t2:
    menor = t2
elif t2 > t3:
    menor = t3
elif t3 > t4:
    menor = t4
elif t4 > t5:
    menor = t5
maior = 0
if t1 < t2:
    maior = t2
elif t2 < t3:
    maior = t3
elif t3 < t4:
    maior = t4
elif t4 < t5:
    maior = t5
print('O maior número gerado é: {}'.format(maior))
print(f'O menor numero gerado é: {menor}')