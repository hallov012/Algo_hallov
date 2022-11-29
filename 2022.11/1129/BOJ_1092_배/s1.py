import sys
sys.stdin = open('input.txt')

n = int(input())
w_lst = list(map(int, input().split()))
m = int(input())
b_lst = list(map(int, input().split()))
w_lst.sort(reverse=True)
b_lst.sort(reverse=True)
ans = 0
# 박스를 배로 옮길 수 없는 경우
if w_lst[0] < b_lst[0]:
    print(-1)
    exit()

while b_lst:
    ans += 1
    for i in range(n):
        for j in range(len(b_lst)):
            if w_lst[i] >= b_lst[j]:
                b_lst.pop(j)
                break
print(ans)


