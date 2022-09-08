import sys, math
sys.stdin = open('input.txt')

def update(node, start, end, left, right, diff):
    if right < start or left > end:
        return
    if left <= start and right >= end:
        tree[node] += diff
        return
    else:
        mid = (start+end)//2
        update(node*2, start, mid, left, right, diff)
        update(node*2+1, mid+1, end, left, right, diff)

def find(node):
    global ans
    while node >= 1:
        ans += tree[node]
        node //= 2

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
k = pow(2, math.ceil(math.log(n, 2)))
tree = [0] * (2*k)

for i, j in enumerate(data):
    tree[k+i] = j

m = int(input())
for _ in range(m):
    command = list(map(int, input().split()))
    if command[0] == 1:
        com, a, b, c = command
        update(1, 1, k, a, b, c)
    else:
        com, a = command
        ans = 0
        find(k+a-1)
        print(ans)