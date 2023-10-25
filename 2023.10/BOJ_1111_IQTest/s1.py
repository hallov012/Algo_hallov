import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
if n <= 2:
    if n == 2 and nums[0] == nums[1]:
        print(nums[0])
    else:
        print('A')
else:
    if nums[0] == nums[1]:
        a = 0
        b = nums[0]
    # nums[1] = nums[0] * a + b
    # b = nums[1] - nums[0] * a
    # nums[2] = nums[1] * a + b
    # nums[1] * a = nums[2] - b
    # nums[1] * a = nums[2] - (nums[1] - nums[0] * a)
    # nums[1] * a = nums[2] - nums[1] + nums[0] * a
    # (nums[1] - nums[0]) * a = nums[2] - nums[1]
    else:
        a = (nums[2] - nums[1]) / (nums[1] - nums[0])
        b = nums[1] - nums[0] * a
        if int(a) != a or int(b) != b:
            print('B')
            exit()
    a = int(a)
    b = int(b)
    for i in range(n-1):
        if nums[i] * a + b != nums[i+1]:
            print('B')
            break
    else:
        print(nums[-1] * a + b)
