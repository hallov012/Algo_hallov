import sys
sys.stdin = open('input.txt')

n = int(input())
data = list(map(int, input().split()))
cnt = [0] * 41
for num in data:
    cnt[num] += 1

# 최대 갯수가 2이고 before은 점점 작아져야 함
before = 2
flag = True
for num in cnt:
    if num > before:
        flag = False
        break
    before = num

if flag:
    ans = 2 ** (cnt.count(2))
    if 1 in cnt:
        ans *= 2
    print(ans)
else:
    print(0)
