import sys
sys.stdin = open('input.txt')

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return arr

def partition(arr, start, end):
    pivot = arr[start]
    l = start
    r = end
    done = False
    while not done:
        while l < len(arr) -1 and arr[l] <= pivot:
            if l == len(arr) - 1:
                break
            l += 1
        while r >= 0 and pivot < arr[r]:
            if r == 0:
                break
            r -= 1
        if r <= l:
            done = True
        else:
            arr[l], arr[r] = arr[r], arr[l]
    arr[start], arr[r] = arr[r], arr[start]
    return r

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    quick_sort(nums, 0, n-1)
    print(f'#{tc} {nums[n//2]}')
