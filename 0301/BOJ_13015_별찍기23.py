n = int(input())

star = ['' for _ in range(2 * (n - 1) + 1)]
outline = '*' + ' ' * (n - 2) + '*'
middle = '*' + ' ' * (n - 2) + '*' + ' ' * (n - 2) + '*'
for i in range(n):
    if i == 0:
        star[i] = star[2 * (n - i) - 2] = '*' * n + ' ' * (2 * (n - i - 1) - 1) + '*' * n
    elif i == n - 1:
        star[i] = ' ' * i + middle
    else:
        star[i] = star[2 * n - i - 2] = ' ' * i + outline + ' ' * (2 * (n - i - 1) - 1) + outline

for i in range(len(star)):
    print(star[i])