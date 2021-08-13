while True:
    num = input()
    if num == 'fim':
        break
    num = int(num)
    if num == 2:
        print('É um número primo')
    elif num % num == 0 and num % 1 == 0 and num % 2 != 0:
        print('É um número primo.')
    else:
        print('Não é um número primo.')
