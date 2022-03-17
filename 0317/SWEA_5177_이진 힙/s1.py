import sys
sys.stdin = open('input.txt')

def heap_push(value):
    global heap_cnt
    heap[heap_cnt] = value
    child = heap_cnt
    parent = heap_cnt // 2
    heap_cnt += 1

    while parent and heap[child] < heap[parent]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    heap = [0] * (n + 1)
    heap_cnt = 1
    ans = 0
    for i in range(n):
        heap_push(nums[i])
    while n > 0:
        n //= 2
        ans += heap[n]
    print(f'#{tc} {ans}')