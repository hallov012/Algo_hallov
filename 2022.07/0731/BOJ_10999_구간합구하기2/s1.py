"""
느리게 갱신되는 세그먼트 트리
https://qrlagusdn.tistory.com/140
https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-10999%EB%B2%88-%EA%B5%AC%EA%B0%84-%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0-2
"""
import sys, math
sys.stdin = open('input.txt')

def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
    else:
        mid = (start+end)//2
        tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

# lazy list를 통해 update를 진행
def update_lazy(node, start, end):
    # 해당 노드의 lazy 값이 존재 할 때
    if lazy[node]:
        # 해당 노드의 값 update
        tree[node] += (end-start+1) * lazy[node]
        # leaf노드가 아니라면 lazy값을 자식값으로 내려줌
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        # 자신의 lazy값은 초기화
        lazy[node] = 0

def subsum(node, start, end, left, right):
    update_lazy(node, start, end)
    if left > end or right < start:
        return 0
    if start >= left and right >= end:
        return tree[node]
    mid = (start+end)//2
    return subsum(node*2, start, mid, left, right) + subsum(node*2+1, mid+1, end, left, right)

def update_range(node, start, end, idx_start, idx_end, diff):
    update_lazy(node, start, end)
    if idx_start > end or idx_end < start:
        return
    # update_range가 해당 노드의 모든 곳을 포함한다면 lazy 값을 update
    if idx_start <= start and idx_end >= end:
        tree[node] += (end-start+1) * diff
        # leaf 노드가 아니라면 자식 노드에게 변동 사항을 전달해줘야함
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    mid = (start+end)//2
    update_range(node*2, start, mid, idx_start, idx_end, diff)
    update_range(node*2+1, mid+1, end, idx_start, idx_end, diff)
    tree[node] = tree[node*2] + tree[node*2+1]

n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(m+k)]
tree = [0] * pow(2, math.ceil(math.log(n, 2))+1)
lazy = [0] * pow(2, math.ceil(math.log(n, 2))+1)

init(1, 0, n-1)

for command in commands:
    if len(command) == 3:
        a, b, c = command
        print(subsum(1, 0, n-1, b-1, c-1))
    else:
        a, b, c, d = command
        update_range(1, 0, n-1, b-1, c-1, d)


