num = int(input('Digite um número inteiro para ver sua tabuada: '))
print(13 * '-')
for n in range(0, 11):
    print(f'{num:>3} * {n:2} = {num * n}')
print(13 * '-')
