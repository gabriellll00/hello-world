peso1 = 0
for n in range(5):
    peso = float(input('Digite um peso: '))
    if peso > peso1:
        peso1 = peso
print(f'O maior peso é {peso1}.')
