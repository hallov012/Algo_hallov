import sys, math
sys.stdin = open('input.txt')

def init(node, start, end):
    if start == end:
        tree[node][0] = a_lst[start]
        tree[node][1] = b_lst[start]
    else:
        tree[node][0] = init(node*2, start, (start+end)//2)[0] + init(node*2+1, (start+end)//2+1, end)[0]
        tree[node][1] = init(node*2, start, (start+end)//2)[1] + init(node*2+1, (start+end)//2+1, end)[1]
    return tree[node]

def subsum(node, start, end, left, right):
    if left > end or right < start:
        return [0, 0]
    if left <= start and right >= end:
        return tree[node]
    return [subsum(node*2, start, (start+end)//2, left, right)[0] + subsum(node*2+1, (start+end)//2+1, end, left, right)[0],
            subsum(node*2, start, (start+end)//2, left, right)[1] + subsum(node*2+1, (start+end)//2+1, end, left, right)[1]]

n = int(input())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

tree = [[0, 0] for _ in range(pow(2, math.ceil(math.log(n, 2))+1))]
init(1, 0, n-1)

print(tree)
ans = 0
for i in range(n):
    for j in range(i, n):
        temp = subsum(1, 0, n-1, i, j)
        if temp[0] == temp[1]:
            ans += 1
print(ans)