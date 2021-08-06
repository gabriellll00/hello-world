valor = float(input())

# Notas + moeda de um real
nota_cem = valor // 100.00
rest_cem = valor % 100.00
nota_cinq = rest_cem // 50.00
rest_cinq = rest_cem % 50.00
nota_vinte = rest_cinq // 20.00
rest_vinte = rest_cinq % 20.00
nota_dez = rest_vinte // 10.00
rest_dez = rest_vinte % 10.00
nota_cinco = rest_dez // 5.00
rest_cinco = rest_dez % 5.00
nota_dois = rest_cinco // 2.00
rest_dois = rest_cinco % 2.00
moeda_1 = rest_dois // 1.00
rest_moeda1real = rest_dois % 1.00
# Moedas
moeda_cinq = rest_moeda1real // 0.50
rest_moeda_cinq = rest_moeda1real % 0.50
moeda_vintcinc = rest_moeda_cinq // 0.25
rest_moeda_vintcinc = rest_moeda_cinq % 0.25
moeda_dez = rest_moeda_vintcinc // 0.10
rest_moeda_dez = rest_moeda_vintcinc % 0.10
moeda_cinc = rest_moeda_dez // 0.05
rest_moeda_cinc = rest_moeda_dez % 0.05
moeda_1cent = rest_moeda_cinc * 100


print('NOTAS:')
print(f'{nota_cem:.0f} nota(s) de R$ 100.00')
print(f'{nota_cinq:.0f} nota(s) de R$ 50.00')
print(f'{nota_vinte:.0f} nota(s) de R$ 20.00')
print(f'{nota_dez:.0f} nota(s) de R$ 10.00')
print(f'{nota_cinco:.0f} nota(s) de R$ 5.00')
print(f'{nota_dois:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda_1:.0f} moeda(s) de R$ 1.00')
print(f'{moeda_cinq:.0f} moeda(s) de R$ 0.50')
print(f'{moeda_vintcinc:.0f} moeda(s) de R$ 0.25')
print(f'{moeda_dez:.0f} moeda(s) de R$ 0.10')
print(f'{moeda_cinc:.0f} moeda(s) de R$ 0.05')
print(f'{moeda_1cent:.0f} moeda(s) de R$ 0.01')
