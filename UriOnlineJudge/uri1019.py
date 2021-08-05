valor = int(input())

nota_cem = valor // 100
resto_cem = valor % 100
nota_cinq = resto_cem // 50
resto_cinq = resto_cem % 50
nota_vinte = resto_cinq // 20
resto_vinte = resto_cinq % 20
nota_dez = resto_vinte // 10
resto_dez = resto_vinte % 10
nota_cinco = resto_dez // 5
resto_cinco = resto_dez % 5
nota_dois = resto_cinco // 2
resto_dois = resto_cinco % 2
nota_um = resto_dois

print(valor)
print(f'{nota_cem} nota(s) de R$ 100,00')
print(f'{nota_cinq} nota(s) de R$ 50,00')
print(f'{nota_vinte} nota(s) de R$ 20,00')
print(f'{nota_dez} nota(s) de R$ 10,00')
print(f'{nota_cinco} nota(s) de R$ 5,00')
print(f'{nota_dois} nota(s) de R$ 2,00')
print(f'{nota_um} nota(s) de R$ 1,00')
