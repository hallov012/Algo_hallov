"""
https://hooongs.tistory.com/118
1. a를 배열에 넣는다
2. b는 딕셔너리에 넣어준다 => key: 식별번호 value: index
3. tree 선언
4. a배열을 기준으로 for문 돌리기
5. b[a의 식별번호]의 인덱스를 방문했을 때 겹치는 선의 수 세기
6. b[a의 식별번호]의 인데스를 방문했다는 의미로 tree update
"""
import sys, math
sys.stdin = open('input.txt')

def subsum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]
    mid = (start+end)//2
    return subsum(node*2, start, mid, left, right) + subsum(node*2+1, mid+1, end, left, right)

def update(node, start, end, idx):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = 1
        return tree[node]
    else:
        mid = (start+end)//2
        update(node*2, start, mid, idx)
        update(node*2+1, mid+1, end, idx)
        tree[node] = tree[node*2] + tree[node*2+1]
        return tree[node]

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b_dict = {}
for i in range(n):
    b_dict[b[i]] = i

tree = [0] * pow(2, math.ceil(math.log(n, 2))+1)
ans = 0

for num in a:
    idx = b_dict[num]
    ans += subsum(1, 0, n-1, idx, n-1)
    update(1, 0, n-1, idx)

print(ans)

