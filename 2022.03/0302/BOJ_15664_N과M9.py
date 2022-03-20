n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
idx_lst = [0] * n

sub_set = []
ans = set()

def dfs():
    if len(sub_set) == m:
        ans.add(tuple(sub_set))
        return
    for i in range(n):
        if not idx_lst[i]:
            sub_set.append(nums[i])
            idx_lst[i] += 1
            dfs()
            sub_set.pop()
            idx_lst[i] -= 1

dfs()
ans_lst = list(ans)
ans_lst.sort()
for line in ans_lst:
    print(*line)