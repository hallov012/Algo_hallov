import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
total = sum(nums)
for _ in range(m):
    idx, x = map(int, input().split())
    total = total - nums[idx-1] + x
    nums[idx-1] = x
    # 공차, 공비를 구함
    d = nums[1] - nums[0]
    r = nums[1] / nums[0]
    flag_d, flag_r = True, True
    if d < 0:
        flag_d = False
    if r != int(r):
        flag_r = False
    # 수열의 합 공식을 이용하여 판별
    if flag_d:
        if total == n * (2*nums[0] + (n-1)*d) // 2:
            for i in range(2, n):
                if nums[i] - nums[i-1] != d:
                    flag_d = False
                    break
        else:
            flag_d = False
    if flag_r:
        if total == nums[0] * (r**n-1) // (r-1):
            for i in range(2, n):
                if nums[i] / nums[i-1] != int(r):
                    flag_r = False
                    break
        else:
            flag_r = False

    if flag_d:
        print('+')
    elif flag_r:
        print('*')
    else:
        print('?')



