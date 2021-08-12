soma = 0
imp_multi = []

for c in range(1, 500):
    if c % 2 != 0 and c % 3 == 0:
        imp_multi.append(c)
        soma += c
print(f'A soma dos números ímpares e múltiplos de 3 entre 1 e 500 é {soma}')
print(f'Números ímpares e múltiplos de 3 entre 1 e 500: \n{imp_multi}')
