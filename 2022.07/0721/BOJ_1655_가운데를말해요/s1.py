"""
https://art-coding3.tistory.com/44
최대힙(leftheap), 최소힙(rightheap)을 이용하여 중간값 구하기
leftheap은 중간값보다 작은 수가 들어가고, rightheap에는 중간값보다 큰 수가 들어간다
짝수번째 시도일 경우, 중간의 두 수 중 작은 값을 외쳐야하므로 leftheap에서 가져와야한다
"""
import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
leftheap, rightheap = [], []
for _ in range(n):
    num = int(input())
    # leftheap과 rightheap의 길이가 같으면 중간값의 기준이 되는 leftheap에 수를 넣는다
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -num)
    # 만약 길이가 같지 않다면 길이를 맞추기 위해 rightheap에 넣는다
    else:
        heapq.heappush(rightheap, num)
    # 만약 leftheap의 루트가 rightheap의 루트보다 크다면 둘의 루트를 바꿔준다
    # 왜? leftheap은 중간값을 기준으로 작은 값, rightheap은 중간값을 기준으로 큰 값이 들어가므로 rightheap의 루트가 항상 더 커야한다
    if rightheap and -leftheap[0] > rightheap[0]:
        left_root = heapq.heappop(leftheap)
        right_root = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -right_root)
        heapq.heappush(rightheap, -left_root)
    # 중간값인 leftheap의 루트를 출력한다
    print(-leftheap[0])