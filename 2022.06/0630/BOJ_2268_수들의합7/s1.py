import sys, math
sys.stdin = open('input.txt')

def subsum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]
    return subsum(node*2, start, (start+end)//2, left, right) + subsum(node*2+1, (start+end)//2+1, end, left, right)

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = diff
    else:
        update(node*2, start, (start+end)//2, idx, diff)
        update(node*2+1, (start+end)//2+1, end, idx, diff)
        tree[node] = tree[node*2] + tree[node*2+1]

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0] * (n+1)
tree = [0] * (pow(2, math.ceil(math.log(n, 2))+1))

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        if b < c:
            print(subsum(1, 0, n-1, b-1, c-1))
        else:
            print(subsum(1, 0, n-1, c-1, b-1))
    elif a == 1:
        b -= 1
        nums[b] = c
        update(1, 0, n-1, b, c)

