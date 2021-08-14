med_idad = 0
mul_menor = 0
age = 0
mais_velho = None
num_mul = 0

for i in range(2):
    nome = input('Digite o nome: ')
    idade = int(input('Digite uma idade: '))
    sexo = input('Seu sexo: ').strip().lower()
    med_idad += idade
    if sexo == 'masculino':
        if idade > age:
            mais_velho = nome
    if sexo == 'feminino':
        num_mul += 1
        if idade < 21:
            mul_menor += 1
print()
print(f'A média de idade do grupo é {med_idad / 2}\n')
if mais_velho is None:
    print('Não existem homens nesse grupo.\n')
else:
    print(f'{mais_velho.title()} é o homem mais velho do grupo.\n')
if num_mul == 0:
    print('Não tem mulheres nesse grupo.\n')
else:
    if mul_menor == 0:
        print('Nenhuma mulher nesse grupo tem menos de 21 anos.\n')
    else:
        print(f'{mul_menor} mulher(es) do grupo tem menos de 21 anos.\n')
