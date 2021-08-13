soma = 0
for n in range(6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
print(f'A soma dos pares entre os números digitados é: {soma}')
