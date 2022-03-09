a, b = map(int, input().split())

for i in range(min(a, b), 0, -1):
    if not a % i and not b % i:
        print(i)
        break
for i in range(max(a, b), a * b + 1):
    if not i % a and not i % b:
        print(i)
        break