"""
세그먼트 트리(Segment Tree: 구간트리) 내용 학습하기
https://velog.io/@corone_hi/%EA%B5%AC%EA%B0%84-%ED%8A%B8%EB%A6%AC-Segment-Tree-Python
https://hini7.tistory.com/42
"""
import sys, math
sys.stdin = open('input.txt')

def init(node, s, e):
    # node가 leaf 노드인 경우 배열의 원소를 반환 => 리프노드는 배열의 그 원소를 가져야하기 때문
    if s == e:
        tree[node] = nums[s]
        return tree[node]
    else:
        # 재귀함수를 이용해 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장
        tree[node] = init(node*2, s, (s+e)//2) + init(node*2+1, (s+e)//2+1, e)
        return tree[node]

def update(node, s, e, idx, diff):
    if idx < s or idx > e:
        return
    tree[node] += diff
    # leaf 노드가 아닌 경우 자식들도 변경해주어야 함
    if s != e:
        update(node*2, s, (s+e)//2, idx, diff)
        update(node*2+1, (s+e)//2+1, e, idx, diff)

"""
구간합
node가 담당하는 구간 [s, e]
합을 구해야하는 구간 [left, right]
"""
def subsum(node, s, e, left, right):
    # 겹치치 않는 부분 => 탐색을 이어갈 필요 없음
    if left > e or right < s:
        return 0
    # [left, right] 안에 [s, e]가 포함되기 때문에 그 node의 자식도 모두 포함 됨 => 더 이상 호출 할 필요가 없음
    if left <= s and e <= right:
        return tree[node]
    # 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작
    return subsum(node*2, s, (s+e)//2, left, right) + subsum(node*2+1, (s+e)//2+1, e, left, right)


input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
tree = [0] * (pow(2, math.ceil(math.log(n, 2))+1))
init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - nums[b-1]
        nums[b-1] = c
        update(1, 0, n-1, b-1, diff)
    elif a == 2:
        print(subsum(1, 0, n-1, b-1, c-1))

