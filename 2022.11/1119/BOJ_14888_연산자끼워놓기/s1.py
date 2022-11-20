import sys
sys.stdin = open('input.txt')

def find(idx, cnt):
    global max_ans, min_ans
    if idx == n:
        max_ans = max(max_ans, cnt)
        min_ans = min(min_ans, cnt)
    if opers[0]:
        opers[0] -= 1
        find(idx+1, cnt + nums[idx])
        opers[0] += 1
    if opers[1]:
        opers[1] -= 1
        find(idx+1, cnt - nums[idx])
        opers[1] += 1
    if opers[2]:
        opers[2] -= 1
        find(idx+1, cnt*nums[idx])
        opers[2] += 1
    if opers[3]:
        opers[3] -= 1
        if cnt > 0 and nums[idx] > 0:
            find(idx+1, cnt//nums[idx])
        elif cnt > 0 and nums[idx] <= 0:
            temp = cnt // (-nums[idx])
            find(idx+1, -temp)
        else:
            temp = (-cnt) // nums[idx]
            find(idx+1, -temp)
        opers[3] += 1

n = int(input())
nums = list(map(int, input().split()))
# 덧셈 뺄셈 곱셈 나눗셈
opers = list(map(int, input().split()))
max_ans = -sys.maxsize
min_ans = sys.maxsize
find(1, nums[0])
print(max_ans)
print(min_ans)
