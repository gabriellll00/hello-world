med_idad = 0
mul_menor = 0
age = 0
mais_velho = ''
num_mul = 0

for i in range(4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite uma idade: '))
    print('Feminino digite "f"/Masculino digite "m"')
    sexo = input('Seu sexo: ').strip().lower()
    med_idad += idade
    if sexo == 'm' and idade > age:
        age = idade
        mais_velho = nome
    elif sexo == 'f':
        num_mul += 1
        if idade < 21:
            mul_menor += 1

print(f'A média de idade do grupo é {med_idad / 4} anos')
if mais_velho == '':
    print('Não existem homens nesse grupo.')
else:
    print(f'{mais_velho.title()} é o homem mais velho do grupo.')
if num_mul == 0:
    print('Não tem mulheres nesse grupo.')
else:
    if mul_menor == 0:
        print('Nenhuma mulher nesse grupo tem menos de 21 anos.')
    else:
        print(f'{mul_menor} mulher(es) do grupo tem menos de 21 anos.')
