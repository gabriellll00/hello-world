notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

valor = float(input())
print('NOTAS:')
for n in notas:
    num = int(valor // n)
    print(f"{num} nota(s) de R$ {n:.2f}")
    valor = valor % n
print('MOEDAS:')
for m in moedas:
    num = int(valor // m)
    if m == 0.01:
        print(f'{valor*100:.0f} moeda(s) de R$ {m:.2f}')
    else:
        print(f'{num} moeda(s) de R$ {m:.2f}')
    valor = valor % m
