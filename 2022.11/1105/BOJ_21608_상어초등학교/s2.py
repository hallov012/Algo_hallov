import sys
sys.stdin = open('input.txt')

def find(num):
    if len(str(num)) == n:
        ans.append(num)
        return
    for i in range(1, 10):
        temp = num*10 + i
        for j in range(2, int(temp**0.5)+1):
            if not temp % j:
                break
        else:
            find(temp)


n = int(input())
ans = []
find(2)
find(3)
find(5)
find(7)
for num in ans:
    print(num)