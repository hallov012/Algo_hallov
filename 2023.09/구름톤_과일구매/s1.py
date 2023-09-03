import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
fruits = []
for _ in range(n):
    p, c = map(int, input().split())
    # 1원당 얻을 수 있는 포만감 & 조각의 수 저장
    fruits.append((c//p, p))

fruits.sort(reverse=True)
ans = 0
for a, b in fruits:
    if b <= k:
        k -= b
        ans += a * b
    else:
        ans += a * k
        break

print(ans)

