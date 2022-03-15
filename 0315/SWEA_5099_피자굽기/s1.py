import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    pizza = []
    ans = []
    for i in range(n):
        pizza.append([cheese[i], i+1])
    i = 0 # 꺼낸 피자의 갯수
    while len(pizza) > 1:
        now_cheese, idx = pizza.pop(0)
        now_cheese //= 2
        if not now_cheese:
            if n + i < m:  # 처음에 넣은 피자 + 꺼낸 피자의 수 < 전체 피자의 수 => 피자를 더 넣어줘야한다
                pizza.append([cheese[n+i], n+i+1])
                i += 1
            else:
                continue
        else:
            pizza.append([now_cheese, idx])
    print(f'#{tc} {pizza[0][1]}')

