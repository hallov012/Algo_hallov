import sys, math
sys.stdin = open('input.txt')

def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
    else:
        mid = (start+end)//2
        tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = diff
    else:
        mid = (start+end)//2
        update(node*2, start, mid, idx, diff)
        update(node*2+1, mid+1, end, idx, diff)
        tree[node] = tree[node*2] + tree[node*2+1]

def subsum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return subsum(node*2, start, mid, left, right) + subsum(node*2+1, mid+1, end, left, right)

input = sys.stdin.readline

n, q = map(int, input().split())
nums = list(map(int, input().split()))
tree = [0] * pow(2, math.ceil(math.log(n, 2))+1)
init(1, 0, n-1)

for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x < y:
        print(subsum(1, 0, n-1, x-1, y-1))
    else:
        print(subsum(1, 0, n-1, y-1, x-1))
    update(1, 0, n-1, a-1, b)

