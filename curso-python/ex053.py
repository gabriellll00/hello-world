frase = input().lower().replace(' ', '')
if frase == frase[::-1]:
    print('é um palíndromo')
else:
    print('não é um palíndromo')
