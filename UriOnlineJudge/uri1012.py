a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

area_trian = (a * c) / 2
area_cir = 3.14159 * (c**2)
area_trap = ((a + b) * c) / 2
area_qua = b * b
area_ret = a * b

print(f'TRIANGULO: {area_trian:.3f}')
print(f'CIRCULO: {area_cir:.3f}')
print(f'TRAPEZIO: {area_trap:.3f}')
print(f'QUADRADO: {area_qua:.3f}')
print(f'RETANGULO: {area_ret:.3f}')
