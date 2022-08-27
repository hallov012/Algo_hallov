import sys, math
sys.stdin = open('input.txt')

def init(node, start, end):
    if start == end:
        tree[node] = data[start]
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
        mid = (start+end)//2
        update(node*2, start, mid, idx, diff)
        update(node*2+1, mid+1, end, idx, diff)
        tree[node] = min(tree[node*2], tree[node*2+1])

def find_min(node, start, end, left, right):
    if start > right or end < left:
        return [sys.maxsize, n]
    if start >= left and end <= right:
        return tree[node]
    mid = (start+end)//2
    return min(find_min(node*2, start, mid, left, right), find_min(node*2+1, mid+1, end, left, right))

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
data = []
for i in range(n):
    data.append([nums[i], i+1])
tree = [[] for _ in range(pow(2, math.ceil(math.log(n, 2))+1))]
init(1, 0, n-1)
m = int(input())
for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 1:
        data[a-1][0] = b
        update(1, 0, n-1, a-1, data[a-1])
    else:
        print(find_min(1, 0, n-1, a-1, b-1)[1])
