import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
lst_a = [input() for _ in range(n)]
lst_b = [input() for _ in range(m)]
ans = list(set(lst_a) & set(lst_b))
ans.sort()
print(len(ans))
for name in ans:
    print(name)