def solution(a, b, n):
    ans = 0
    cnt = n
    while cnt >= a:
        temp = (cnt // a) * b
        ans += temp
        cnt = (cnt % a) + temp
    return ans

print(solution(2, 1, 20))
print(solution(3, 1, 20))