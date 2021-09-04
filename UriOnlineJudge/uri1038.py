cod, quant = input().split()

if cod == '1':
    print(f'Total: R$ {(int(quant) * 4):.2f}')
elif cod == '2':
    print(f'Total: R$ {(int(quant) * 4.50):.2f}')
elif cod == '3':
    print(f'Total: R$ {(int(quant) * 5):.2f}')
elif cod == '4':
    print(f'Total: R$ {(int(quant) * 2):.2f}')
elif cod == '5':
    print(f'Total: R$ {(int(quant) * 1.50):.2f}')
