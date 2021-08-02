codigo, num, valor = input().split()
codigo2, num2, valor2 = input().split()

total = (int(num) * float(valor)) + (int(num2) * (float(valor2)))
print(f'VALOR A PAGAR: R$ {total:.2f}')
