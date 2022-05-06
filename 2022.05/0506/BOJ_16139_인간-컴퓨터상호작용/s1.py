import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

s = input()
n = len(s)
q = int(input())
check_dic = defaultdict(list)
for i in range(n):
    check_dic[ord(s[i])].append(i)

for key, value in check_dic.items():
    cnt = [0] * (n + 1)
    for num in value:
        cnt[num+1] = 1
    for i in range(1, n+1):
        cnt[i] += cnt[i-1]
    check_dic[key] = cnt

for _ in range(q):
    alpa, l, r = list(input().split())
    if ord(alpa) not in check_dic.keys():
        print(0)
    else:
        ans = check_dic[ord(alpa)][int(r)+1] - check_dic[ord(alpa)][int(l)]
        print(ans)