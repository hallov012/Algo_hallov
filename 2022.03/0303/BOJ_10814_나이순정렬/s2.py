import sys
sys.stdin = open('input.txt')

n = int(input())
age_lst = [0] * n
name_lst = [''] * n
for i in range(n):
    age, name = map(str, input().split())
    age_lst[i] = int(age)
    name_lst[i] = name
age_set = set(age_lst)
for age in age_set:
    same_age = []
    for i in range(n):
        if age_lst[i] == age:
            same_age.append(name_lst[i])
    for j in range(len(same_age)):
        print(age, same_age[j])

