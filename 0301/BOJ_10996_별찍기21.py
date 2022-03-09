n = int(input())

for i in range(2 * n):
    if not i % 2:
        for j in range(n):
            if not j % 2:
                print('*', end='')
            else:
                print(' ', end='')
    else:
        for j in range(n):
            if not j % 2:
                print(' ', end='')
            else:
                print('*', end='')
    print()
