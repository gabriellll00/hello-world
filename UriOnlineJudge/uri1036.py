a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

delta = b**2 - (4 * a * c)

if a != 0 and delta > 0:
    raiz1 = (-b + (delta ** 0.5)) / (2 * a)
    raiz2 = (-b - (delta ** 0.5)) / (2 * a)
    print(f'R1 = {raiz1:.5f}')
    print(f'R2 = {raiz2:.5f}')
else:
    print('Impossivel calcular')
