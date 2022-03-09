import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
people = list(range(1, n+1))
josephus = []
i, j = 0, 0
while sum(people) != 0:
    if not people[j]:
        i -= 1
    elif i == k - 1:
        josephus.append(people[j])
        people[j] = 0
    i += 1
    j += 1
    if i == k:
        i = 0
    if j == n:
        j = j % n
print('<', end="")
for i in range(n):
    if i == n-1:
        print(josephus[i], end="")
        print('>')
    else:
        print(josephus[i], end=", ")
