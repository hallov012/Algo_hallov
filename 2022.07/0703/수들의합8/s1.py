import sys
from collections import defaultdict
sys.stdin = open('input.txt')

n = int(input())
sum_lst = [0] * (n+1)
a_lst = [0] + list(map(int, input().split()))
b_lst = [0] + list(map(int, input().split()))
check = defaultdict(list)
check[0].append(0)

# 각 인덱스의 차이 + 지금까지의 차이 값을 sum_lst에 저장
for i in range(1, n+1):
    sum_lst[i] = a_lst[i] - b_lst[i] + sum_lst[i-1]
    check[sum_lst[i]].append(i)

ans = 0
# 차이가 같은 인덱스들이라면 2개를 골라 쌍을 만들면 합이 같다
for value in check.values():
    l = len(value)
    # l개의 idx 중 2쌍을 구하는 경우의 수를 ans에 더한다
    ans += l*(l-1) // 2
print(ans)