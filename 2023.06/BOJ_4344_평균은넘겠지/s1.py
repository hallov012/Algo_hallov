import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def roundNum(val, digits):
    return round(val+10**(-len(str(val))-1), digits)


C = int(input())
for _ in range(C):
    n, *nums = map(int, input().split())
    mean = sum(nums) / n
    over_cnt = 0
    for num in nums:
        if mean < num:
            over_cnt += 1
    ans = over_cnt / n * 100
    print(f"{roundNum(ans, 3):.3f}%")