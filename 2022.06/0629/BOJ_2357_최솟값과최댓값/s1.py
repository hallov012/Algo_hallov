import sys, math
sys.stdin = open('input.txt')

def min_init(node, start, end):
    if start == end:
        min_tree[node] = nums[start]
        return min_tree[node]
    else:
        min_tree[node] = min(min_init(node*2, start, (start+end)//2), min_init(node*2+1, (start+end)//2+1, end))
        return min_tree[node]

def max_init(node, start, end):
    if start == end:
        max_tree[node] = nums[start]
        return max_tree[node]
    else:
        max_tree[node] = max(max_init(node*2, start, (start+end)//2), max_init(node*2+1, (start+end)//2+1, end))
        return max_tree[node]

def min_find(node, start, end, left, right):
    if left > end or right < start:
        return sys.maxsize
    if left <= start and right >= end:
        return min_tree[node]
    return min(min_find(node*2, start, (start+end)//2, left, right),
               min_find(node*2+1, (start+end)//2+1, end, left, right))

def max_find(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return max_tree[node]
    return max(max_find(node * 2, start, (start + end) // 2, left, right),
               max_find(node * 2 + 1, (start + end) // 2 + 1, end, left, right))

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
min_tree = [0] * (pow(2, math.ceil(math.log(n, 2))+1))
max_tree = [0] * (pow(2, math.ceil(math.log(n, 2))+1))
min_init(1, 0, n-1)
max_init(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    print(min_find(1, 0, n-1, a, b), end=" ")
    print(max_find(1, 0, n-1, a, b))
