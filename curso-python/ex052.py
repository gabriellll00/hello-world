while True:
    numero = input('Digite um número: ')
    contador = 0
    if numero == 'fim':
        break
    numero = int(numero)
    for num in range(1, numero+1):
        if numero % num == 0:
            contador += 1
    if contador == 2:
        print(f'{numero} é um número primo.')
        print(f'{contador} divisão/divisões.')
    else:
        print(f'{numero} não é um número primo.')
        print(f'{contador} divisão/divisões.')

