secs = int(input())

horas = secs // 3600
rest_hora = secs % 3600
minutos = rest_hora // 60
rest_minutos = rest_hora % 60
segundos = rest_minutos

print(f'{horas}:{minutos}:{segundos}')
