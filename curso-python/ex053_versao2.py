frase = input().lower().strip()
palavras = frase.split()
palav_juntas = ''.join(palavras)
print(palavras)
print(palav_juntas)
inverso = ''

for i in range(len(palav_juntas)-1, -1, -1):
    inverso += palav_juntas[i]
if inverso == palav_juntas:
    print(f'{palav_juntas} e {inverso}')
    print('É um palíndromo')
else:
    print(f'{palav_juntas} e {inverso}')
    print('Não é um palíndromo')
