n = int(input())

star = ''
for i in range(2*n):
    if not i % 2:
        star += '*'
    else:
        star += ' '
for i in range(n):
    if not i % 2:
        print(star)
    else:
        print(' ' + star)
