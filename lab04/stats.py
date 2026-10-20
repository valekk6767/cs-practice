a = int(input())
b = int(input())
c = int(input())
if a > c and a > 8:
    mx = a
elif c > a and c > 8:
    mx = c
else:
    mx = 8
if b < 5:
    mn = b
else:
    mn = 5
if (mx - 12) < 0 or mn == 0:
    print('Ошибка')
else:
    y = ((mx - 12)**0.5) / mn
    print(y)