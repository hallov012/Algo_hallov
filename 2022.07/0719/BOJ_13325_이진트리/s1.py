import sys
from collections import deque
sys.stdin = open('input.txt')

def dfs(deep, node):
    if deep == k-1:
        # max_len으로 두 자식노드를 갱신해줘야 하므로 합은 max_len*2 가 된다
        max_len = max(tree[node][node*2], tree[node][node*2+1])
        dp[node] = [max_len, 2 * max_len]
        return [max_len, 2*max_len]
    else:
        dp[node][0] = max(tree[node][node*2] + dfs(deep+1, node*2)[0],
                       tree[node][node*2+1] + dfs(deep+1, node*2+1)[0])
        # 최장거리의 합에 dp[node][0]에는 자식 노드의 거리도 포함되어있으므로 그것을 뺀 값을 더해준다
        dp[node][1] = dp[node*2][1] + dp[node*2+1][1] + \
                      (dp[node][0] - dp[node*2][0]) + (dp[node][0] - dp[node*2+1][0])
        return dp[node]

k = int(input())
data = deque(list(map(int, input().split())))
tree = {i: {} for i in range(1, 2 ** (k+1))}
# [다음 자식 노드까지의 최장거리, 두 길이의 합]
dp = [[0, 0] for _ in range(2 ** (k+1))]
for i in range(1, 2 ** k):
    tree[i][2*i] = data.popleft()
    tree[i][2*i+1] = data.popleft()
ans = dfs(0, 1)
print(ans[1])