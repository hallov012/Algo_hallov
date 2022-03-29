import sys, heapq
sys.stdin = open('input.txt')

def check(lst):
    for k in range(10):
        if lst[k] == 3:
            return True
    for j in range(8):
        if lst[j] and lst[j+1] and lst[j+2]:
            return True
    return False

T = int(input())

for tc in range(1, T+1):
    ans = 0
    n = 12
    data = list(map(int, input().split()))
    player_1, player_2 = [0] * 10, [0] * 10
    for i in range(n):
        if not i % 2:
            player_1[data[i]] += 1
            if check(player_1):
                ans = 1
                break
        else:
            player_2[data[i]] += 1
            if check(player_2):
                ans = 2
                break

    print(f'#{tc} {ans}')