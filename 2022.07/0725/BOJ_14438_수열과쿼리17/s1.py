import sys, math
sys.stdin = open('input.txt')

def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
    else:
        mid = (start + end) // 2
        tree[node] = min(init(node*2, start, mid), init(node*2+1, mid+1, end))
    return tree[node]

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = diff
    else:
        mid = (start + end) // 2
        update(node*2, start, mid, idx, diff)
        update(node*2+1, mid+1, end, idx, diff)
        tree[node] = min(tree[node*2], tree[node*2+1])

def find_min(node, start, end, left, right):
    if left > end or right < start:
        return sys.maxsize
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return min(find_min(node*2, start, mid, left, right), find_min(node*2+1, mid+1, end, left, right))

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
tree = [0] * pow(2, math.ceil(math.log(n, 2))+1)
init(1, 0, n-1)
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        nums[b-1] = c
        update(1, 0, n-1, b-1, c)
    else:
        print(find_min(1, 0, n-1, b-1, c-1))

