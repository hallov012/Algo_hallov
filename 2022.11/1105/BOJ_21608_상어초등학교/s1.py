import sys
sys.stdin = open('input.txt')

def find(num, cnt):
    if cnt == n:
        ans.append(num)
        return
    for i in range(1, 10):
        temp = num + str(i)
        if nums[int(temp)]:
            find(temp, cnt+1)

n = int(input())
m = 10**n
nums = [1] * (m+1)
nums[0] = nums[1] = 0
for i in range(2, int(m**0.5)+1):
    if nums[i]:
        for j in range(2*i, m+1, i):
            nums[j] = 0
ans = []
find("", 0)
ans.sort()
for num in ans:
    print(num)