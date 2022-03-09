import sys
sys.stdin = open('input.txt')

# 별(4) > 동그라미(3) > 네모(2) > 세모(1)
N = int(input())
for n in range(N):
    card_a = list(map(int, input().split()))
    card_b = list(map(int, input().split()))
    cnt_a = [0] * 4
    cnt_b = [0] * 4
    for i in range(1, card_a[0]+1):
        cnt_a[card_a[i]-1] += 1
    for i in range(1, card_b[0]+1):
        cnt_b[card_b[i]-1] += 1
    i = 3
    while i >= 0:
        if cnt_a == cnt_b:
            print('D')
            break
        if cnt_a[i] > cnt_b[i]:
            print('A')
            break
        elif cnt_a[i] < cnt_b[i]:
            print('B')
            break
        else:
            pass
        i -= 1


