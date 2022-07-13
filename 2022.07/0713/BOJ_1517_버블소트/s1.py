import sys
sys.stdin = open('input.txt')

def merge_sort(start, end):
    global ans
    if start < end:
        mid = (start+end)//2
        merge_sort(start, mid)
        merge_sort(mid+1, end)
        a, b = start, mid+1
        temp = []
        while a <= mid and b <= end:
            if nums[a] <= nums[b]:
                temp.append(nums[a])
                a += 1
            else:
                temp.append(nums[b])
                b += 1
                ans += mid - a + 1
        if a <= mid:
            temp = temp + nums[a:mid+1]
        if b <= end:
            temp = temp + nums[b:end+1]
        for i in range(len(temp)):
            nums[start+i] = temp[i]

n = int(input())
nums = list(map(int, input().split()))
ans = 0
merge_sort(0, n-1)
print(ans)
