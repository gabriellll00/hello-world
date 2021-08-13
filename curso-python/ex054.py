from datetime import date
contador = 0
for anos in range(7):
    ano = int(input())
    if int(date.today().year) - ano < 21:
        contador += 1
print(f'{contador} pessoas são menores de idade.')
