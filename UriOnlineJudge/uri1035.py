a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b > c and d > a:
    if (c + d) > (a + b) and c > 0 < d:
        if a % 2 == 0:
            print('Valores aceitos')
        else:
            print('Valores nao aceitos')
    else:
        print('Valores nao aceitos')
else:
    print('Valores nao aceitos')
