import sys, math
sys.stdin = open('input.txt')

def init(node, start, end):
    if start == end:
        tree[node] = nums[start] % l
    else:
        tree[node] = (init(node*2, start, (start+end)//2) * init(node*2+1, (start+end)//2+1, end)) % l
    return tree[node]

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = diff
    else:
        update(node*2, start, (start+end)//2, idx, diff)
        update(node*2+1, (start+end)//2+1, end, idx, diff)
        # 자식 노드가 먼저 갱신되므로 부모노드를 바뀐 값을 적용해 다시 갱신해준다
        tree[node] = (tree[2*node] * tree[2*node+1]) % l

def find_multi(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[node]
    return (find_multi(node*2, start, (start+end)//2, left, right)
            * find_multi(node*2+1, (start+end)//2+1, end, left, right)) % l

input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
tree = [0] * (pow(2, math.ceil(math.log(n, 2))+1))
l = 1000000007
init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        nums[b] = c
        # diff = c / nums[b]로 둘 경우 zeroDivisionError가 생길 수 있으므로 diff를 c로 두고 함수 내에서 업데이트
        update(1, 0, n-1, b, c)
    elif a == 2:
        b, c = b-1, c-1
        print(find_multi(1, 0, n-1, b, c))

