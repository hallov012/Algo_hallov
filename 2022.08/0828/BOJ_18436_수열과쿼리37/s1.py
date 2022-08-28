import sys, math
sys.stdin = open('input.txt')

def init(node, start, end):
    if start == end:
        # 짝수일 경우, 0번 idx에 1로 저장
        if not data[start]%2:
            tree[node][0] = 1
        else:
            tree[node][1] = 1
    else:
        mid = (start+end)//2
        init(node*2, start, mid)
        init(node*2+1, mid+1, end)
        tree[node][0] = tree[node*2][0] + tree[node*2+1][0]
        tree[node][1] = tree[node*2][1] + tree[node*2+1][1]
    return tree[node]

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    if start == end:
        if not diff%2:
            tree[node] = [1, 0]
        else:
            tree[node] = [0, 1]
    else:
        mid = (start+end)//2
        update(node*2, start, mid, idx, diff)
        update(node*2+1, mid+1, end, idx, diff)
        tree[node][0] = tree[node*2][0] + tree[node*2+1][0]
        tree[node][1] = tree[node*2][1] + tree[node*2+1][1]

def find(node, start, end, left, right):
    if start > right or end < left:
        return [0, 0]
    if left <= start and right >= end:
        return tree[node]
    else:
        mid = (start+end)//2
        left_node = find(node*2, start, mid, left, right)
        right_node = find(node*2+1, mid+1, end, left, right)
        return [left_node[0]+right_node[0], left_node[1]+right_node[1]]

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
tree = [[0, 0] for _ in range(pow(2, math.ceil(math.log(n, 2))+1))]
init(1, 0, n-1)

m = int(input())
for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 1:
        if data[a-1]%2 == b%2:
            data[a-1] = b
        else:
            data[a-1] = b
            update(1, 0, n-1, a-1, b)
    elif command == 2:
        print(find(1, 0, n-1, a-1, b-1)[0])
    elif command == 3:
        print(find(1, 0, n-1, a-1, b-1)[1])