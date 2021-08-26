peso1 = 0
peso2 = 0

for n in range(1, 6):
    peso = float(input('Digite um peso: '))
    if peso > peso1:
        peso1 = peso
        print(peso1)
    if peso2 == 0:
        peso2 = peso
        print(peso2)
    elif peso < peso2:
        peso2 = peso
        print(peso2)
print(f'O maior peso é {peso1}.')
print(f'O menor peso é {peso2}.')
