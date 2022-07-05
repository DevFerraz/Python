extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze')
extenso += ('Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite o número que deseja ver por extenso (1 a 20): '))

for c in range(len(extenso)):
    if c == num:
        print(extenso[num])
if num < 0 or num > 20:
    print('Número inválido! ')
        