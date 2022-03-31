import sys
sys.stdin = open('input.txt')

def binary_search(nums, target, start, end):
    check = 0    # 1: 이전에 왼쪽 탐색, 2: 이전에 오른쪽 탐색
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            end = mid - 1
            if check in [0, 1]:
                check = 2
            else:
                break
        else:
            start = mid + 1
            if check in [0, 2]:
                check = 1
            else:
                break
    return False

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    lst_a = list(map(int, input().split()))
    lst_a.sort()
    lst_b = list(map(int, input().split()))
    ans = 0
    for num in lst_b:
        if binary_search(lst_a, num, 0, n-1):
            ans += 1
    print(f'#{tc} {ans}')