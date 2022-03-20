import sys
sys.stdin = open('input.txt')

n = int(input())

for tc in range(n):
    result = str(input())
    ans = 0
    score, i = 1, 0
    while i < len(result):
        if result[i] == 'O':
            ans += score
            score += 1
        else:
            score = 1
        i += 1
    print(ans)